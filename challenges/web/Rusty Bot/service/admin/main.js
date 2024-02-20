import puppeteer from "puppeteer";
import express from "express";
import dotenv from "dotenv";

dotenv.config({ path: "../.env" });

const app = express();
app.use(express.json());

const port = +process.env.BOT_PORT;

async function visit(url) {
	const browser = await puppeteer.launch({
		executablePath: "/usr/bin/chromium-browser",
		headless: "new",
		args: [
			"--disable-dev-shm-usage",
			"--no-sandbox",
			"--disable-setuid-sandbox",
			"--disable-gpu",
			"--no-gpu",
			"--disable-default-apps",
			"--disable-translate",
			"--disable-device-discovery-notifications",
			"--disable-software-rasterizer",
			"--disable-xss-auditor",
		],
	});
	const ctx = await browser.createIncognitoBrowserContext();

	const page = await ctx.newPage();
	try {
		await page.goto(
			`http://${process.env.SERVER_ALIAS}:${process.env.SERVER_PORT}/`,
			{
				timeout: 5000,
				waitUntil: "networkidle2",
			}
		);
		await page.type("#login_username", "admin");
		await page.type("#login_password", process.env.ADMIN_PASSWORD);
		await Promise.all([
			page.waitForNavigation({
				timeout: 5000,
			}),
			page.click("#login_submit"),
		]);

		// Go to your URL
		await page.goto(url, { timeout: 10 * 1000, waitUntil: "networkidle2" });
		await page.waitForTimeout(30 * 1000);
	} finally {
		await page.close();
		await ctx.close();
		await browser.close();
	}
}

app.post("/visit", async (req, res) => {
	const url = req.body.url;
	if (
		url === undefined ||
		(!url.startsWith("http://") && !url.startsWith("https://"))
	) {
		return res.status(400).send({ error: "Invalid URL" });
	}

	try {
		console.log(`[*] Visiting ${url}`);
		await visit(url);
		console.log(`[*] Done visiting ${url}`);
		return res.sendStatus(200);
	} catch (e) {
		console.error(`[-] Error visiting ${url}: ${e.message}`);
		return res.status(400).send({ error: e.message });
	}
});

app.listen(port, async () => {
	console.log(`[*] Listening on port ${port}`);
});

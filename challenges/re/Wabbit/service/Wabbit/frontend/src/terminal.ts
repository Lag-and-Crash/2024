import { WebContainer, FileSystemTree } from '@webcontainer/api';


let webcontainer: WebContainer;

export async function boot(btn: HTMLButtonElement, out: HTMLDivElement) {

  webcontainer = await WebContainer.boot()

  const files: FileSystemTree = {
    'go': {
      file: {
        contents: new Uint8Array(await (await fetch('./go.wasm')).arrayBuffer())
      }
    }
  }

  await webcontainer.mount(files);

  btn.addEventListener("click", async () => {
    const process = await webcontainer.spawn("wasm", ["go"]);
    process.output.pipeTo(
      new WritableStream({
        write(data) {
          const p = document.createElement("p");
          p.innerHTML = data;
          out.appendChild(p)
        }
      })
    )
  })

}

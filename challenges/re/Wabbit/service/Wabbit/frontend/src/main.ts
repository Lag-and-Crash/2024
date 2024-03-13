import './style.css'
import { boot } from './terminal.ts'

document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
  <div id="terminal">
    <h1>There is so much that awaits you!</h1>
    <code id="out">
    </code>
    <button id="bootButton">Find out now!</button>
  </div>
`

boot(document.querySelector<HTMLButtonElement>('#bootButton')!, document.querySelector<HTMLDivElement>('#out')!)

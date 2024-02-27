
# Solution
1. Through the file's header, identify that it is a compressed folder. Decompress it and explore each subdirectory.
2. The main source code for the app is in `app.data\device-atlas.zip\app\index.js`.
3. The program displays different icons (`l.href="loc".concat(a,".jpg")`), and records the user's current position when a button is tapped (`s.push(e.coords.latitude.toFixed(4)`).
4. The icon can be found in `app.data\device-atlas.zip\resources\`, while the CSS file contains a hint:
```/*
Route: wyjmD|sgkNg_@`@aCoEsBhFc_@TiAsA]oC\gIHwEcHpBAfEoGjBeHrBLnA{D~Hs@qGcIdCaEtBHfC

More compact, thanks to Google. */
```
5. Searching online for "Google route encode" will lead you to this [website](https://developers.google.com/maps/documentation/utilities/polylineutility), which can be used to decode the route.
6. Each icon represents a physical building that can be found along the route.
7. Knowing the location of each point, construct a solve script (such as the one in `\solution\solve.js`) 



You can try some dynamic analysis using the [FitBit emulator and SDK](https://dev.fitbit.com/getting-started/).
As the mentioned in the challenge description, you'll have trouble running the program as it is. To fix it, open app.data\manifest.json and modify `"filename": "???.zip",` to `"filename": "device-atlas.zip",` instead.
Then, zip the archive back up, place it in the `build` folder, and install.
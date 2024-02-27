import * as document from "document";
import { geolocation } from "geolocation";
import * as crypto from "crypto";


const BigTitle = document.getElementById("BigTitle");
const Subtitle = document.getElementById("Subtitle");
const image = document.getElementById("logo");
const startButton = document.getElementById("startButton");


startButton.layer = 99;

BigTitle.textContent = "KillCode Decryptor";
Subtitle.textContent = "Emergency Use Only";
  
var flag = [198, 201, 201, 241, 234, 205, 180, 185, 272, 219, 236, 222, 227, 238, 183, 138, 177, 185, 184, 167, 160, 190, 199, 135, 128, 152, 159, 189, 178, 155, 191, 226, 131, 128, 152]


var loc = 1;
var coordArray = []
startButton.addEventListener("click", async function start() {
    

    if (loc < 5){
        geolocation.getCurrentPosition(function(position) {
            coordArray.push(position.coords.latitude.toFixed(4));
            coordArray.push(position.coords.longitude.toFixed(4));
            
         })
         
        loc += 1;
        image.href = `loc${loc}.jpg`;
    }
    
    else{
        
        await geolocation.getCurrentPosition(async function(position) {
            coordArray.push(position.coords.latitude.toFixed(4));
            coordArray.push(position.coords.longitude.toFixed(4));
            BigTitle.textContent = "KillCode:";
            
            
            image.style.display='none';
            startButton.style.display='none';
          
            var key=coordArray.join(" ")
            console.log(key);

            var keyarray = []
            for (let i=0;i<key.length;i++){
                keyarray.push(key.charCodeAt(i))
            }
            

            flag.reverse();

            let padding = flag.length-key.length%flag.length;
            for (let i=0;i<padding;i++){
                keyarray.push(0);
            }
            keyarray.reverse();

            for (let i=0;i<keyarray.length;i++){
                flag[i%flag.length]-=keyarray[i];
            }

            flag.reverse();
            var output = '';
            for (let i=0;i<flag.length;i++){
                output+= String.fromCharCode(flag[i]);
            }
            Subtitle.textContent=output;
          
         });

        }
  })

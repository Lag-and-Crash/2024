// Encrypted flag; extracted from index.js
var c = [198, 201, 201, 241, 234, 205, 180, 185, 272, 219, 236, 222, 227, 238, 183, 138, 177, 185, 184, 167, 160, 190, 199, 135, 128, 152, 159, 189, 178, 155, 191, 226, 131, 128, 152]

// Hardcoded key with correct coordinates extracted from encoded polyline
var t = "28.5745 -80.6527 28.5806 -80.6535 28.5806 -80.6501 28.5848 -80.6532 28.5885 -80.6554"

// decryption code; copied from index.js
n=[]
for(d=0;d<t.length;d++)n.push(t.charCodeAt(d))
c.reverse()
a=c.length-t.length%c.length
for(d=0;d<a;d++)n.push(0)
n.reverse()
for(d=0;d<n.length;d++)c[d%c.length]-=n[d]
c.reverse()
f=""
for(d=0;d<c.length;d++)f+=String.fromCharCode(c[d])
console.log(f)
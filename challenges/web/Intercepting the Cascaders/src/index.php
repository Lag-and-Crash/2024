
<!DOCTYPE HTML>  
<html>
<head>
<style>
/* Source: https://codepen.io/savnac/pen/gOYMzvq */
BODY {
  margin: 0;
}

.rdm { position: absolute; width: 100%; height: 100%; background-size: 100% 100%; background: radial-gradient(ellipse at center, #feffff 0%,#ddf1f9 50%,#a0d8ef 100%); }

.t3d { position:absolute; left:50%; top:50%; margin-top:-125px; font-size:200px; font-family:'Fredoka One'; letter-spacing:-0.1em; color:#00D98D; }

.bf div { position:absolute; background:transparent; text-align:center; width:1000px; height:250px; }

.t3d > div { transform-style:preserve-3d; animation:spin 3s linear infinite; }

@keyframes spin { 
  0% { transform: rotateY(0deg); }
  100% { transform: rotateY(360deg); }
}

@keyframes wobble { 
  0% { transform: rotateX(0deg) rotateX(0deg); }
  25% { transform: rotateX(-10deg) rotateX(10deg); }
  60% { transform: rotateX(5deg) rotateX(10deg); }
  75% { transform: rotateX(20deg) rotateX(-10deg); }   
  100% { transform: rotateX(0deg) rotateX(0deg); }
}

.t3d { transform-style:preserve-3d; transform:perspective(2000px); } 

.t3d > div > div { transform-style:preserve-3d; transform:translateX(-500px); }

.bf { transform-style:preserve-3d; transform:rotatex(0deg); animation:wobble 3s ease-out infinite; }

.bf div:nth-child(1) { transform:translateZ( 12px); }
.bf div:nth-child(2) { transform:translateZ(  9px); }
.bf div:nth-child(3) { transform:translateZ(  6px); }
.bf div:nth-child(4) { transform:translateZ(  3px); }
.bf div:nth-child(5) { transform:translateZ(  0px); }
.bf div:nth-child(6) { transform:translateZ( -3px); }
.bf div:nth-child(7) { transform:translateZ( -6px); }
.bf div:nth-child(8) { transform:translateZ( -9px); }
.bf div:nth-child(9) { transform:translateZ(-12px); }

.bf div {
  color: #00D98D;
  text-shadow: 0px 0p 14px rgba(145,245,225,.3);
}
.bf div:first-child,
.bf div:last-child {color: #2B3B45;}
.bf div:first-child { 
  _color: rgba(145, 195, 245, 1);
  _color: rgba(255, 255, 95, 1);
  
  _background-clip:text;}

.bf div:nth-child(5) { text-shadow:0px 0px 1px rgba(255,255,90,.5), 0px 0px 2px rgba(255,255,90,1), 0px 0px 15px rgba(255,255, 90,1); }
</style>
</head>
<body>  
<h2>QUT CSS Tester - 3D Text!</h2>
<p>
<?php
ini_set('allow_url_fopen', false);
ini_set('allow_url_include', false);
stream_wrapper_unregister('http');
stream_wrapper_unregister('ftp');
stream_wrapper_unregister('zlib');
stream_wrapper_unregister('data');
stream_wrapper_unregister('glob');
stream_wrapper_unregister('phar');
stream_wrapper_unregister('rar');
stream_wrapper_unregister('ogg');
stream_wrapper_unregister('expect');

if (isset($_GET['file'])) {
    $text = substr(file_get_contents($_GET['file'], true),0,35);
    $file = fopen("files/1d788013b9c73e1dead5b9758b56b9dd.txt", "w");
    fwrite($file, $text);
    fclose($file);
    echo "<div class=\"rdm\">
    <div class=\"t3d\"> 
      <div>
        <div>
          <div class=\"bf\">";
    echo "<div>";
    include('files/1d788013b9c73e1dead5b9758b56b9dd.txt');
    echo "</div>";
    echo "<div>";
    include('files/1d788013b9c73e1dead5b9758b56b9dd.txt');
    echo "</div>";
    echo "<div>";
    include('files/1d788013b9c73e1dead5b9758b56b9dd.txt');
    echo "</div>";
    echo "<div>";
    include('files/1d788013b9c73e1dead5b9758b56b9dd.txt');
    echo "</div>";
    echo "<div>";
    include('files/1d788013b9c73e1dead5b9758b56b9dd.txt');
    echo "</div>";
    echo "<div>";
    include('files/1d788013b9c73e1dead5b9758b56b9dd.txt');
    echo "</div>";
    echo "<div>";
    include('files/1d788013b9c73e1dead5b9758b56b9dd.txt');
    echo "</div>";
    echo "<div>";
    include('files/1d788013b9c73e1dead5b9758b56b9dd.txt');
    echo "</div>";
    echo "<div>";
    include('files/1d788013b9c73e1dead5b9758b56b9dd.txt');
    echo "</div>";
    echo "
          </div>
        </div>
      </div>
    </div>
  </div>";
} else {
    echo "<div><a href='/index.php?file=files/test1.txt'>test1</a></div><div><a href='/index.php?file=files/test2.txt'>test2</a></div><div><a href='/index.php?file=files/test3.txt'>test3</a></div>";
}
?>
</body>
</html>
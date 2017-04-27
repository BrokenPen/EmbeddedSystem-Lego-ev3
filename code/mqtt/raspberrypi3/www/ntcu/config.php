
<!-- let include some javascript here : -->
<script type="text/javascript" src="./script/canvasjs.min.js"></script>
<script type="text/javascript" src="./script/jquery-latest.js"></script> 
<script type="text/javascript" src="./script/jquery.tablesorter.js"></script>
<link rel="stylesheet" type="text/css" href="./css/green/style.css">

<?php
  
  $mysqlConfig = [
    'host' => 'localhost',
    'port' => '3306',
    'name' => 'mqtt',
    'username' => 'raspberrypi3',
    'password' => 'formosa',
    'charset' => 'utf8'
    ];
    
  
  echo "\nI am config.php";

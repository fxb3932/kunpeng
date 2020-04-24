<?php
$img_file = file_get_contents("11.11.png");
echo base64_encode($img_file);
echo "\n"
?>

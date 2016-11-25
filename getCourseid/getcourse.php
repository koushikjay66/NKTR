<?php 
require 'database.php';
require 'functions.php';

date_default_timezone_set("Asia/Dhaka");

$day=array("SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT");

$day =strtoupper(date("D", time()));

$hour=date("G", time());

$min=date("i", time());

$ip=getRealIpAddr();

echo get_course_id_section(getSlotTime($hour, $min), $ip, $day);
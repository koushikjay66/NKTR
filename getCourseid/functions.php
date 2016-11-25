<?php


function getRealIpAddr()
{
  if (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))   //to check ip is pass from proxy
    {
      $ip=$_SERVER['HTTP_X_FORWARDED_FOR'];
    }
    elseif (!empty($_SERVER['HTTP_CLIENT_IP']))   //check ip from share internet
    {
      $ip=$_SERVER['HTTP_CLIENT_IP'];
    }else
    {
      $ip=$_SERVER['REMOTE_ADDR'];
    }
    return $ip;
}// End of function 


function getSlotTime($hr, $min){

  $times=array("8:00-9.20", "9.30-10.50", "11.00-12.20", "12.30-1.50", "2.00-");

  $time=floatval($hr.".".$min);
  if($time>=8.00 && $time<9.29){

    return "8:00";
  }elseif($time>=9.30 && $time<10.59){

    return "9.30";
  }elseif($time>=11.00 && $time<12.29){

    return "11.00";
  }elseif($time>=12.30 && $time<13.59){

    return "12.30";
  }elseif($time>=14.00 && $time<15.29){

    return "14.00";
  }elseif($time>=15.30 && $time<16.59){

    return "15.30";
  }elseif($time>=17.00 && $time<18.29){

    return "17.00";
  }elseif($time>=18.30 && $time<19.59){

    return "18.30";
  }elseif($time>=20.00 && $time<21.29){

    return "20.00";
  }

}// End of FUNCTION

function get_course_id_section($time, $ip, $day){
  $database = new database();
  $sql = "SELECT course, section FROM room_course WHERE day='{$day}' AND room_ip = '{$ip}' AND slot_id IN (SELECT slot_id FROM slot WHERE time ='{$time}') LIMIT 1";


 $res=$database->fetch_result($database->perform_query($sql));

 return $res["course"].",".$res["section"];


}// ENd of function  get_course_id_Section


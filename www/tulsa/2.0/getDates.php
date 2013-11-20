<?php
//$cur_date = date('Y-m-d');
$subdomain = explode(".", $_SERVER['HTTP_HOST']);
$environ = $subdomain[0] == 'dev' ? 'dev' : '';

$con = mysql_connect("db2536.perfora.net", "dbo336192140", "tulsafoobar");
if (!$con) die('Could not connect to database: ' . mysql_error());
mysql_select_db("db336192140", $con);

for($i=0; $i<6; $i++) {
    $temp_date = date('Y-m-d', strtotime('now - ' . $i . 'days')); 
    $query = "select count(*) as ct  from " . $environ . "records where bookingDate = '" . $temp_date . "'";
    $result = mysql_query($query);
    while($row = mysql_fetch_object($result)) {
        $ret[$i] = Array($row->ct, $temp_date);
    }
}
echo json_encode($ret);
//print_r($ret);
//echo json_encode($json_dates);
mysql_close();
?>

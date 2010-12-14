<?php
/* if the subdomain is dev, use the dev table (devrecords), otherwise just leave blank */
$subdomain = explode(".", $_SERVER['HTTP_HOST']);
$environ = $subdomain[0] == 'dev' ? 'dev' : '';

$con = mysql_connect("db2536.perfora.net", "dbo336192140", "tulsafoobar");
if (!$con) die('Could not connect to database: ' . mysql_error());
mysql_select_db("db336192140", $con);


for($i=0; $i<7; $i++) {
    $json_dates[$i] = date('Y-m-d', strtotime('now - ' . $i . 'days'));
}

//$one_week_ago = date('Y-m-d', strtotime('now - 7 days'));
$query = "select * from " . $environ . "records where bookingDate = '" . $json_dates[5] . "' ORDER BY personID DESC";
$result = mysql_query($query);
while($row = mysql_fetch_object($result)) {
    $rows[] = $row;
}
echo json_encode($rows);
mysql_close();
?>

<?php
session_start();

/* if the subdomain is dev, use the dev table (devrecords), otherwise just leave blank */
$subdomain = explode(".", $_SERVER['HTTP_HOST']);
$environ = $subdomain[0] == 'dev' ? 'dev' : '';

$con = mysql_connect("db2536.perfora.net", "dbo336192140", "tulsafoobar");
if (!$con) die('Could not connect to database: ' . mysql_error());
mysql_select_db("db336192140", $con);


if($_GET['thisDay'] && isset($_SESSION['mugshots_is_logged_in'])) {
    $query = "select * from " . $environ . "records where bookingDate = '" . $_GET['thisDay'] . "' ORDER BY personID DESC";
    $result = mysql_query($query);
    while($row = mysql_fetch_object($result)) {
        $row->refetch_link = "<a href='' onclick='ajax_refetch(" . $row->personId . ");'</a>";
        $rows[] = $row;
    }
    echo json_encode($rows);
} elseif($_GET['thisDay']) {
    $offset = $_GET['offset'] ? " OFFSET " . $_GET['offset'] : "OFFSET 0";
    $query = "select * from " . $environ . "records where bookingDate = '" . $_GET['thisDay'] . "' ORDER BY personID DESC limit 20 " . $offset;
    $result = mysql_query($query);
    while($row = mysql_fetch_object($result)) {
        $row->refetch_link = "";        
        $rows[] = $row;
    }
    echo json_encode($rows);
}
mysql_close();
?>

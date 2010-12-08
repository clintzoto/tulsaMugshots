<?php
if($_GET['id']) {
    $con = mysql_connect("db2536.perfora.net", "dbo336192140", "tulsafoobar");
    if (!$con) die('Could not connect to database: ' . mysql_error());
    mysql_select_db("db336192140", $con);

    $query = "select * from records where personId=" . $_GET['id'];
    $result = mysql_query($query);
    $row = mysql_fetch_object($result);
    echo json_encode($row);
    mysql_close();
}
?>

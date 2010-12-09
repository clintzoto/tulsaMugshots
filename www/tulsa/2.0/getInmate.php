<?php
if($_GET['id']) {
    $con = mysql_connect("db2536.perfora.net", "dbo336192140", "tulsafoobar");
    if (!$con) die('Could not connect to database: ' . mysql_error());
    mysql_select_db("db336192140", $con);

    $race_array = array("W"=>"White", "B"=>"Black", "H"=>"Hispanic", "I"=>"Pacific Islander", "O"=>"Other");

    $query = "select * from records where personId=" . $_GET['id'];
    $result = mysql_query($query);
    $row = mysql_fetch_object($result);
    $row->race = $race_array[$row->race];
    $row->gender = $row->gender == "M" ? "Male" : "Female";

    echo json_encode($row);
    mysql_close();
}
?>

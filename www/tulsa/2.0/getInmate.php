<?php
if($_GET['id']) {
    $subdomain = explode(".", $_SERVER['HTTP_HOST']);
    $environ = $subdomain[0] == 'dev' ? 'dev' : '';
    $con = mysql_connect("", "", "");
    if (!$con) die('Could not connect to database: ' . mysql_error());
    mysql_select_db("", $con);

    $race_array = array("W"=>"White", "B"=>"Black", "H"=>"Hispanic", "I"=>"Pacific Islander", "O"=>"Other");

    $query = "select * from " . $environ  . "records where personId=" . $_GET['id'];
    $result = mysql_query($query);
    $row = mysql_fetch_object($result);
    $row->race = $race_array[$row->race];
    $row->gender = $row->gender == "M" ? "Male" : "Female";

    echo json_encode($row);
    mysql_close();
}
?>

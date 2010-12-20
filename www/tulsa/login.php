<?php

$con = mysql_connect("db2536.perfora.net", "dbo336192140", "tulsafoobar");
if (!$con) die('Could not connect to database: ' . mysql_error());
mysql_select_db("db336192140", $con);
session_start();

if($_SERVER['REQUEST_METHOD'] == "POST") {
     $result = mysql_query("SELECT * FROM users WHERE username='" . $_POST['username'] . "' AND password=MD5('" . $_POST['password'] . "')");
     if(mysql_num_rows($result) > 0) {
         $_SESSION['mugshots_is_logged_in'] = 1;
     }
}

if(!isset($_SESSION['mugshots_is_logged_in'])) {
    // display your login here

$html = '<form method="POST" action="login.php">';
$html .= 'Username: <input type="text" name="username" size="20">';
$html .= 'Password: <input type="password" name="password" size="20">';
$html .= '<input type="submit" value="Submit" name="login">';
$html .= '</form>';
echo $html;

} else {
    header("Location: index.php");
}
?>


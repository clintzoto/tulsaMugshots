<!DOCTYPE html> 
<html> 
<head>
<title>Tulsa County Inmates</title>
<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0; user-scalable=0;" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
<!--<link rel="stylesheet" href="css/jquery.mobile-1.0a2.min.css" />-->
<link rel="stylesheet" href="http://code.jquery.com/mobile/1.0a2/jquery.mobile-1.0a2.min.css" />
<link rel="stylesheet" href="css/mugshots.css" />
<!--<link rel='stylesheet' media='screen and (min-width: 1px) and (max-width: 480px)' href='css/480.css' />-->
<!--<link id="size-stylesheet" rel="stylesheet" href="css/size-default.css" />-->
<script src="javascript/jquery-1.4.4.min.js"></script>
<script src="javascript/jquery.mobile-1.0a2.min.js"></script>
<script src="javascript/jquery-ui-1.8.7.custom.min.js"></script>
<script src="javascript/mugshots.js"></script>
</head>
<body> 
<style>
#inmate_detail_img {width: auto;}
</style>
<div data-role="page" data-theme="b" id="datePage">
    <div data-role="header">
        <center><h2>TULSA County Inmates</h2></center>
    </div>
    <div data-role="content">
        <ul id="dates" data-role="listview" data-theme="b">
        </ul>
    </div>
</div>

<div data-role="page" data-theme="b" id="inmateBriefs">
    <div data-role="header">
        <h2 id="inmate_briefs_header">TULSA County</h2>
    </div>
    <div data-role="content">
        <ul id="inmateBrief" data-role="listview" data-theme="b">
        </ul>
    </div>
    <div data-role="header">
        <h2>&nbsp;</h3>
    </div>
</div>
<div data-role="page" data-theme="b" id="inmateDetails">
    <div data-role="header">
        <h2>TULSA County</h2>
    </div>
    <div data-role="content" id="inmateDetail">
    </div>
</div>
</body>
</html>



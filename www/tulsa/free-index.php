<!DOCTYPE html> 
<html> 
<head>
<title>Tulsa County Inmates</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="css/jquery.mobile-1.1.0.css" />
<script src="http://code.jquery.com/jquery-1.6.4.min.js"></script>
<script src="javascript/jquery.mobile-1.1.0.js"></script>
<script src="javascript/mugshots.js"></script>
</head>
<body> 
    <script>

    $("#dates li").live('click', function(e){ 
        daySession.prototype.day = $(this).data("value"); 
        getInmatesByDate($(this).data("value"));
        buildInmateBriefs();
        refresh();
    }); 
   
    $("#inmateBriefs li").live('click', function (e){
            inmates_index= $(this).data("value");
            daySession.prototype.currInmateDetail = inmates_index;
            buildInmateDetail();
            refresh();
    });
    </script>

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
    <div id="inmate_briefs_header" data-role="header">
        <h2>Tulsa County Inmates</h2>
    </div>
    <div data-role="content">
        <ul id="inmateBrief" data-role="listview" data-theme="b">
        </ul>
    </div>
    <div id="inmate_briefs_footer" data-role="footer">
        <a href="" onclick="updateInmatesByDate(); refresh();">More</a>
    </div>
</div>

<div data-role="page" data-theme="b" id="inmateDetails">
    <div data-role="header">
        <h2>TULSA County</h2>
    </div>
    <div data-role="content" id="inmateDetail">
        <div class="details">
            <img id="inmate_detail_img" /><br />
            <span id="inmate_name"></span><span id="inmate_race"></span><span id="inmate_gender"></span><br />
            Resides <span id="inmate_address"></span><br /><span id="inmate_city"></span>, <span id="inmate_state"></span> <span id="inmate_zip"></span><br />
            Born <span id="inmate_birth"></span> <span id="inmate_hair"></span><span id="inmate_eyes"></span><br />
            <span id="inmate_height"></span> tall <span id="inmate_weight"></span><br />
            Arrested by <span id="inmate_arrested_by"></span> with <span id="inmate_agency"></span><br />
            at <span id="inmate_arrest_time"></span> on <span id="inmate_arrest_date"></span> for <br />
            <span style="color: red;" id="inmate_charge"></span><br />
            <span style="color: red;" id="inmate_charge2"></span><br />
            <span style="color: red;" id="inmate_charge3"></span><br />
            Booked at <span id="inmate_book_time"><span> on <span id="inmate_book_date"></span>
            <span id="inmate_bond"></span>
        </div>
    </div>
</div>
</body>
</html>



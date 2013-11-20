
$(document).ready(function() {
var Session = $.Class.create({
    dates: "",
    construct: function(){
        $.ajax({
            url: "/tulsa/2.0/getDates.php",
            dataType: 'json',
            //data: "thisDay=" + thisDaay,
            async: true,
            success: function(data){
                this.dates = data;                
            }
        });
    },
    getInmates: function(day){
        $.ajax({
            url: "/tulsa/2.0/getInmatesByDate.php",
            dataType: 'json',
            data: "thisDay=" + day,
            async: true,
            success: function(data){
                return data;
            }
        });
    }
});

var daySession = $.Class.create(Session, {
    day: "",
    inmates: "",
    //currInmateDetail: "", 
    init: function(){
        this.construct();
    },
    getDates: function(){
        console.log(this.dates);
        buildDatesLi(this.dates);
        //return this.dates;
    },
    returnInmates: function(day){
        this.day = day;
        buildInmateBriefs(this.getInmates(this.day));
        
    },
    returnCurrInmateDetail: function(ndx){
        buildInmateDetail(this.inmates[ndx]); 
    }
});


    

/*
$.("#inmateBriefs").live('pagebeforecreate', function(event, ui){
    console.log("this page was just hidden: " + ui.prevPage);
});
*/

var blah = new daySession();
blah.init();

$("#dates li").live('click', function(){
    blah.getInmates($(this).data("value"));
    getInmatesByDate(blah.returnDay($(this).data("value")));
});

$("#inmateBriefs li").live('click', function (e){
    inmates_index= $(this).data("value");
    blah.returnCurrInmateDetail($(this).data("value"));
});



function buildDatesLi(data) {
    var iloop = data.length;
    while(iloop--) {
       var DatesItem = '<li data-value="' + data[iloop][1] + '" id="datesItem"><a href="#inmateBriefs">' + data[iloop][1] + '</a><span class="ui-li-count ui-btn-up-c ui-btn-corner-all">' + data[iloop][0] + '</span></span>';
        $(DatesItem).prependTo("#dates");
    }
    $("#dates").listview("refresh");
}

 function buildInmateBriefs(thisDay, inmates) {
    daySession.prototype.inmates = inmates
    $("#inmateBrief li").remove();
        var iloop = inmates.length;
      
        while(iloop--) {
            //build the listview
            //php that loads arrayDailyInmates checks to for generic no_photo.jpg and updates mugshotHash with no_photo
            //this prevents records with no photos from creating a new image file when there is no photo
            var mugImageLink = inmates[iloop].mugshotHash == "no_photo" ? "no_photo" : inmates[iloop].personId + "-" + inmates[iloop].mugshotHash;  
            var split_name = inmates[iloop].name.split(",");
            var inmate = "<li data-value='" + iloop + "'><a  href='#inmateDetails' >"
                + "<img  src='/tulsa/mugs/thumbs85x85/" + mugImageLink + ".jpg' />"
                + split_name[0] 
                + "<br />" 
                + split_name[1] 
                + "</a><br /><span style='color:white; font-size: 13px;'>" 
                + inmates[iloop].bookingTime  
                + "</span>"
                + "</li>";
            $(inmate).prependTo("#inmateBrief");
        }
    $("#inmateBrief").listview("refresh");
  }
function buildInmateDetail(objInmate){
        objTemplate = $('#inmateDetail');
        if(objInmate.refetch_link) {
            $(objTemplate).append("<br /><a href='javascript:void(0);' onclick='ajax_refetch(" + objInmate.personId + ");'>refetch info</a>");
            $(objTemplate).append("<br />" + objInmate.personId);
            $(objTemplate).append("<br />http://dev.pillowhammer.com/tulsa/mugs/" + objInmate.personId + "-" + objInmate.mugshotHash + ".jpg");
        }
        var mugImageLink = objInmate.mugshotHash == "no_photo" ? "no_photo" : objInmate.personId + "-" + objInmate.mugshotHash;
        $('#inmate_detail_img', objTemplate).attr('src', '/tulsa/mugs/thumbs320/' + mugImageLink + '.jpg');
        $('#inmate_name', objTemplate).html(objInmate.name);
        $("#inmate_address", objTemplate).html(objInmate.address);
        $("#inmate_city", objTemplate).html(objInmate.city);
        $("#inmate_state", objTemplate).html(objInmate.state);
        $("#inmate_zip", objTemplate).html(objInmate.zip);
        $("#inmate_arrest_date", objTemplate).html(objInmate.arrestDate);
        $("#inmate_arrest_time", objTemplate).html(objInmate.arrestTime);
        $("#inmate_arrested_by", objTemplate).html(objInmate.arrestBy);
        $("#inmate_agency", objTemplate).html(objInmate.agency);
        $("#inmate_book_date", objTemplate).html(objInmate.bookingDate);
        $("#inmate_book_time", objTemplate).html(objInmate.bookingTime);
        $("#inmate_charge", objTemplate).html(objInmate.charge);
        $("#inmate_charge2", objTemplate).html(objInmate.charge2);
        $("#inmate_charge3", objTemplate).html(objInmate.charge3);
        $("#inmate_bond", objTemplate).html(objInmate.bondAmt);
        $("#inmate_birth", objTemplate).html(objInmate.birthday);
        $("#inmate_hair", objTemplate).html(objInmate.hair);
        $("#inmate_eyes", objTemplate).html(objInmate.eyes);
        $("#inmate_height", objTemplate).html(objInmate.feet + "ft " + objInmate.inches + "in");
        $("#inmate_weight", objTemplate).html(objInmate.weight + " lbs");
        $("#inmate_race", objTemplate).html(" " + objInmate.race + " ");
        $("#inmate_gender", objTemplate).html(objInmate.gender);
}

}); 

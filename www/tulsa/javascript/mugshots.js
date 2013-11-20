    //
function daySession() {
    this.day;
    this.inmates;
    this.currInmateDetail;
    this.offset = 0;
    this.nextOffset = function() {
        this.offset = this.offset + 20;
    }
    this.updateInmates = function(im) {
        for (r in im) {
            this.inmates.push(im[r]);
        }
    }

    this.returnOffset = returnOffset;
    this.returnDay = returnDay;
    this.returnInmates = returnInmates; 
    this.returnCurrInmateDetail = returnCurrInmateDetail;

    function returnOffset() { return this.offset }
    function returnDay() { return this.day; }
    function returnInmates() { return this.inmates; }
    function returnCurrInmateDetail() {return this.inmates[this.currInmateDetail]; }
} 
    var blah = new daySession();

$.getJSON("/tulsa/2.0/getDates.php", function(data) {
    buildDatesLi(data);
});

function buildDatesLi(data) {
    var iloop = data.length;
    while(iloop--) {
       var DatesItem = '<li data-value="' + data[iloop][1] + '" id="datesItem"><a href="#inmateBriefs">' 
            + data[iloop][1] + '</a><span class="ui-li-count ui-btn-up-c ui-btn-corner-all">' + data[iloop][0] + '</span></li>';
       $(DatesItem).prependTo("#dates");
    }
    $("#dates").listview("refresh");
}

function getInmatesByDate(thisDay) {
    $("#inmateBrief").empty();   
    $.ajax({
        url: "/tulsa/2.0/getInmatesByDate.php",
        dataType: 'json',
        data: "thisDay=" + thisDay, 
        async: false,
        success: function(data){
            //blah.updateInmates(data);
            daySession.prototype.inmates = data;
            return true;
        }
    });
}
function refresh() {
  //  if(buildInmateBriefs()){
   //     $("#inmateBriefs").show();
        $("#inmateBrief").listview("refresh");
  //  }
}
function updateInmatesByDate() {
    blah.nextOffset();
    thisDay = blah.returnDay();
    offset = blah.returnOffset();
    $.ajax({
        url: "/tulsa/2.0/getInmatesByDate.php",
        dataType: 'json',
        data: "thisDay=" + thisDay + "&offset=" + offset, 
        async: false,
        success: function(inmates){
            blah.updateInmates(inmates.reverse());
            iloop = inmates.length;
            while(iloop--) {
                //build the listview
                //php that loads arrayDailyInmates checks to for generic no_photo.jpg and updates mugshotHash with no_photo
                //this prevents records with no photos from creating a new image file when there is no photo
                var mugImageLink = inmates[iloop].mugshotHash == "no_photo" ? "no_photo" : inmates[iloop].personId + "-" + inmates[iloop].mugshotHash;  
                var split_name = inmates[iloop].name.split(",");
                var inmate = "<li data-value='" + (iloop + offset)  + "'><a  href='#inmateDetails' >"
                    + "<img  src='/tulsa/mugs/thumbs85x85/" + mugImageLink + ".jpg' />"
                    + split_name[0] + "<br />" + split_name[1] 
                    + "<br /><span style='color:white; font-size: 13px;'>" 
                    + inmates[iloop].bookingTime + "</span>" + "</a></li>";
                $(inmate).appendTo("#inmateBrief:first-child");
            }
        }
    });
    refresh();
}

function buildInmateBriefs() {
    var inmates = blah.returnInmates();
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
            + "<br /><span style='color:white; font-size: 13px;'>" 
            + inmates[iloop].bookingTime  
            + "</span>"
            + "</a></li>";
        $(inmate).prependTo("#inmateBrief");
    }
//    var more = "<li id='more'><a href='#inmateBriefs'>more</a></li>";
//    $(more).appendTo("#inmateBrief");        
    //return true; 
    refresh();
}

function buildInmateDetail(){
        var objInmate = blah.returnCurrInmateDetail();
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

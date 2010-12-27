    //
    $(document).ready(function() {
        loadData();
    });

/*
    function adjustStyle(width) {
        width = parseInt(width);
        if (width < 481) {
            $("#size-stylesheet").attr("href", "css/size-small.css");
        } else {
           $("#size-stylesheet").attr("href", "css/size-wide.css");
        }
    }
    $(function() {
        adjustStyle($(this).width());
        $(window).resize(function() {
            adjustStyle($(this).width());
        });
    });

*/
    function loadData() {
        $.getJSON("/tulsa/2.0/getDates.php", function(data) {
            $("#dates li").remove();
            for (i=0; i < data.length; i++) {
               var DatesItem = '<li id="datesItem"><a onclick="getInmatesByDate(\'' + data[i][1] + '\'); return true;" href="#inmateBriefs">' + data[i][1] + '</a><span class="ui-li-count ui-btn-up-c ui-btn-corner-all">' + data[i][0] + '</span></span>';
                $(DatesItem).appendTo("#dates");
            }
            $("#dates").listview("refresh");
        });
    }


    function getInmatesByDate(thisDay) {
        $("#inmateBrief li").remove();
        //$.mobile.pageLoading();
        $.mobile.pageLoading();
        $.ajax({
            url: "/tulsa/2.0/getInmatesByDate.php",
                dataType: 'json',
                data: "thisDay=" + thisDay, 
                async: false,
                success: function(data){
                    buildInmateBriefs(thisDay, data);
                    buildInmateDetails(data);
                    //$.mobile.changePage('inmateBriefs',"slide", true, false);
                    $.mobile.pageLoading( true );
                } 
            });
            $("#inmateBrief").listview("refresh");
      }




      function gotoInmateDetails(personId) {
                //$.mobile.changePage('inmateDetails',"slide",false,true);
                $(".details").hide();
                $('#inmateDetail-' + personId).show();

      }

      function buildInmateBriefs(thisDay, arrayDailyInmates) {
            for (i=0; i < arrayDailyInmates.length; i++) {
                //build the listview
                var split_name = arrayDailyInmates[i].name.split(",");
                var inmate = "<li><a onclick='gotoInmateDetails(" + arrayDailyInmates[i].personId  + ");' href='#inmateDetails' >"
                    + "<img  src='/mugs/" + arrayDailyInmates[i].personId + ".jpg' />"
                    + split_name[0] + "<br />" + split_name[1] + "</a><br /><span style='color:white; font-size: 13px;'>" 
                    + arrayDailyInmates[i].bookingTime  
                    + "</span>"
                    + arrayDailyInmates[i].update_image_link
                    + "</li>";
                $(inmate).appendTo("#inmateBrief");
            }
            //console.log($("#inmateBrief"));
      }

      function buildInmateDetails(arrayDailyInmates) {
            $.each(arrayDailyInmates, function(index, obj) {
                    objTemplate = detailTemplateMerge(obj);
                    $(objTemplate).appendTo($("#inmateDetail"));

            });
            $('.details').bind('swipeleft', function(e){
                $(e.currentTarget).hide('slide');
                $(e.currentTarget.previousSibling).show('slide');
             
/*
                $(e.currentTarget).hide();
                $(e.currentTarget.previousSibling).show();
*/
            });
            $('.details').bind('swiperight', function(e){
                $(e.currentTarget).hide('slide');
                $(e.currentTarget.nextSibling).show('slide');
            });
      }

      function detailTemplateMerge(objInmate) {
            var strTemplate = '<div class="details" style="display: none;"><img id="inmate_detail_img" /><br /><span id="inmate_name"></span>' + 
                '<span id="inmate_race"></span><span id="inmate_gender"></span><br />Resides <span id="inmate_address"></span><br /><span id="inmate_city"></span>' + 
                ', <span id="inmate_state"></span> <span id="inmate_zip"></span><br />Born <span id="inmate_birth"></span> <span id="inmate_hair"></span> ' + 
                '<span id="inmate_eyes"></span><br /><span id="inmate_height"></span> tall <span id="inmate_weight"></span><br />Arrested by <span id="inmate_arrested_by">' + 
                '</span> with <span id="inmate_agency"></span><br />at <span id="inmate_arrest_time"></span> on <span id="inmate_arrest_date"></span> for <br />' +
                '<span style="color: red;" id="inmate_charge"></span><br /><span style="color: red;" id="inmate_charge2"></span><br />' +
                '<span style="color: red;" id="inmate_charge3"></span><br />Booked at <span id="inmate_book_time"><span> on <span id="inmate_book_date"></span>' +
                '<span id="inmate_bond"></span></div>';
            var objTemplate = $(strTemplate).clone();
            $(objTemplate).attr('id', "inmateDetail-" + objInmate.personId);
            $('#inmate_detail_img', objTemplate).attr('src', '/mugs/' + objInmate.personId + '.jpg');
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
            //console.log(objTemplate)
            return objTemplate;
      }



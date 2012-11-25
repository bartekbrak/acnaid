var STORES_CURRENT_VOIVODESHIP = null;
var STORES_CURRENT_LOCALITY = null;
var STORES_SV_URL = null;
var STORES_SL_URL = null;
var VOIVODESHIP = {};
function select_locality(slug, locality_name)
{
    $.get(
        STORES_SL_URL,
        {'slug': slug, 'voivodeship': STORES_CURRENT_VOIVODESHIP},
        function(data){
            STORES_CURRENT_LOCALITY = slug;
            $("#stores-list").slideUp(500, function(){
                $("#stores-list h3 strong").html(locality_name);
                $("#stores-list ul").empty();
                var counter = 0;
                var line = $("<div class=\"line\"></div>");
                $.each(data, function(index,store){
                    line.append("<li><strong>" + store.fields.name + "</strong>"
                                + (store.fields.phone ? "<br />" + store.fields.phone : "")
                                + "<br />" + store.fields.address
                                + "<br />" + store.fields.postal_code
                                + " " + locality_name + "</li>");
                    counter++;
                    if (counter == 5) {
                        counter = 0;
                        line.append("<div style=\"clear: both;\"></div>");
                        $("#stores-list ul").append(line);
                        line = $("<div class=\"line\"></div>");
                    }
                });
                line.append("<div style=\"clear: both;\"></div>");
                $("#stores-list ul").append(line);
                $("#stores-list").slideDown(500);
            });
        },
        'json'
    );
}
function activate_locality_select()
{
    $("#locality-select li").click(function(event){select_locality($(event.currentTarget).attr("id").split('-').splice(1,50).join('-'),$(event.currentTarget).html());$("#locality-select li.active").removeClass("active");$(event.currentTarget).addClass("active");});
}
function select_voivodeship(slug)
{
    $.get(
        STORES_SV_URL,
        {'slug': slug},
        function(data){
            STORES_CURRENT_VOIVODESHIP = slug;
            $("#stores-list").slideUp(500,function(){$("#stores-list ul").empty();});
            $("#localities-list").fadeOut(200, function(){
                $("#localities-list h3 strong").html(VOIVODESHIP[slug]);
                $("#locality-select").empty();
                $.each(data, function(index,locality){
                    $("#locality-select").append("<li id=\"localityselect-" + locality.fields.slug + "\">" + locality.fields.name + "</li>");
                });
                activate_locality_select();
                $("#localities-list").fadeIn(200);
            });
        },
        'json'
    );
}

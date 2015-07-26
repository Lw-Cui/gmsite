/**
 * Created by lw on 15-7-25.
 */
function period() {
    var today = new Date();
    var hour = today.getHours();
    if (hour < 12)
        return 'morning';
    else if (hour < 18)
        return 'afternoon';
    else
        return 'evening';
}

$(document).ready(function() {
    $("#period").text(period());
    $("#clockIn")
        .click(function(){
            $(this)
                .text("CLOCKED")
                .css("color", "#19ddff");
            $.post("/clock_in/", {
                period: period(),
                }, function(data, status) {
                    var obj = JSON.parse(data)
                    //$("#attend").text(obj[period()]).slideDown(2000);
                });
        })
        .mouseenter(function() {
            $(this).animate({backgroundColor: 'white'}, 'fast').promise().done(function() {
                $(this).css("color", "#55BDFF");
            })
        })
        .mouseleave(function() {
            $(this).animate({backgroundColor: 'transparent'}, 'fast').promise().done(function() {
                $(this).css("color", "#19ddff");
            })
    });
});

/**
 *
 * Created by lw on 15-7-24.
 */
$(document).ready(function() {
    $("#title")
        .fadeIn("slow")
        .mouseenter(function () {
            $(this).fadeTo("fast", 1);
        })
        .mouseleave(function () {
            $(this).fadeTo("slow", 0.8);
        });

    $("input")
        .fadeTo("slow", 0.7)
        .focus(function () {
            $(this).fadeTo("fast", 0.95);
        })
        .blur(function () {
            $(this).fadeTo("fast", 0.7);
        });
});

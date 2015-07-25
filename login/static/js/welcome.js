/**
 * Created by lw on 15-7-25.
 */
$(document).ready(
    function welcome() {
        $("#welcome")
            .fadeIn(2000)
            .fadeOut(2000, function() {
                $(this).text("欢迎来到 ");
            })
            .fadeIn(2000)
            .fadeOut(2000, function() {
                $(this).text("Bienvenue à ");
            })
            .fadeIn(2000)
            .fadeOut(2000, function() {
                $(this).text("Добро пожаловать ");

            })
            .fadeIn(2000)
            .fadeOut(2000, function() {
            $(this).text("welcome to ");
        })
        setTimeout(welcome, 0);
    }
);

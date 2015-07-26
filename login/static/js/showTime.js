$(document).ready(
    function thisTime() {
        var today = new Date();
        var hour = today.getHours();
        var minute = today.getMinutes();
        if (minute < 10) minute = '0' + minute;
        if (hour < 10) hour = '0' + hour;
        if (minute !== window.minute) {
            $("#time")
                .fadeOut(1500, function () {
                    $(this).text(hour + ":" + minute);
                })
                .fadeIn(1500);
            window.minute = minute;
        }
        $("#time").text(hour + ":" + minute);
        setTimeout(thisTime, 3000);
    }
);

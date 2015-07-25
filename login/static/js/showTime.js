$(document).ready(
    function thisTime() {
        var today = new Date();
        var h = today.getHours();
        var m = today.getMinutes();
        if (m < 10) m = '0' + m;
        if (h < 10) h = '0' + h;
        $("#time").text(h + ":" + m);
        setTimeout(thisTime, 5000);
    }
);

$(document).ready(function thisTime() {
        var today=new Date();
        var h=today.getHours();
        var m=today.getMinutes();
        if (m < 10) m = '0' + m;
        $("#time").text(h + ":" + m);
        setTimeout(function(){thisTime();},5000);
});

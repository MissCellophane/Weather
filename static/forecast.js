$(document).ready(function() {
    function GetRequest() {
        var url = decodeURI(location.search);
        if (url.indexOf("?") != -1) {
            var str = url.substr(1);
            var key = str.split("=")[0];
            var value = str.split("=")[1];
            var request = {};
            request[key] = value;
        }
        return request;
    }

    var ID = GetRequest().uid;
    $.post('/apis/forecast', {uid: ID}, function(res) {
        console.log(res.weather_data);
        $.each(res.weather_data, function(index, data) {
            $("#day1").append(index);
            $("#day1").append("<br>");

            $.each(data, function(day, weather) {
                $("#day1").append(day + 1);
                $("#day1").append("</br>");

                $.each(weather, function(condition, result) {
                    $("#day1").append(condition);
                    $("#day1").append(":");
                    $("#day1").append(result);
                    $("#day1").append("</br>");

                $("#day1").append("</br>");
                });

            $("#day1").append("</br>");
            });

            $("#day1").append("</br>");
        });
    });

});
$(document).ready(function(){
    $("button").click(function() {
        var LOCATION = $("input").val();
        $.post('/apis/forecast', {"location": LOCATION}, function(res) {
            location.href = '/forecast_page?weather_data=' + res.weather_data;
        });
    });
});

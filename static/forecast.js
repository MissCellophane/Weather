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
        var days = ['今天', '明天', '后天']
        var city_count = -1;

        $.each(res.weather_data, function(city, data) {
            city_count += 1;

            var tab_str = "<table border='1' id=" + city +"></table>";
            var table = $(tab_str);
            table.appendTo($("#day1"));
            var cap_str = "<caption><b>" + city + "</b></caption>";
            var cap = $(cap_str);
            cap.appendTo(table);

            var tr = $("<tr></tr>");
            tr.appendTo(table);
            var head_str = $("<th>天气情况</th>");
            head_str.appendTo(tr);

            var rows = 1;
            var con_flag = {};
            $.each(data, function(day, weather) {
                var day_str = "<th>" + days[day] + "</th>";
                var heading = $(day_str);
                heading.appendTo(tr.eq(0));

                $.each(weather, function(condition, result) {
                    if (!(condition in con_flag)) {
                        con_flag[condition] = rows;
                        rows += 1;
                        var tr = $("<tr></tr>");
                        tr.appendTo(table);
                        var td_str = "<td>" + condition + "</td>";
                        var td = $(td_str);
                        td.appendTo(tr);
                    }

                    var td_str = "<td>" + result + "</td>";
                    var td = $(td_str);
                    var tr= $("<tr></tr>");
                    var tmp = con_flag[condition] + city_count * 20;
                    td.appendTo($($("tr").eq(con_flag[condition] + city_count * 20)));
                });


            });

        $("#day1").append("</br>");
        });

    });

});
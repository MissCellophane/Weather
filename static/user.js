$(document).ready(function(){
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

    request = GetRequest();

    var count = 0;
    $.post('/apis/forecast_setdefault', {uid: request['ID']}, function(res) {
        if (res.cities) {
            $.each(res.cities, function(index, data) {
                $("#inputbox").append('<input class="form-control"> <br>');
                $($(".form-control")[count]).val(data);
                count += 1;
            });
        }
    });

    if ($($(".form-control")[count]).val()=='') {
        $($(".form-control")[count]).remove();
    }

    $("#add").click(function() {
        $("#inputbox").append('<input class="form-control"> <br>');
    });


    $("#default").click(function() {
        var citys = [];
        $("input.form-control").each(function() {
            $(this).val() && citys.push($(this).val());
        });

        var post_city = JSON.stringify(citys);
        $.post('/apis/forecast_preference', {pref: post_city, uid: request['ID']}, function(res) {
            if (res.status) {
                alert("设置成功");
            }
            else {
                alert("设置失败：请检查城市名称");
            }
        });
    });


    $("#search").click(function() {
        location.href = '/forecast_page?uid=' + request['ID'];
    });

});

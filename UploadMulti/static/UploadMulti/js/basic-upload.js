$(function () {
    $(".js-upload-photos").click(function () {
        $("#fileupload").click();
    });

    $("#fileupload").fileupload({
        dataType: 'json',
        done: function (e, data) {
              if (data.result.is_valid) {
                var today = new Date();
                // var date = (today.getMonth()+1)+"/"+today.getDate()+"/"+today.getFullYear();
                var options = { year: 'numeric', month: 'short', day: 'numeric' ,hour:'numeric', minute: 'numeric', timezone: 'America/New_York'};
                
                $("#gallery tbody").prepend(
                    "<tr><td>" + data.result.name + "<br><strong>Uploaded Date: </strong>" + today.toLocaleDateString("en-US", options)+", " + "</td></tr>"
                )
            }
        }
    });
});

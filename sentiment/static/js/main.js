    $(document).ready(function() {
        function refreshImage()
        {
            $.ajax({url: "loadImage", success: function(result){
                $("#images").html(result);
            }});
        }
        $("#button1").click(function(){
            $("#images").html("Loading...");
          $.ajax({
              url: 'search_query',
              type: "POST",
              data: {
                query:$('#query').val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
              },

            success:function(result){
                setTimeout(refreshImage,1000)

                //alert('Hey!');
             },
            failure: function () {
                 alert("Something gone terribly wrong!");
             }
          })
        })
    })

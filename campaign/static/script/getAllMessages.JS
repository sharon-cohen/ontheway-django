$(document).ready(function(){
    $.getJSON("static/data/messages.Json", function(data) {
       $('#All').html(data.title);
       $('#messages').append("<ul>");
       $.each(data.messages, function() {
           $('#messages ul').append("<li><b>" + "message from " + this.sender + ":</b> <br>" + this.content + " <br> (Received on " + this.Date +  ")" +"</li>" +"<br>");
       });
    });
});
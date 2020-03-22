var fixed=0
var display_create = function(created){
    $("#viewcreated").empty()
    fixed=created[0]["id"]
    console.log(fixed)
    var newdiv="<div id='clikab'>Success! Click here to view your entry, or submit a new entry</div>"
    $("#viewcreated").append(newdiv)

  }




var save_create= function(id,name,portrait,death,reigns,reigne,descrip,rating,children){
  var data_to_create = { "id":id,"name":name, "portrait":portrait,"death":death, "reigns":reigns, "reigne":reigne, "descrip":descrip, "rating":rating, "children":children}
  $.ajax({
      type: "POST",
      url: "save_create",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(data_to_create),
      success: function(result){
        var currcreated = result["created"]
        created=currcreated
        display_create(created)
        $("#id").val('');
        $("#name").val('')
        $("#death").val('')
        $("#descrip").val('')
        $("#portrait").val('')
        $("#reigns").val('')
        $("#reigne").val('')
        $("#rating").val('')
        $("#children").val('')
        $( "#id" ).focus();
      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });
}
var searchsearch = function(searchedname){
  var data_to_search = {"searchedname": searchedname}
  $.ajax({
      type: "POST",
      url: "createsearchdata",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(data_to_search),
      success: function(result){
          var currsearched = result["searched"]
          searched=currsearched
      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });
}

$(document).ready(function(){


  $("#viewcreated").on('click',function(){
    window.location.href='http://127.0.0.1:5000/view/'+fixed+"";

  })



  $("#post").on('click',function(){
    document.getElementById("viewcreated").style.display = "none";
    if( isNaN($("#id").val() ) ){
      document.getElementById("warnid").style.display = "inline-block";
    }
    if( !isNaN($("#id").val() ) ){
      document.getElementById("warnid").style.display = "none";
    }
    if(  $("#id").val().length==0 ){
      document.getElementById("warnid2").style.display = "inline-block";
    }
    if(  $("#id").val().length>0 ){
      document.getElementById("warnid2").style.display = "none";
    }
    if(  $("#name").val().length==0 ){
      document.getElementById("warnname").style.display = "inline-block";
    }
    if(  $("#name").val().length>0 ){
      document.getElementById("warnname").style.display = "none";
    }
    if(  $("#portrait").val().length==0 ){
      document.getElementById("warnportrait").style.display = "inline-block";
    }
    if(  $("#portrait").val().length>0 ){
      document.getElementById("warnportrait").style.display = "none";
    }
    if(  $("#death").val().length==0 ){
      document.getElementById("warndeath").style.display = "inline-block";
    }
    if(  $("#death").val().length>0 ){
      document.getElementById("warndeath").style.display = "none";
    }
    if(  $("#descrip").val().length==0 ){
      document.getElementById("warndescrip").style.display = "inline-block";
    }
    if(  $("#descrip").val().length>0 ){
      document.getElementById("warndescrip").style.display = "none";
    }
    if( isNaN($("#reigns").val())||$("#reigns").val().length==0  ){
      document.getElementById("warnstart").style.display = "inline-block";
    }
    if( !isNaN($("#reigns").val())&&$("#reigns").val().length>0  ){
      document.getElementById("warnstart").style.display = "none";
    }
    if( isNaN($("#reigne").val() )||$("#reigne").val().length==0 ){
      document.getElementById("warnend").style.display = "inline-block";
    }
    if( !isNaN($("#reigne").val() )&&$("#reigne").val().length>0 ){
      document.getElementById("warnend").style.display = "none";
    }
    if( isNaN($("#rating").val() )||$("#rating").val().length==0 ){
      document.getElementById("warnrate").style.display = "inline-block";
    }
    if( !isNaN($("#rating").val() )&&$("#rating").val().length>0 ){
      document.getElementById("warnrate").style.display = "none";
    }


    if(!isNaN($("#id").val() )&& $("#id").val().length>0&& $("#name").val().length>0 && $("#portrait").val().length>0&& $("#death").val().length>0&&$("#descrip").val().length>0&&!isNaN($("#reigns").val() )&&!isNaN($("#reigne").val() )&&!isNaN($("#rating").val() )&& $("#reigne").val().length>0&& $("#reigns").val().length>0&& $("#rating").val().length>0 ){
      document.getElementById("viewcreated").style.display = "inline-block";
      save_create($("#id").val(),$("#name").val(),$("#portrait").val(),$("#death").val(), $("#reigns").val(), $("#reigne").val(), $("#descrip").val(), $("#rating").val(),$("#children").val())

    }

  })

  $("#Search").keypress(function(event) {
      if (event.keyCode === 13) {
          event.preventDefault();
          $("#searchbut").click();
      }
  });


  $("#searchbut").on('click',function(){
      var searchterm=$("#Search").val()
      searchsearch(searchterm)
      window.location.href='http://127.0.0.1:5000/search/'+searchterm+"";

  })





})

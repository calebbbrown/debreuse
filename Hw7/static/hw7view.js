var display_view = function(viewed){

    $.each(viewed, function(index, value){
      var fixed = value["id"]
      var twofixed=value["name"]
      var twofivefixed=value["portrait"]
      var threefixed=value["death"]
      var fourfixed=value["reignstart"]
      var fivefixed=value["reignend"]
      var sixfixed=value["summary"]
      var sevenfixed=value["rating"]
      var eightfixed=value["children"]

      var newdiv="<div class='row'><div class='col-md-3'><b><u>Name:</b></u> "+twofixed+"</div></div>"
      var sudiv="<div class='row'><div class='col-md-3'><b><u>Portrait Link:</b></u> "+twofivefixed+"</div></div>"
      var twodiv="<div class='row' id=descriprow><div><b><u>Cause of Death:</b></u> "+threefixed+"&nbsp&nbsp&nbsp&nbsp<button class='editor' id='descripbut'>Edit Cause of Death</button></div></div>"
      var threediv="<div class='row'><div class='col-md-3'><b><u> Reign Start:</b></u> "+fourfixed+"</div><div id='clikab' class='col-md-5'><b><u>Reign End:</b></u> "+fivefixed+"</div></div>"
      var fourdiv="<div class='row'><div style='width:700px'><b><u>Description:</b></u> "+sixfixed+"</div></div>"
      var fivediv="<div class='row' id='ratingrow'><div ><b><u>Rating:</b></u> "+sevenfixed+"&nbsp&nbsp&nbsp&nbsp<button class='editor' id='ratebut'>Edit Rating</button></div></div>"

      if (eightfixed != undefined &&eightfixed.length != 0){

        for (i = 0; i < eightfixed.length; i++) {
          if(eightfixed[i][0]!="z"){
            $("#viewframe6").append("<div>"+eightfixed[i]+"<button class='delbut' id=del"+i+">Delete</button></div>")
          }
          if(eightfixed[i][0]=="z"){
            $("#viewframe6").append("<div><button class='undbut' id=und"+i+">Undo Delete</button></div>")
          }
        }
      }

      $("#viewframe1").append(newdiv)
      $("#viewframe4insert").append(twodiv)
      $("#viewframe3").append(threediv)
      $("#viewframe25").append(sudiv)
      $("#viewframe4").append(fourdiv)
      $("#viewframe5insert").append(fivediv)
      $("#editdescrip").attr("value", threefixed)
      $("#editrate").attr("value", sevenfixed)
    })
  }

  var update_recent= function(name){
    var data_to_update = {"name":name}
    $.ajax({
        type: "POST",
        url: "/update_recent",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_update),
        success: function(result){
          console.log("cool")
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
  }


  var save_descrip_edit= function(name, death){
    var data_to_edit = {"name":name, "death":death}
    $.ajax({
        type: "POST",
        url: "/save_descrip_edit",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_edit),
        success: function(result){
          var currviewed = result["currviewed"]
          viewed=currviewed
          window.location.href='http://127.0.0.1:5000/view/'+viewed[0]["id"]+"";

        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
  }

  var save_rating_edit= function(name, rating){
    var data_to_edit2 = {"name":name, "rating":rating}
    $.ajax({
        type: "POST",
        url: "/save_rating_edit",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_edit2),
        success: function(result){
          var currviewed = result["currviewed"]
          viewed=currviewed
          window.location.href='http://127.0.0.1:5000/view/'+viewed[0]["id"]+"";

        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
  }

  var save_edit_child= function(name, childpos){
    var data_to_edit3 = {"name":name, "childpos":childpos}
    $.ajax({
        type: "POST",
        url: "/save_edit_child",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_edit3),
        success: function(result){
          var currviewed = result["currviewed"]
          viewed=currviewed

          window.location.href='http://127.0.0.1:5000/view/'+viewed[0]["id"]+"";


        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
  }

  var undo_edit_child= function(name, childpos){
    var data_to_edit4 = {"name":name, "childpos":childpos}
    $.ajax({
        type: "POST",
        url: "/undo_edit_child",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_edit4),
        success: function(result){
          var currviewed = result["currviewed"]
          viewed=currviewed

          window.location.href='http://127.0.0.1:5000/view/'+viewed[0]["id"]+"";


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
        url: "viewsearchdata",
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

    display_view(viewed)
    update_recent(viewed[0]["name"])
    $("#descripbut").on('click',function(){
            document.getElementById("edit1").style.display = "inline-block";
            document.getElementById("descriprow").style.display = "none";
            $( "#editdescrip" ).focus();

    })
    $("#resetbut1").on('click',function(){
            document.getElementById("edit1").style.display = "none";
            document.getElementById("descriprow").style.display = "inline-block";


    })
    $("#submitbut1").on('click',function(){
            save_descrip_edit(viewed[0]["name"], $( "#editdescrip" ).val())

    })



    $("#ratebut").on('click',function(){
            document.getElementById("edit2").style.display = "inline-block";
            document.getElementById("ratingrow").style.display = "none";
            $( "#editrate" ).focus();

    })
    $("#resetbut2").on('click',function(){
            document.getElementById("edit2").style.display = "none";
            document.getElementById("ratingrow").style.display = "inline-block";

    })
    $("#submitbut2").on('click',function(){
            save_rating_edit(viewed[0]["name"], $( "#editrate" ).val())


    })

    $(".delbut").on('click',function(){

            var look=$(this).attr("id")
            console.log( "del", look[3])

            save_edit_child(viewed[0]["name"],look[3])

    })

    $(".undbut").on('click',function(){

            var look=$(this).attr("id")
            console.log("un", look[3])
            undo_edit_child(viewed[0]["name"],look[3])

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

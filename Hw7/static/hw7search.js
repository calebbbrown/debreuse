var display_searches = function(searched, theterm){
    $("#num").html("Number of results: "+searched.length+"")
    term=theterm[0]["term"]
    $("#results").empty()
    $.each(searched, function(index, value){
      var place=value["place"]
      var name = value["name"]
      var orig=name
      var death=value["death"]
      var which=value["which"]
      if(which==="aname"){
        console.log(place, term.length)
        if(place==-1&&term.length==1){

          name=name.replace(name[0], '<b><u>'+name[0]+'</u></b>')
        }
        if(place==-1&&term.length>1){
          name=name.replace(name[0], '<b><u>'+name[0]+'</u></b>')
          name=name.replace(term.substring(1), '<b><u>'+term.substring(1)+'</u></b>')
        }
        else{
          name=name.replace(term, '<b><u>'+term+'</u></b>')
        }
      }
      if(which==="death"){
        if(place==-1&&term.length==1){
          death=death.replace(death[0], '<b><u>'+death[0]+'</u></b>')
        }
        if(place==-1&&term.length>1){
          death=death.replace(death[0], '<b><u>'+death[0]+'</u></b>')
          death=death.replace(term.substring(1), '<b><u>'+term.substring(1)+'</u></b>')
        }
        else{
          death=death.replace(term, '<b><u>'+term+'</u></b>')
        }
      }

      var newdiv="<div class='row resulty' id="+orig+"><div class='col-md-8'>Name: "+name+" </br>Cause of Death: "+death+"</div></div>"
      $("#results").prepend(newdiv)

    });
  }

  var searchsearch = function(searchedname){
    var data_to_search = {"searchedname": searchedname}
    $.ajax({
        type: "POST",
        url: "searchsearchdata",
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

  var viewsearch = function(viewid){
    var data_to_view = {"viewid": viewid}
    $.ajax({
        type: "POST",
        url: "viewsearch",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_view),
        success: function(result){
            var currviewed = result["currviewed"]
            viewed=currviewed
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
    display_searches(searched, theterm)

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

    $(".resulty").on('click',function(){
        var dest=$(this).attr("id")
        var actdest=0
        for(i=0;i<Emperors.length;i++){
          if(Emperors[i]["name"]==dest){
            actdest=Emperors[i]["id"]
          }
        }
        console.log(dest)
        viewsearch(actdest)
        window.location.href='http://127.0.0.1:5000/view/'+actdest+"";

    })
  })

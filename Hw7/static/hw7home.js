var display_cards = function(){
    console.log("again")
    $("#card1").empty()
    $("#card2").empty()
    $("#card3").empty()
    $("#card4").empty()
    $("#card5").empty()
    $("#card6").empty()
    $("#card7").empty()
    $("#card8").empty()
    $("#card9").empty()
    $("#card10").empty()
    var count=1
    $.each(recentsearches, function(index, value){
        console.log("again")
        var fixed = value["id"]
        var cardlink=value["portrait"]
        var cardalt=value["name"]
        var cardtitle=value["name"]
        var newdiv="<img class='card-img-top' src="+cardlink+" alt="+cardalt+"><div class='card-body'><h4 class='card-title'>"+cardtitle+"</h4></div>"
        $("#card"+count).prepend(newdiv)
        count+=1

    })
  }


  var searchsearch = function(searchedname){
    var data_to_search = {"searchedname": searchedname}
    $.ajax({
        type: "POST",
        url: "searchdata",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_search),
        success: function(result){
            var currsearched = result["currsearched"]
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

  var viewview = function(viewid){
    var data_to_view = {"viewid": viewid}
    $.ajax({
        type: "POST",
        url: "viewview",
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
    display_cards(recentsearches)

    $("#Search").keypress(function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            $("#searchbut").click();
        }
    });


    $("#searchbut").on('click',function(){
        var searchterm=$("#Search").val()
        searchsearch(searchterm)
        console.log(searchterm)
        window.location.href='http://127.0.0.1:5000/search/'+searchterm+"";

    })

    $(".card").on('click',function(){
        var cardid=$(this).attr('id')
        var cardnum=parseInt(cardid.substring(4))
        var viewid=recentsearches[cardnum-1]["id"]
        console.log(viewid)
        viewview(viewid)

        window.location.href='http://127.0.0.1:5000/view/'+viewid+"";

    })




  })

function displayList() {
  $.get('/show?_=' + new Date().getTime(), function() {
  })
    .done(function (data) {
        update_list(data);
    })
    .always(function () {
        setTimeout(displayList, 360000);
    });
}

$(document).ready(function () {
    displayList();
})

function update_list(data) {
    var data = JSON.parse(JSON.parse(data));
    jdata = data["data"];
    $("#stockList").html("");
    var projectClass = 0;
    for(var key in jdata){
      if(projectClass == 5){ projectClass = 0;}
      var card = '<div class="col-md-3"><div class="project project-'+ projectClass +'"><div class="shape"><div class="shape-text">'+
                  jdata[key]["symbol"] + '</div></div><div class="project-content"><h3 class="lead">' +
                  jdata[key]["symbol"] + '</h3><ul style="list-style-type:lower-greek"><li><b>Open Price:</b> '+ jdata[key]["openPrice"] +'</li><li><b>High Price:</b> '+
                  jdata[key]["highPrice"]+'</li><li><b>Low Price:</b> '+ jdata[key]["lowPrice"] +'</li><li><b>Traded Quantity:</b> '+
                  jdata[key]["tradedQuantity"]+'</li><li><b>LTP:</b> '+ jdata[key]["ltp"] +'</li><li><b>Previous Price:</b> '+
                  jdata[key]["previousPrice"] + '</li><li><b>Net Price:</b> '+ jdata[key]["netPrice"]+'</li><li><b>Turnover(In lakhs):</b> '+
                  jdata[key]["turnoverInLakhs"]+ '</li><li><b>Last Corp Announcement Date:</b> '+ jdata[key]["lastCorpAnnouncementDate"]+
                  '</li><li><b>Last Corp Announcement:</b> '+ jdata[key]["lastCorpAnnouncement"]+'</li></ul></div></div></div>';

      $("#stockList").append(card);
      // var symbol = jdata[key]["symbol"];
      // var companyDetails = getCompanyDetails(symbol);
      projectClass += 1;
    }
    $("#time").html(data["time"]);
}

// function getCompanyDetails(symbol){
//   var delay = 2000;
//   $.ajax({
//       url: "/logo?_="+ new Date().getTime(),
//       data: {
//           "symbol": symbol
//       },
//       success: function(data) {
//         setTimeout(function() {
//           delaySuccess(data);
//         }, delay);
//       }
//   });
// }
//
// function delaySuccess(data) {
//   return data;
//   // console.log(Object.keys(data));
// }

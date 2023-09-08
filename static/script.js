window.setInterval('refresh()', 25 * 1000); 	// Calls function every 25sec
// Refresh or reload page.
function refresh() {
    window .location.reload();
}
var timeleft = 25;
var downloadTimer = setInterval(function(){ 
if(timeleft <= 0){
  clearInterval(downloadTimer);
  document.getElementById("countdown").innerHTML = "0";
} else {
  document.getElementById("countdown").innerHTML = timeleft;
}
timeleft -= 1;
}, 1000);
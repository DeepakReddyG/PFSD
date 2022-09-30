var lClicks = 0;
var dClicks = 0;

$(".likes").on("click", function(){
	lClicks += 1;
    document.getElementById("l-counter").innerHTML = lClicks;
})

$(".dislikes").on("click", function(){
	dClicks += 1;
    document.getElementById("d-counter").innerHTML = dClicks;
})
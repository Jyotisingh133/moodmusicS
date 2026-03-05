function detectMood(){

fetch('/detect')

.then(response => response.json())

.then(data => {

document.getElementById("emotion").innerHTML =
"Detected Mood: " + data.emotion;

document.getElementById("player").src =
data.song.link;

});

}
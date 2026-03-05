const video = document.getElementById("video");

navigator.mediaDevices.getUserMedia({video:true})

.then(function(stream){

video.srcObject = stream;

})

.catch(function(error){

console.log("Camera Error",error);

});
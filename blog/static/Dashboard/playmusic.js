//addeeventlistener to play music when user click the button
//using scope function to rewrite its method
//function playMusic(){
//    function createResource(){
//      var audio1 = document.createElement('audio');
//    var txt1 = document.querySelector('#btn1');
//  audio1.src = 'https://mdn.mozillademos.org/files/2587/AudioTest%20(1).ogg';
//if (txt1.textContent == 'Play'){
//  audio1.play();
//txt1.textContent = 'Stop';
//}else{
//txt1.textContent = 'Play';
//audio1.pause();}
//}
//   return createResource;
//}
//add event when user click play button

var btn = document.querySelector('.btn');
btn.addEventListener('click',updateButon);

function updateButon() {
    var audio = document.createElement('audio');
    audio.src = 'https://mdn.mozillademos.org/files/2587/AudioTest%20(1).ogg';
    audio.play();
    }







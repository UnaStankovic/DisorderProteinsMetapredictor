// Browse button
var fileinput = document.getElementById("browse");
function HandleBrowseClick()
{
    var fileinput = document.getElementById("browse");
    fileinput.click();
}
function Handlechange()
{
    
    var textinput = document.getElementById("filename");
    textinput.textContent = fileinput.value;
}

var submit = document.getElementById('submit')
submit.addEventListener("click", generate_data)

// packing what is supposed to be sent when clicked on submit
function generate_data(){
    var disprot_id = document.getElementById('disprot_id').value 
    AA_sequence = document.getElementById('sequence').value
    if(AA_sequence != ""){
        sequence = AA_sequence
    }else{
        sequence = ""
    }

    var json = {sequence: sequence, disprot_id: disprot_id, filename: fileinput.value}
    console.log(json)

    return json
}

//const io = require('socket.io-client')

const socket = io('http://localhost:5000')

socket.on('message', data => {
    console.log('Got from server: ');
    console.log(data);
  });

  function send_data() {
    const json = generate_data();
    console.log('Sending to server:');
    console.log(json);
  
    socket.emit('message', json);
  }

  
socket.on('connect', () => {
    console.log('Connected to server');
    loop();
  });

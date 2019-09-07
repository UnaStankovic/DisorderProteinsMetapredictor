const txtSequence = document.getElementById('sequence');
const txtDisprotId = document.getElementById('disprot_id');

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

fileinput.addEventListener('change', function() {
    fReader = new FileReader();
    fReader.readAsText(this.files[0]);
    fReader.onloadend = function(event){
        txtSequence.value = event.target.result;
    }
})

var submit = document.getElementById('submit')
submit.addEventListener("click", send_data)

// packing what is supposed to be sent when clicked on submit
function generate_data(){
    var AA_sequence = txtSequence.value;

    if(AA_sequence != ""){
        sequence = AA_sequence
    }else{
        sequence = ""
    }
    var disprot_id = txtDisprotId.value 
    var json = {sequence: sequence, disprot_id: disprot_id}
    //console.log(json)
    return json
}

//const io = require('socket.io-client')

const socket = io('http://localhost:5000')

socket.on('message', data => {
    console.log('Got from server: ');
    console.log(data);
  });

socket.on('disprotinfo', data => {
    console.log('Got from server: ');
    console.log(data);
  });

socket.on('predicted', data => {
    console.log('Got from server: ');
    console.log(data);
    for (const pred of data) {
        create_predictor(pred.result, pred.name);
    }
    hide_loader()
});


socket.on('iupred2_predict', data => {
    console.log('Got from server: ');
    console.log(data);
    create_predictor(data, "IUPRED2")
  });

socket.on('spotd_predict', data => {
    console.log('Got from server: ');
    console.log(data);
    create_predictor(data, "SPOTD")
});
socket.on('pondr_predict', data => {
    console.log('Got from server: ');
    console.log(data);
    create_predictor(data, "PONDR");
});
/*
socket.on('espritz_predict', data => {
    console.log('Got from server: ');
    console.log(data);
    create_predictor(data, "ESPRITZ")
});
socket.on('cspritz_predict', data => {
    console.log('Got from server: ');
    console.log(data);
    create_predictor(data, "CSPRITZ")
});
*/
function send_data() {
    const json = generate_data();
    console.log('Sending to server:');
    //console.log(json);
    socket.emit('message', json);
}

  
socket.on('connect', () => {
    console.log('Connected to server');
  });

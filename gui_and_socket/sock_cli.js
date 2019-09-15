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
submit.addEventListener("click", sendData)

// packing what is supposed to be sent when clicked on submit
function generateData(){
    var AASequence = txtSequence.value;

    if(AASequence != ""){
        sequence = AASequence
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
    console.log('Got from server.');
    console.log(data);

  });

socket.on('predicted', data => {
    console.log('Got from server.');
    console.log(data);
    createScale(data.sequence);
    for (const pred of data.predictors) {
        createPredictor(pred.result, pred.name);
    }
    hideLoader(); 
    createConsensus(data.consensus.result);
    addMetrics(data.metrics);
    addDetailedMetrics(data.partial_metrics);
});


function sendData() {
    //txtSequence.value == "" ||
    if (txtDisprotId.value == ""){
        alert("You must enter the DisProt id!");
    }
    else{
        showLoader()
        const json = generateData();
        console.log('Sending to server.');
        socket.emit('message', json);
    }
}

  
socket.on('connect', () => {
    console.log('Connected to server');
});


  /*
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
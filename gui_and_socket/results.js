let resultsDiv = document.getElementById('results_div');

function createScale(sequence) {
    const scaleWrap = document.createElement('div');
    scaleWrap.classList.add('scale-wrap');

    const predictorWrap = document.createElement('div');
    predictorWrap.classList.add('predictor-wrap');

    for(let i=0; i < sequence.length; i++){

        const scaleEl = document.createElement('span');
        const scaleElWrap = document.createElement('span');

        const aaSymbol = document.createElement('span');
        const aaWrap = document.createElement('span');

        aaSymbol.classList.add('aa');
        aaSymbol.classList.add('sequence');
        aaWrap.classList.add('aa-wrap');
        aaSymbol.innerText = sequence[i];

        scaleElWrap.classList.add('scale-el-wrap');
        scaleEl.classList.add('scale-el');
        scaleEl.innerHTML = i+1;

        scaleElWrap.appendChild(scaleEl);
        scaleWrap.appendChild(scaleElWrap);

        aaWrap.appendChild(aaSymbol);
        predictorWrap.appendChild(aaWrap);

    }

    scaleWrap.style.width = `${sequence.length * 30 + 110}px`;
    resultsDiv.appendChild(scaleWrap);
    const predList = document.querySelector('.predictors-list');
    const predictorLabel = document.createElement('div');
    predictorLabel.classList.add('predictor-label');
    predictorLabel.innerHTML = 'Sequence'
    predList.appendChild(predictorLabel);

    predictorWrap.style.width = `${sequence.length * 30 + 110}px`;
    resultsDiv.appendChild(predictorWrap);
}

function createPredictor(sequence, predName){
    let name = document.createElement('h2');
    let pom = 0;
    
    const predictorWrap = document.createElement('div');
    predictorWrap.classList.add('predictor-wrap');
    
    for(let i=0; i < sequence.length; i++){

        const aaSymbol = document.createElement('span');
        const aaWrap = document.createElement('span');

        aaSymbol.classList.add('aa');
        aaWrap.classList.add('aa-wrap');
        aaSymbol.innerText = sequence[i];

        if (sequence[i] === 'D') {
            aaSymbol.classList.add('disordered');
        } else {
            aaSymbol.classList.add('ordered');
        }

        aaWrap.appendChild(aaSymbol);
        predictorWrap.appendChild(aaWrap);

    }

    const predList = document.querySelector('.predictors-list');
    const predictorLabel = document.createElement('div');
    predictorLabel.classList.add('predictor-label');
    predictorLabel.innerHTML = predName // Predictor Name
    predList.appendChild(predictorLabel);

    predictorWrap.style.width = `${sequence.length * 30 + 110}px`;
    resultsDiv.appendChild(predictorWrap);
}

function createConsensus(cons){
    let name = document.createElement('h2');
    let pom = 0;

    const predictorWrap = document.createElement('div');
    predictorWrap.classList.add('predictor-wrap');
    
    for(let i=0; i < cons.length; i++){

        const aaSymbol = document.createElement('span');
        const aaWrap = document.createElement('span');
        const aaText = document.createElement('span');

        aaSymbol.classList.add('aa');
        aaText.classList.add('aa-consensus');
        aaWrap.classList.add('aa-wrap');
        aaWrap.classList.add('consensus-wrap');
        aaText.innerText = cons[i];

        aaSymbol.classList.add('consensus-h');
        aaSymbol.style.height = (cons[i] * 100) + "%";
    
        aaWrap.appendChild(aaSymbol);
        aaWrap.appendChild(aaText);
        predictorWrap.appendChild(aaWrap);

    }

    const predList = document.querySelector('.predictors-list');
    const predictorLabel = document.createElement('div');
    predictorLabel.classList.add('predictor-label');
    predictorLabel.innerHTML = "Consensus" 
    predList.appendChild(predictorLabel);
    predictorWrap.style.width = `${cons.length * 30 + 110}px`;
    resultsDiv.appendChild(predictorWrap);   
}

function addMetrics(metrics){
    const wrap = document.createElement('div');
    wrap.id = "metrics";
    heading = document.createElement('h2');
    heading.innerHTML = "Metrics";
    wrap.appendChild(heading);
    for(i = 0; i < metrics.length; i++){
        p = document.createElement('p');
        p.innerHTML = metrics[i].name + ' : ' + metrics[i].result;
        //console.log(metrics[i]);
        wrap.appendChild(p);
    }
    resultsDiv.appendChild(wrap);
    addConsensusImage();
}

function addConsensusImage(){
    const wrap = document.createElement('div');
    wrap.id = "imageDiv";
    const img = document.createElement('img');
    img.alt = "consensus";
    img.src = 'predicted.png';
    img.style.marginTop = "20px";
    wrap.appendChild(img);
    resultsDiv.appendChild(wrap);
   
}

function addDetailedMetrics(partialMetrics){
    const wrap = document.createElement('div');
    wrap.id = "detailed-metrics";
    heading = document.createElement('h2');
    heading.innerHTML = "Detailed metrics";
    wrap.appendChild(heading);
    metricsTable = document.createElement('table');

    // Adding first row
    var tr = document.createElement('tr');
    metrics = ["Number of predictors/Metrics", "Accuracy", "Precision", "Recall", "F1"];
    for (m in metrics){
        var th = document.createElement('th');
        th.innerHTML = metrics[m];
        tr.appendChild(th);
    }
    metricsTable.appendChild(tr);

    // Adding data 
    for(i in partialMetrics){
        var tr = document.createElement('tr');
        var td = document.createElement('td');
        td.innerHTML = i;
        tr.appendChild(td);
        for(j=0; j < 4; j++){
            var td = document.createElement('td');
            td.innerHTML = partialMetrics[i][j];
            tr.appendChild(td);
        }
        metricsTable.appendChild(tr);
    }
    wrap.appendChild(metricsTable)
    resultsDiv.appendChild(wrap);
    addReloadButton();
}

function addReloadButton(){
    const wrap = document.createElement('div');
    wrap.id = "reloadDiv";
    const btn = document.createElement('div');
    btn.id = "reload";
    btn.classList = 'button';
    btn.innerHTML = "Run another analysis";
    btn.addEventListener("click", clearResults);
    wrap.appendChild(btn);
    resultsDiv.appendChild(wrap);
}

function clearResults(){
    window.location.reload(false); 
}
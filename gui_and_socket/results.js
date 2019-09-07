let results_div = document.getElementById('results_div');



let predictors = ["iupred2", "pondr", "spotd", "espritz", "cspritz"]
let sequence = "MSEPKAIDPKLSTTDRVVKAVPFPPSHRLTAKEVFDNDGKPRVDILKAHLMKEGRLEESV\
ALRIITEGASILRQEKNLLDIDAPVTVCGDIHGQFFDLMKLFEVGGSPANTRYLFLGDYV\
DRGYFSIECVLYLWALKILYPKTLFLLRGNHECRHLTEYFTFKQECKIKYSERVYDACMD\
AFDCLPLAALMNQQFLCVHGGLSPEINTLDDIRKLDRFKEPPAYGPMCDILWSDPLEDFG\
NEKTQEHFTHNTVRGCSYFYSYPAVCEFLQHNNLLSILRAHEAQDAGYRMYRKSQTTGFP\
SLITIFSAPNYLDVYNNKAAVLKYENNVMNIRQFNCSPHPYWLPNFMDVFTWSLPFVGEK\
VTEMLVNVLNICSDDELGSEEDGFDGATAAARKEVIRNKIRAIGKMARVFSVLREESESV\
LTLKGLTPTGMLPSGVLSGGKQTLQSATVEAIEADEAIKGFSPQHKITSFEEAKGLDRIN\
ERMPPRRDAMPSDANLNSINKALTSETNGTDSNGSNSSNIQ"
console.log(sequence.length)

// create_predictor(sequence, 'Sequence');
//create_predictor(sequence, 'IUPRED2');
//create_predictor(sequence, 'IUPRED2');

function create_scale(sequence) {
    const scaleWrap = document.createElement('div');
    scaleWrap.classList.add('scale-wrap');

    const predictorWrap = document.createElement('div');
    predictorWrap.classList.add('predictor-wrap');

    for(let i=0; i < sequence.length; i++){

        const scale_el = document.createElement('span');
        const scale_el_wrap = document.createElement('span');

        const aa_symbol = document.createElement('span');
        const aa_wrap = document.createElement('span');

        aa_symbol.classList.add('aa');
        aa_symbol.classList.add('sequence');
        aa_wrap.classList.add('aa-wrap');
        aa_symbol.innerText = sequence[i];

        scale_el_wrap.classList.add('scale-el-wrap');
        scale_el.classList.add('scale-el');
        scale_el.innerHTML = i;

        scale_el_wrap.appendChild(scale_el);
        scaleWrap.appendChild(scale_el_wrap);

        aa_wrap.appendChild(aa_symbol);
        predictorWrap.appendChild(aa_wrap);

    }

    scaleWrap.style.width = `${sequence.length * 30 + 110}px`;
    results_div.appendChild(scaleWrap);
    const predList = document.querySelector('.predictors-list');
    const predictorLabel = document.createElement('div');
    predictorLabel.classList.add('predictor-label');
    predictorLabel.innerHTML = 'Sequence'
    predList.appendChild(predictorLabel);

    predictorWrap.style.width = `${sequence.length * 30 + 110}px`;
    results_div.appendChild(predictorWrap);
}

function create_predictor(sequence, pred_name){
    let name = document.createElement('h2');
    let pom = 0;

    const predictorWrap = document.createElement('div');
    predictorWrap.classList.add('predictor-wrap');
    
    console.log(sequence.length)
    for(let i=0; i < sequence.length; i++){

        const aa_symbol = document.createElement('span');
        const aa_wrap = document.createElement('span');

        aa_symbol.classList.add('aa');
        aa_wrap.classList.add('aa-wrap');
        aa_symbol.innerText = sequence[i];

        if (sequence[i] === 'D') {
            aa_symbol.classList.add('disordered');
        } else {
            aa_symbol.classList.add('ordered');
        }

        aa_wrap.appendChild(aa_symbol);
        predictorWrap.appendChild(aa_wrap);

    }

    const predList = document.querySelector('.predictors-list');
    const predictorLabel = document.createElement('div');
    predictorLabel.classList.add('predictor-label');
    predictorLabel.innerHTML = pred_name // Predictor Name
    predList.appendChild(predictorLabel);

    predictorWrap.style.width = `${sequence.length * 30 + 110}px`;
    results_div.appendChild(predictorWrap);
}
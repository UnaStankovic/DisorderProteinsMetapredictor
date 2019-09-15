import eventlet
import socketio
import json
#from predictors.predictor import Predictor
import disprot_service 
import predictor_service 
import threading
from consensus import consensus, plot_consensus, consensus_treshold
from measures import measure_all, binarize_values
from disprot_service import shortened_sequence 

sio = socketio.Server(cors_allowed_origins=['http://localhost:9004'])
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

def prediction_calls(data):
    id_disp = data["disprot_id"]
    s = data["sequence"]
    # DisProt database call
    [disprot, seq] = disprot_service.get_sequence_info(id_disp)
    print(seq, len(seq))
    if (s == ""):
        s = seq

    # Storing the sequence in a file in order to locally use the predictors
    f = open("sequence.txt", "w")
    f.write(s)
    f.close()

    # Calling predictors
    iupred2 = predictor_service.iupred2_predict(s)
    #SPOTD: uncomment the function call 
    #spotd = predictor_service.spotd_predict(s) 
    pondr = predictor_service.pondr_predict(s)
    ss = shortened_sequence(s)
    [loops, hotloops, rem465] = predictor_service.disembl_predict(ss)

    #SPOTD: add spotd to the call
    predictors_all = [iupred2, pondr, loops, hotloops, rem465]
    cons = consensus(ss, predictors_all)
    bin_disprot = binarize_values(disprot)
    m = measure_all(consensus_treshold(cons), bin_disprot)

    # Doing consensus and metrics for when one, two or more predictors said "D"
    consensus_values = {}
    for i in range(1,len(predictors_all)+1):
        cons_tres = consensus_treshold(cons,1/len(predictors_all)*i)
        consensus_values[i] = measure_all(cons_tres, bin_disprot)      

    #SPOTD : add spotd to the predictors list
    result = {
                "predictors": [
                {
                    'name': 'IUPRED2',
                    'result': iupred2
                },
                {
                    'name': 'PONDR',
                    'result': pondr 
                }, 
                {
                    'name': 'LOOPS',
                    'result': loops 
                },
                {
                    'name': 'HOTLOOPS',
                    'result': hotloops 
                },
                {
                    'name': 'REM465',
                    'result': rem465 
                },
                {
                    'name': 'DisProt',
                    'result': disprot 
                }
                ],
                "consensus": {
                    'name': 'cons',
                    'result': cons
                },
                "sequence": ss,
                "metrics" : [
                    {
                        'name': 'Accuracy',
                        'result' : m[0]
                    },
                    {
                        'name': 'Precision',
                        'result': m[1] 
                    },
                    {
                        'name': 'Recall',
                        'result': m[2] 
                    },
                    {
                        'name': 'F1 score',
                        'result': m[3] 
                    }
                ],
                "partial_metrics": consensus_values
            }
    
    sio.emit('predicted', result)


@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.on("message")
def message(sid, data):
    print('message ', data)
    
    # Calling all the predictors to give their opinion on the sequence in the same thread!
    x = threading.Thread(target=prediction_calls(data), args=(data))
    x.start()
    
    #
    #sio.emit('spotd_result', spotd)
    
    #sio.emit('pondr_predict', pondr)
    """
    cspritz = predictor_service.cspritz_predict(s)
    sio.emit('cspritz_result', cspritz)
    espritz = predictor_service.espritz_predict(s)
    sio.emit('espritz_result', espritz)
    """

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
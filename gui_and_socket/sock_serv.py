import eventlet
import socketio
import json
#from predictors.predictor import Predictor
import disprot_service 
import predictor_service 

sio = socketio.Server(cors_allowed_origins=['http://localhost:9004'])
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.on("message")
def message(sid, data):
    print('message ', data)
    if (data["disprot_id"] != ""):
        response = disprot_service.get_sequence_info(data["disprot_id"])
        if(response):
                sio.emit("disprotinfo", response)

    #print(data["sequence"])
    s = data["sequence"]
    # Storing the sequence in a file in order to locally use the predictors
    f = open("sequence.txt", "w")
    f.write(s)
    f.close()

    # Calling all the predictors to give their opinion on the sequence
    iupred2 = predictor_service.iupred2_predict(s)
    #spotd = predictor_service.spotd_predict(s)
    pondr = predictor_service.pondr_predict(s)
    result = [{
            'name': 'iupred2',
            'result': iupred2
        },
        {
            'name': 'pondr',
            'result': pondr 
        }]
    sio.emit('predicted', result)
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

#@sio.event
#def message(sid, disprot):
#        pass

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
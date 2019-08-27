import socketio

sio = socketio.Server()

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

app = socketio.WSGIApp(sio, app)

if __name__ == "__main__":
    app.run()
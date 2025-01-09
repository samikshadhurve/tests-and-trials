from flask import Flask, Response
import cv2
import numpy as np

app = Flask(__name__)


camera1 = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(1)
camera3 = cv2.VideoCapture(2)

def generate_frames():
    while True:

        success1, frame1 = camera1.read()
        success2, frame2 = camera2.read()
        success3, frame3 = camera3.read()


        if not success1 or not success2 or not success3:
            break


        frame1 = cv2.resize(frame1, (640, 480))
        frame2 = cv2.resize(frame2, (640, 480))
        frame3 = cv2.resize(frame3, (640, 480))


        combined_frame = np.hstack((frame1, frame2, frame3))


        ret, buffer = cv2.imencode('.jpg', combined_frame)
        combined_frame = buffer.tobytes()


        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + combined_frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return "<h1>Live Video Stream</h1><img src='/video_feed' />"

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)


from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    str = "Hello World! HyunJungKim"
    return str
    
import cv2 as cv
if __name__ == '__main__':
    # /dev/video0 
    cap = cv.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('webcam', frame)
        cv.waitKey(1)
        pass

    app.run(host='0.0.0.0', port='8000') 
        
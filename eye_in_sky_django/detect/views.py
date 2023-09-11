from django.shortcuts import render
import os, signal
from django.urls import reverse

# Create your views here.
def call(request):
    if(request.method=="POST"):
        from ultralytics import YOLO
        from ultralytics.yolo.v8.detect.predict import DetectionPredictor
        import cv2

        model = YOLO("D:/Languages/Web/Practice/eye-in-sky/eye_in_sky_django/final.pt") #if not working try giving the absolute path od the best_final.pt file
        model.predict(source="0", show=True, conf=0.5)
        

        return 'Object detection completed!'
    else:
        return render(request,"detect/home.html")
    
def stop(request):
    if(request.method=="POST"):
        os.kill(os.getpid(), signal.SIGINT)
        print("Serve shutting down..")
        return render(request, "{% url 'home' %}")
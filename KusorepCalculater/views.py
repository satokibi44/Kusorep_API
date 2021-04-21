from rest_framework import viewsets, filters
from django.http import HttpResponse, JsonResponse
from .Bert.PredictTaskExecutor import PredictTaskExecutor

# Create your views here.
def kusorep_score_viewset(request):
    if(request.method == "GET"):
        msg = request.GET["msg"]
        predictTaskExecutor = PredictTaskExecutor()
        label = predictTaskExecutor.main(sentence)
        kusoripu_score = label[1]
        return HttpResponse("Hello, Nginx."+msg)
    else:
        return HttpResponse("Hello, Nginx.")


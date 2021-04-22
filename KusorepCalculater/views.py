from rest_framework import viewsets, filters
from django.http import HttpResponse, JsonResponse
from .Bert.PredictTaskExecutor import PredictTaskExecutor

# Create your views here.
def kusorep_score_viewset(request):
    if(request.method == "GET"):
        msg = request.GET["msg"]
        predictTaskExecutor = PredictTaskExecutor()
        label = predictTaskExecutor.main(msg)
        kusoripu_score = label[1]

        return JsonResponse({
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': {'sentence': msg, 'kusoripu_score': kusoripu_score}
        })


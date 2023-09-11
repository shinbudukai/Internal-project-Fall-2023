from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.views import status
from rest_framework.views import Response
from .serializers import GetAllLanguageSerializer
from .models import languageDetect
from languageDetectTest import LanguageCalls
import unittest


# Create your views here.    

#print(detectlanguage.detect(["xin chào"]))

class HomepageView(TemplateView):
    template_name = 'app.html'

class GetAllLanguageAPIView(APIView):
    def get(self, request):
        list_language = languageDetect.objects.all()
        mydata = GetAllLanguageSerializer(list_language, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

def getInput(request):
    context = {}
    if request.method == 'POST':
        userInput = request.POST.get('userInput')
        #detect = detectlanguage.detect([userInput])
        detect = LanguageCalls(userInput).languageDecetion()
        context['userInput'] = detect
    return render(request,"app.html", context)


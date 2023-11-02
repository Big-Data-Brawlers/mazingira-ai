from django.shortcuts import render
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response


class Prediction(APIView):
    def post(self.request):
        data = request.data
        najibu = NinaswaliConfig.model
        Jibu = najibu.predict(data)
        response_dict = {"Predicted answer": Jibu}
        print(response_dict)
        return Response(response_dict, status=200)

from main.models import ImageModel
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .apps import MainConfig
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ("image",)


class call_model(ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = CommentSerializer

    def create(self, request):
        try:
            image = request.data.get("image")
            # sentence is the query we want to get the prediction for
            # predict method used to get the prediction
            response = MainConfig.predictor(image.file)

            # returning JSON response
            return Response(status=status.HTTP_200_OK, data={"response": response})
        except Exception as exc:
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"error": str(exc)}
            )
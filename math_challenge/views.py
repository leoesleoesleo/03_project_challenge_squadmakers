# Standard Library
import logging
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Django
from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView

# Internal
from math_challenge.services import (
    services_least_common_multiple, 
    services_plus_one
)

logger = logging.getLogger(__name__)


class LeastCommonMultipleViews(APIView):
    		
    class InputSerializer(serializers.Serializer):
        numbers = serializers.ListField()
    
    class OutputSerializer(serializers.Serializer):
        response = serializers.IntegerField()
    
    def get(self, request):
        try:
            input_serializer = self.InputSerializer(
                data=request.data
            )            
            input_serializer.is_valid(raise_exception=True)
            get_response = services_least_common_multiple(
                **input_serializer.validated_data
            )
            validated_data = self.OutputSerializer(
                get_response
            ).data
        except ValidationError:
            return Response(
                {
                    "status": "Error",
                    "message": "Invalid input data",
                    "errors": error.detail,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as error:
            logger.exception(
                "Error :: LeastCommonMultipleViews get:: %d", str(error)
            )
            return Response(
                {
                    "error": "Internal Server Error"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return Response(
            validated_data, status=status.HTTP_200_OK
        )


class ServicesPlusOneViews(APIView):
    		
    class InputSerializer(serializers.Serializer):
        number = serializers.IntegerField()
    
    class OutputSerializer(serializers.Serializer):
        response = serializers.IntegerField()
        
    def get(self, request):
        try:
            input_serializer = self.InputSerializer(
                data=request.data
            )            
            input_serializer.is_valid(raise_exception=True)
            get_response = services_plus_one(
                **input_serializer.validated_data
            )
            validated_data = self.OutputSerializer(get_response).data
        except ValidationError:
            return Response(
                {
                    "status": "Error",
                    "message": "Invalid input data",
                    "errors": error.detail,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as error:
            logger.exception(
                "Error :: ServicesPlusOneViews get:: %d", str(error)
            )
            return Response(
                {
                    "error": "Internal Server Error"
                }, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return Response(
            validated_data, status=status.HTTP_200_OK
        )

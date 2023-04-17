# Standard Library
import logging

# Django
from django.core.exceptions import ValidationError
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Internal
from joke_challenge.services import (
    services_delete_joke,
    services_get_joke,
    services_save_joke,
    services_update_joke
)

logger = logging.getLogger(__name__)


class JokeChallengeViews(APIView):
    		
    class InputSerializer(serializers.Serializer):
        param = serializers.CharField(allow_blank=True)
    
    class OutputSerializer(serializers.Serializer):
        response = serializers.CharField()
    
    @swagger_auto_schema(
        operation_summary="Get joke",
        operation_description="Gets a joke from Chuck or Dad",
        responses={
            200: openapi.Response(
                "Joke obtained", schema=OutputSerializer
            ),
            400: "Validation error",
            500: "Internal Server Error",
        },
        manual_parameters=[
            openapi.Parameter(
                name='param',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Kind of joke. Possible values: "Chuck" or "Dad"',
                required=False
            )
        ]
    )
    def get(self, request):
        try:
            input_serializer = self.InputSerializer(
                data=request.data
            )            
            input_serializer.is_valid(raise_exception=True)
            get_response = services_get_joke(
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
                "Error :: JokeChallengeViews get:: %d", str(error)
            )
            return Response(
                {"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return Response(
            validated_data, status=status.HTTP_200_OK
        )

    
    class PostInputSerializer(serializers.Serializer):
        text = serializers.CharField()
    
    class PostOutputSerializer(serializers.Serializer):
        response = serializers.CharField()

    @swagger_auto_schema(
        operation_summary="Save Joke",
        operation_description="Save a joke in the database",
        request_body=PostInputSerializer,
        responses={
            200: openapi.Response(
                "Joke Save", schema=PostOutputSerializer
            ),
            400: "Validation Error",
            500: "Internal Server Error",
        },
    )
    
    def post(self, request):
        """
        POST: will save in a database the joke
        (text passed by parameter)
        the text is assumed to be the joke itself
        """
        try:
            input_serializer = self.PostInputSerializer(
                data=request.data
            )            
            input_serializer.is_valid(raise_exception=True)
            services_save_joke(
                **input_serializer.validated_data
            )
            get_response = {"status": "Success"}
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
                "Error :: JokeChallengeViews post:: %d", str(error)
            )
            return Response(
                {"status": "Error", "message": "Internal server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return Response(get_response, status=status.HTTP_200_OK)
    
    
    class PutInputSerializer(serializers.Serializer):
        text = serializers.CharField()
        number = serializers.IntegerField()

    @swagger_auto_schema(
        operation_summary="Update Joker",
        operation_description="Update a joke in the database",
        request_body=PutInputSerializer,
        responses={
            200: openapi.Response(
                "Joke Update", schema=OutputSerializer
            ),
            400: "validation error",
            500: "Internal Server Error",
        },
    )
    
    def put(self, request):
        """
        UPDATE: updates the joke with the new text replacing the
        joke indicated in the parameter "number"
        """
        try:
            input_serializer = self.PutInputSerializer(
                data=request.data
            )
            input_serializer.is_valid(raise_exception=True)
            services_update_joke(
                **input_serializer.validated_data
            )
            get_response = {"status": "Success"}
            return Response(get_response, status=status.HTTP_200_OK)
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
                "Error :: JokeChallengeViews put:: %d", str(error)
            )
            return Response(
                {"status": "Error", "message": "Internal server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    
    class DeleteInputSerializer(serializers.Serializer):
        number = serializers.IntegerField()
    
    @swagger_auto_schema(
        operation_summary="Delete Joke",
        operation_description="Delete a joke in the database",
        request_body=DeleteInputSerializer,
        responses={
            200: openapi.Response(
                "Delete Joke", schema=OutputSerializer
            ),
            400: "validation error",
            500: "Internal Server Error",
        },
    )
    
    def delete(self, request):
        """
        DELETE: removes the joke indicated 
        in the parameter number
        """
        try:
            input_serializer = self.DeleteInputSerializer(
                data=request.data
            )
            input_serializer.is_valid(raise_exception=True)
            services_delete_joke(
                **input_serializer.validated_data
            )
            get_response = {"status": "Success"}
            return Response(get_response)
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
                "Error :: JokeChallengeViews delete:: %d", str(error)
            )
            return Response(
                {"status": "Error", "message": "Internal server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

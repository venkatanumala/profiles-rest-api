from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from res_framework.authentication import TokenAuthentication


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

# Create your views here.
""" Test APi View"""
class HelloApiView(APIView):

    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Retrun a list of APIView features """
        an_apiview=[
            'Uses  HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to Traditional Django view',
            'Gives you most control over your application',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """ create a hello message with your serializer"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """To update the complete object"""
        return Response({'message':'PUT'})

    def patch(self,request,pk=None):
        """To Partial update the object"""
        return Response({'message':'PATCH'})

    def delete(self,request,pk=None):
        """To delete the object"""
        return Response({'message':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test APi view set"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """return hello message"""
        a_viewset=[
            'Uses actions (list, Create, retrive, update, partial_update)',
            'Automatically maps to urls using Routers',
            'Provide more  functionality with less code',
            ]
        return Response({'message':'Hello','a_viewset':a_viewset})



    def create(self,request):
        """ create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self,request,pk=None):
        """ Hadinlng an object by getting its ID """
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """ Handling updating a object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handling updating part of an object(partial update)"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """ Destroying an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating anf updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permissions_class=(permissions.UpdateOwnProfile,)

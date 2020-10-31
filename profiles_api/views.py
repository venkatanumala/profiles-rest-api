from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
""" Test APi View"""
class HelloApiView(APIView):

    def get(self,request,format=None):
        """Retrun a list of APIView features """
        an_apiview=[
            'Uses  HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to Traditional Django view',
            'Gives you most control over your application',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete )',
            'Is similar to a traditional django view',
            'line3',
            'line4',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

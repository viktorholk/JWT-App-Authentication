from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken
# Create your views here.

@api_view(['GET'])
def current_user(request):
    # Determine the current user by their token, and return their data

    seriallizer = UserSerializer(request.user)
    return Response(seriallizer.data)

class UserList(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        seriallizer = UserSerializerWithToken(data=request.data)
        if seriallizer.is_valid():
            seriallizer.save()
            return Response(seriallizer.data, status=status.HTTP_201_CREATED)
        return Response(seriallizer.errors, status=status.HTTP_400_BAD_REQUEST)



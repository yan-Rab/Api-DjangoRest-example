from .models import Users
from .serializers import UsersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.http import Http404



class UsersViews(APIView):

    def get(self, request, format=None):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        serialized = UsersSerializer(data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)

        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersViewsDetail(APIView):

    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serialized = UsersSerializer(user)

        return Response(serialized.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serialized = UsersSerializer(user, data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)

        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.

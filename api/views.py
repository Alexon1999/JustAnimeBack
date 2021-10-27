from rest_framework import generics, status
from rest_framework.views import APIView
# Create your views here.
from .serializers import UserSerializer, UserConnecterSerializer
from .models import User
from rest_framework.response import Response


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SeConnecterView(APIView):
    serializer_class = UserConnecterSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs) -> Response:
        try:
            user = User.objects.get(mail=request.data.get(
                'mail'), mdp=request.data.get('mdp'))
            return Response({"msg": "trouvé", "user": self.serializer_class(user).data}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            # unauthorized
            return Response(status=status.HTTP_401_UNAUTHORIZED)

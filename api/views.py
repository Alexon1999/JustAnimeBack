from rest_framework import generics, status, permissions
from rest_framework.views import APIView
# Create your views here.
from .serializers import ContentSerializer, UserSerializer, UserConnecterSerializer
from .models import User, Content
from rest_framework.response import Response


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SeConnecterView(APIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs) -> Response:
        try:
            user = User.objects.get(mail=request.data.get(
                'mail'), mdp=request.data.get('mdp'))
            return Response({"msg": "trouvé", "user": self.serializer_class(user).data}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            # unauthorized
            return Response({"msg": "Nous n'avons pas trouvé pas trouvé d'utilisateur avec ces identifiants "}, status=status.HTTP_401_UNAUTHORIZED)


class CreateContentView(APIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.data.get('userId'))
            content = Content.objects.create(name=request.data.get(
                'name'), imageUrl=request.data.get('imageUrl'), tmdb_id=request.data.get('tmdbId'))
            user.watch_list.add(content)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

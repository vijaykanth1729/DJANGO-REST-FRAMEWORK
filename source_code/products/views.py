from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import (
                        BasicAuthentication,
                        SessionAuthentication,
                        TokenAuthentication
                        )
from rest_framework.permissions import IsAuthenticated
from .serializers import (
                        ProductSerializer,
                        AnimalSerializer,
                        MovieSerializer,
                        UserLoginSerializer
                        )
from .models import Product, Animal, Movie

@api_view(['GET', 'POST'])
def products_list(request, format=None):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def product_detail(request, pk, format=None):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AnimalApiView(APIView):
    def get(self, request, format=None):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnimalDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Animal.objects.get(id=id)
        except Animal.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        animal = self.get_object(id)
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)

    def put(self, request,id,format=None):
        animal = self.get_object(id)
        serializer = AnimalSerializer(animal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, format=None):
        animal = self.get_object(id)
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieListView(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args,**kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MovieDetailView(mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class MovieList(generics.ListCreateAPIView):
    # these are the very simplest forms of writing views..
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



class MovieViewSet(viewsets.ModelViewSet):
    # THis will generate urls automatically using Routers..
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # it finds all auths in list, if any one matches it gives data..
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
class ProductViewSet(viewsets.ModelViewSet):
    # THis will generate urls automatically using Routers..
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
class AnimalViewSet(viewsets.ModelViewSet):
    # THis will generate urls automatically using Routers..
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]



from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
class LoginView(APIView):
    # Implementing to retrive token, instead we can use djangp-rest-auth library.
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request,user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'Token':token.key},status=200)

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    def post(self, request):
        django_logout(request)
        return Response(status=204)

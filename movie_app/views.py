from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializers, MovieSerializers, ReviewSerializers


# @api_view(['GET', 'POST'])
# def director_list(request):
#     if request.method == 'GET':
#         queryset = Director.objects.all()
#         serializer = DirectorSerializers(queryset, many=True)
#         return Response(serializer.data, status=200)
#     elif request.method == 'POST':
#         serializer = DirectorSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)


class DirectorAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers

    # @api_view(['GET', 'PUT', ])
    # def director_detail(request, id):
    #     queryset = get_object_or_404(Movie, id=id)
    #     if Movie.method == 'GET':
    #         queryset = get_object_or_404(Movie, id=id)
    #         serializer = MovieSerializers(queryset)
    #         return Response(serializer.data, status=200)
    #     elif request.method == 'PUT':
    #         serializer = DirectorSerializers(queryset, data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=200)
    #     elif request.method == 'DELETE':
    #         queryset.delete()
    #         return Response(status=204)


class DirectorDetailAPIViwe(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers
    lookup_field = 'id'


# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         queryset = Movie.objects.all()
#         serializer = MovieSerializers(queryset, many=True)
#         return Response(serializer.data, status=200)
#     elif request.method == 'POST':
#         serializer = DirectorSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)


class MovieAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, id):
#     queryset = get_object_or_404(Movie, id=id)
#     if request.method == 'GET':
#         serializer = MovieSerializers(queryset)
#         return Response(serializer.data, status=200)
#     elif request.method == 'PUT':
#         serializer = MovieSerializers(queryset, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
#     elif request.method == 'DELETE':
#         queryset.delete()
#         return Response(status=204)


class MovieDetelAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    lookup_field = 'id'

    # @api_view(['GET'])
    # def review_list(request):
    #     if request.method == 'GET':
    #         queryset = Review.objects.all()
    #         serializer = ReviewSerializers(queryset, many=True)
    #         return Response(serializer.data, status=200)
    #     elif request.method == 'POST':
    #         serializer = ReviewSerializers(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=200)

    # @api_view(['GET', 'PUT', 'DELETE'])
    # def review_detail(request, id):
    #     queryset = get_object_or_404(Review, id=id)
    #     if request.method == 'GET':
    #         serializer = ReviewSerializers(queryset)
    #         return Response(serializer.data, status=200)
    #     elif request.method == 'PUT':
    #         serializer = ReviewSerializers(queryset, data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=200)
    #     elif request.method == 'DELETE':
    #         queryset.delete()
    #         return Response(status=204)


class ReviewAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    lookup_field = 'id'

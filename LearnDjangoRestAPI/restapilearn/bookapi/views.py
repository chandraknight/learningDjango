# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.response import Response  # this is to parse resonse
# # this is decorator for get post other requests
# from rest_framework.decorators import api_view
# # this is require to use status code
# from rest_framework import status
# from bookapi.models import Book
# from bookapi.serializer import BookSerializer

# # Create your views here.
# # this will return data without serilizer


# def books_list(request):
#     books = Book.objects.all()  # complex Data
#     # this will convert onject to list python data structure
#     booksPython = list(books.values())
#     return JsonResponse({
#         'books': booksPython
#     })  # this will json data


# @api_view(['GET'])  # this is necessary to handle api request methods
# def book_list_with_serializer(request):
#     books = Book.objects.all()  # complex Data
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])  # this is necessary to handle api request methods
# def book_create(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         # return Response(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def book(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except:
#         return Response({
#             'error': 'Book Not found'
#         }, status=status.HTTP_404_NOT_FOUND)
#     if (request.method == 'GET'):
#         serializer = BookSerializer(book)
#         return Response(serializer.data)

#     if (request.method == 'PUT'):
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     if request.method == 'DELETE':
#         book.delete()
#         # return Response({
#         #     "delete": True
#         # })
#         return Response(status=status.HTTP_204_NO_CONTENT)

# defining class views

from rest_framework.views import APIView  # this will help to inerite view
from rest_framework.response import Response  # this is to parse resonse

# this is require to use status code
from rest_framework import status
from bookapi.models import Book
from bookapi.serializer import BookSerializer


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            # return Response(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    def get_book_by_pk(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Book Not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

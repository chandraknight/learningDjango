from django.urls import path
# from . import views
from bookapi.views import BookList,BookCreate,BookDetail

urlpatterns = [
    # path('list/',views.books_list,name='list'),
    # path('listwithserializer/',views.book_list_with_serializer,name='listwithserializer'),
    # path('create/',views.book_create,name='createbook'),
    # path('<int:pk>',views.book),

    path('list/',BookList.as_view()),
    path('create/',BookCreate.as_view()),
    path('<int:pk>',BookDetail.as_view()),
]

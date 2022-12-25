from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.say_hello, name='hello'),
    path('hellofromhtml/', views.render_html_file, name='hellofromhtml'),
path('render_html_file_with_context/',views.render_html_file_with_context,name='renderhtmlfilewithcontext')
]

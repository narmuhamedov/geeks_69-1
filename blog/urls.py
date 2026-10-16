from django.urls import path
from . import views

urlpatterns = [
    path('hello_world/', views.HelloWorldView.as_view()),
    path('my_favourite_emodji/', views.MyFavouriteEmodjiView.as_view()),
    path('about_my_self/', views.AboutMySelfView.as_view()),
    
    path('blog_list/', views.BlogListView.as_view()),
    path('blog_list/<int:id>/', views.BlogDetailView.as_view()),
    path('search/', views.SearchView.as_view()),
]


from django.urls import path
from blogapp import views
urlpatterns = [
    path('',views.signup),
    path('login/',views.LogIn),
    path('home/',views.home),
    path('mypost/',views.myPost,name='mypost'),
    path('newpost/',views.newPost),
    path('signout/',views.signout),
    path('update/<int:pk>',views.postupdate.as_view()),
    path('delete/<int:pk>',views.postdelete.as_view())
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('categories/', views.categories_page, name='categories'),
    path('difficult-words/', views.difficult_words_page, name='difficult_words'),
    path('image-speaking/', views.image_speaking_page, name='image_speaking'),
]
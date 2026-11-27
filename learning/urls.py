
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('categories/', views.categories_page, name='categories'),
    path('difficult-words/', views.difficult_words_page, name='difficult_words'),
    path('image-speaking/', views.image_speaking_page, name='image_speaking'),
    path('categories/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('exercises/', views.exercises_page, name='exercises'),
    path('listening/', views.listening_page, name='listening'),
    path('speaking/', views.speaking_page, name='speaking'),
    path('reading/', views.reading_page, name='reading'),
    path('vocabulary/', views.vocabulary_page, name='vocabulary'),
]

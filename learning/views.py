from django.shortcuts import render

def home(request):
    return render(request, 'learning/home.html')

def login_page(request):
    return render(request, 'learning/login.html')

def register_page(request):
    return render(request, 'learning/register.html')
def categories_page(request):
    return render(request, 'learning/categories.html')
def difficult_words_page(request):
    return render(request, 'learning/difficult_words.html')
def image_speaking_page(request):
    return render(request, 'learning/image_speaking.html')
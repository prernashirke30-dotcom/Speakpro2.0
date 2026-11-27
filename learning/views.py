
from django.shortcuts import render
from django.http import Http404


# HOME PAGE
def home(request):
    return render(request, 'learning/home.html')


# LOGIN PAGE
def login_page(request):
    return render(request, 'learning/login.html')


# REGISTER PAGE
def register_page(request):
    return render(request, 'learning/register.html')


# CATEGORIES PAGE
def categories_page(request):
    return render(request, 'learning/categories.html')


# DIFFICULT WORDS PAGE
def difficult_words_page(request):
    return render(request, 'learning/difficult_words.html')


# IMAGE SPEAKING PAGE
def image_speaking_page(request):
    return render(request, 'learning/image_speaking.html')


# CATEGORY DATA
CATEGORY_DATA = {
    'daily-use': {
        'title': 'Daily Use English',
        'words': [
            {'word': 'Beautiful', 'meaning': 'सुंदर', 'example': 'This is a beautiful flower.'},
            {'word': 'Important', 'meaning': 'महत्वपूर्ण', 'example': 'English is important.'},
            {'word': 'Happy', 'meaning': 'खुश', 'example': 'I am happy today.'},
        ]
    },

    'interview': {
        'title': 'Interview English',
        'words': [
            {'word': 'Experience', 'meaning': 'अनुभव', 'example': 'I have two years of experience.'},
            {'word': 'Confident', 'meaning': 'आत्मविश्वासी', 'example': 'I am confident.'},
        ]
    },

    'basic': {
        'title': 'Basic English',
        'words': [
            {'word': 'Apple', 'meaning': 'सेब', 'example': 'I eat an apple.'},
            {'word': 'Water', 'meaning': 'पानी', 'example': 'I drink water.'},
        ]
    },

    'advanced': {
        'title': 'Advanced English',
        'words': [
            {'word': 'Magnificent', 'meaning': 'शानदार', 'example': 'The view is magnificent.'},
            {'word': 'Inevitable', 'meaning': 'अपरिहार्य', 'example': 'Change is inevitable.'},
        ]
    },

    'business': {
        'title': 'Business English',
        'words': [
            {'word': 'Meeting', 'meaning': 'बैठक', 'example': 'I have a meeting today.'},
            {'word': 'Negotiation', 'meaning': 'बातचीत', 'example': 'The negotiation was successful.'},
        ]
    },

    'travel': {
        'title': 'Travel English',
        'words': [
            {'word': 'Journey', 'meaning': 'यात्रा', 'example': 'Have a safe journey.'},
            {'word': 'Reservation', 'meaning': 'आरक्षण', 'example': 'I have a hotel reservation.'},
        ]
    },
}


# CATEGORY DETAIL PAGE
def category_detail(request, category_slug):
    category = CATEGORY_DATA.get(category_slug)

    if category is None:
        raise Http404("Category not found")

    return render(request, 'learning/category_detail.html', {
        'category': category
    })


# ENGLISH EXERCISES
def exercises_page(request):
    return render(request, 'learning/activity.html', {
        'title': 'English Exercises'
    })


# LISTENING PRACTICE
def listening_page(request):
    return render(request, 'learning/listening.html')


# SPEAKING PRACTICE
def speaking_page(request):
    return render(request, 'learning/speaking.html')


# READING PRACTICE
def reading_page(request):
    return render(request, 'learning/reading.html')


# VOCABULARY LISTING
def vocabulary_page(request):
    return render(request, 'learning/activity.html', {
        'title': 'Vocabulary Listing'
    })

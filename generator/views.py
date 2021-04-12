from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'home.html')
def password(request):
    characters = list('abcdefghjkilmnopqrstuvyxwz')
    upper_char = list('ABCDEFGHJKILMNOPQRSTUVYXWZ')
    numbers = list('1234567890')
    specials_char = list('!@#$%^&*()_+-=<>?/\\')
    mypass = ''
    length = int(request.GET.get('length', 10))
    if request.GET.get('uppercase'):
        characters.extend(upper_char)
    if request.GET.get('number'):
        characters.extend(numbers)
    if request.GET.get('special'):
        characters.extend(specials_char)

    for x in range(length):
        mypass += random.choice(characters)
    return render(request, 'password.html' , { 'password' : mypass})

import random
import string
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def generate_password(request):
    length = int(request.GET.get('length', 12))
    include_upper = request.GET.get('uppercase')
    include_lower = request.GET.get('lowercase')
    include_numbers = request.GET.get('numbers')
    include_special = request.GET.get('special')

    characters = ''
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        password = 'Please select at least one option.'
    else:
        password = ''.join(random.choice(characters) for _ in range(length))

    return render(request, 'result.html', {'password': password})

import json
import os
from django.shortcuts import render

MEALS_JSON_PATH = os.path.join(os.path.dirname(__file__), 'meals.json')


def load_meals():
    with open(MEALS_JSON_PATH, 'r') as f:
        return json.load(f)


def menu_view(request):
    meals = load_meals()

    search_name     = request.GET.get('name', '').strip()
    filter_category = request.GET.get('category', '').strip()

    all_categories = sorted(set(m['category'] for m in meals))

    filtered = meals

    if search_name:
        filtered = [m for m in filtered if search_name.lower() in m['name'].lower()]

    if filter_category and filter_category != 'All Categories':
        filtered = [m for m in filtered if m['category'] == filter_category]

    return render(request, 'menu/menu.html', {
        'meals':             filtered,
        'categories':        all_categories,
        'selected_category': filter_category,
        'search_name':       search_name,
    })

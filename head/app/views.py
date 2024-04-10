from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
import os
from xml.etree import ElementTree as ET
from django.http import JsonResponse
import json

def parse_xml_data(xml_file):
    data = []
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for doc in root.findall('doc'):
        item = {}
        for field in doc.findall('field'):
            item[field.attrib['name']] = field.text
        data.append(item)
    return data

def index(request):
    xml_file_path = os.path.join(settings.STATIC_ROOT, 'xml', 'data.xml')
    data = parse_xml_data(xml_file_path)
    paginator = Paginator(data, 10)  # Assuming 10 items per page
    page = request.GET.get('page')
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'reviews': reviews})

def search_reviews(request):
    keyword = request.GET.get('keyword')
    xml_file = os.path.join(settings.STATIC_ROOT, 'xml', 'data.xml')
    data = parse_xml_data(xml_file)
    filtered_reviews = [review for review in data if keyword.lower() in review['review'].lower()]
    return JsonResponse(filtered_reviews, safe=False)

def filter_reviews(request):
    cuisines = request.GET.getlist('cuisines[]')
    stars = request.GET.getlist('stars[]')
    xml_file = os.path.join(settings.STATIC_ROOT, 'xml', 'data.xml')
    data = parse_xml_data(xml_file)
    
    filtered_reviews = data
    
    # Filter by cuisines
    if cuisines:
        filtered_reviews = [review for review in filtered_reviews if review['categoryName'].lower() in cuisines]
    
    # Filter by stars
    if stars:
        filtered_reviews = [review for review in filtered_reviews if review['review_stars'] in stars]
    
    return JsonResponse(filtered_reviews, safe=False)

def sort_reviews(request):
    sort_by = request.GET.get('sort_by')
    sort_order = request.GET.get('sort_order')
    xml_file = os.path.join(settings.STATIC_ROOT, 'xml', 'data.xml')
    data = parse_xml_data(xml_file)
    if sort_by == 'date':
        sorted_reviews = sorted(data, key=lambda x: x['publishedAtDate'], reverse=(sort_order == 'desc'))
    elif sort_by == 'stars':
        sorted_reviews = sorted(data, key=lambda x: x['review_stars'], reverse=(sort_order == 'desc'))
    elif sort_by == 'likes_count':
        sorted_reviews = sorted(data, key=lambda x: int(x['likesCount']), reverse=(sort_order == 'desc'))
    else:
        sorted_reviews = data
    return JsonResponse(sorted_reviews, safe=False)

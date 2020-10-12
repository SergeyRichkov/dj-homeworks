from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv
import urllib.parse


def index(request):
    return redirect(reverse('bus_st'))


def bus_stations(request):
    station_info = []
    with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            station_info.append({'Name': row['Name'], 'Street': row['Street'],
                                 'District': row['District']})

    paginator = Paginator(station_info, 10, orphans=5)
    page_number = request.GET.get('page', 1)
    current_page = paginator.page(page_number)
    page_obj = paginator.get_page(page_number)
    data = page_obj.object_list

    np, pp = 1, 1
    if page_obj.has_next():
        np = page_obj.next_page_number()
    if page_obj.has_previous():
        pp = page_obj.previous_page_number()

    np_params = urllib.parse.urlencode({'page': np})
    pp_params = urllib.parse.urlencode({'page': pp})
    next_page_url = f"{reverse('bus_st')}?{np_params}"
    prev_page_url = f"{reverse('bus_st')}?{pp_params}"

    return render(request, 'index.html',
                  context={
         'bus_stations': data,
                      'current_page': current_page,
                      'prev_page_url': prev_page_url,
                      'next_page_url': next_page_url
                  })




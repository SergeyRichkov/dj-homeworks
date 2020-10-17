from django.shortcuts import render
from django.conf import settings
import csv

def inflation_view(request):
    template_name = 'inflation.html'

    inflation_table = []
    with open(settings.INFLATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
           inflation_table.append(row)
    title_row = inflation_table[0]
    years = inflation_table[1:]
    back_color = 'red'



    # чтение csv-файла и заполнение контекста
    context = {'title_row': title_row,
               'years': years,
               'back_colors': back_color}

    return render(request, template_name,
                  context=context)

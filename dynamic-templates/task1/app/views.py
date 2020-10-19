from django.shortcuts import render
from django.conf import settings
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    inflation_info = []
    title_iflation_row = []
    with open(settings.INFLATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        dict_reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            title_iflation_row.append(row)
        csvfile.seek(0)
        for row2 in dict_reader:
            inflation_info.append({
                'Year': row2['Год'],
                'Jan': row2['Янв'], 'Feb': row2['Фев'], 'Mar': row2['Мар'],
                'Apr': row2['Апр'], 'May': row2['Май'], 'Jun': row2['Июн'],
                'Jul': row2['Июл'], 'Aug': row2['Авг'], 'Sep': row2['Сен'],
                'Oct': row2['Окт'], 'Nov': row2['Ноя'], 'Dec': row2['Дек'],
                'Summ': row2['Суммарная']})

    title_row = title_iflation_row[0]

    context = {'title_row': title_row,
               'inflation_info': inflation_info
               }

    return render(request, template_name,
                  context=context)

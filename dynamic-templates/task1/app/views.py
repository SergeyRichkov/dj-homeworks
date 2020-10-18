from django.shortcuts import render
from django.conf import settings
import csv

def inflation_view(request):
    template_name = 'inflation.html'

    inflation_table = []
    inflation_info = []
    title_iflation_row = []
    with open(settings.INFLATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        dict_reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            title_iflation_row.append(row)
            inflation_table.append(row[1:-1])
        csvfile.seek(0)
        for row2 in dict_reader:
            inflation_info.append({'Year': row2['Год'], 'Summ': row2['Суммарная']})


    title_row = title_iflation_row[0][1:-1]
    years = inflation_table[1:]
    a = []
    b = []
    c = []
    for abc in inflation_info:
        a.append(abc['Year'])
        b.append(abc['Summ'])

    c = [a, b]
    print(1111111111, c)



    context = {'title_row': title_row,
               'years': years,
               'inflation_info': inflation_info,
               'c': c
                # 'inflation_of_year': inflation_of_years
               }

    return render(request, template_name,
                  context=context)

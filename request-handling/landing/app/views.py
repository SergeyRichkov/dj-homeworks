from collections import Counter
from django.shortcuts import render, reverse

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    template_name = 'home.html'
    pages = {
        'Вариант A': reverse('landing') + '?ab-test-arg=original',
        'Вариант B': reverse('landing') + '?ab-test-arg=test',
    }

    context = {
        'pages': pages
    }
    param = request.GET.get('from-landing', '')
    if param == 'original':
        counter_click[param] += 1
    elif param == 'test':
        counter_click[param] += 1
    return render(request, template_name, context)


def landing(request):
    param = request.GET.get('ab-test-arg', '')
    counter_show[param] += 1
    if param == 'original':
        print(counter_show)
        return render(request, 'landing.html', counter_show)
    elif param == 'test':
        print(counter_show)
        return render(request, 'landing_alternate.html', counter_show)


def stats(request):
    test_conv = counter_click['test'] / counter_show['test']
    origin_conv = counter_click['original'] / counter_show['original']
    return render(request, 'stats.html', context={
        'test_conversion': test_conv,
        'original_conversion': origin_conv,
    })

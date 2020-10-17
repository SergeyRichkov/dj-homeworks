from django import  template

register = template.Library()

@register.filter
def background_paint(value):
    color = ''
    if value == '':
        color = 'white'
    elif float(value) >= 1 and float(value) <= 2 :
        color = 'salmon'
    elif float(value) > 2 and float(value) <= 5 :
        color = 'red'
    elif float(value) > 5:
        color = 'darkred'
    elif float(value) < 0:
        color = 'green'
    else:
        color = 'white'
    return color

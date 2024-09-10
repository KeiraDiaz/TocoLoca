from django.shortcuts import render

def show_main(request):
    context = {
        'Name' : 'Mushroom Lamp',
        'Price': '$19.90',
        'Desc': 'Cute Lamp'
    }

    return render(request, "main.html", context)
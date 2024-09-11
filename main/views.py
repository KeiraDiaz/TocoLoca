from django.shortcuts import render

def show_main(request):
    context = {
        'Name' : 'TocaLoca',
        'Price': 'Name',
        'Desc': 'KKI'
    }

    return render(request, "main.html", context)
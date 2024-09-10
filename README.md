# Assignment 2 Breakdown of the Process (UNFINISHED)

# Explain how you implemented the checklist above step-by-step (not just following the tutorial).

First and Foremost, breaking down the problem step by step to have a clear vision on what to do. After analyzing, I realized that they were asking for a combination of tutorial 0 and 1.

```
env\Scripts\activate
```

This first line is to activate the previous virtual environment I had already created from the tutorials. The purpose of this virtual environment is to store all my dependencies and imports rather than importing them all to my computer.

```
django-admin startproject TocoLoca .
```

Next, it was time to set up the actual django project which I set as TocoLoca, which is a play on "toko lokal".

```
python manage.py startapp main

...
INSTALLED_APPS = [
    ...,
    'main'
]
...
```

I then created an application as part of my django project called main and added main as an installed app in my settings.py thats in my original TocoLoca Project. After that, I created a simple HTML Page with CSS styling and put that in my templates inside main. Furthermore, I started programmed a model to fit this program. 

```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

```

Now, it's time to handle migrations. This involves creating a folder for migrations and applying migrations to the local database. 

```
python manage.py makemigrations
python manage.py migrate
```

Moving on,

```
from django.shortcuts import render

def show_main(request):
    context = {
        'Name' : 'Mushroom Lamp',
        'Price': '$19.90',
        'Desc': 'Cute Lamp'
    }

    return render(request, "main.html", context)
```


```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

I put this block of code inside my views.py inside main.

# Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.

![image](https://github.com/user-attachments/assets/bcf23b23-161a-413f-b5f9-5d586b95a893)


# Explain the use of git in software development!

Git is a distributed version control system used in software development to track changes in code, facilitate collaboration, and maintain a history of revisions. It enables developers to create branches to work on new features or bug fixes without affecting the main codebase. These branches can be merged back into the main project after review, ensuring that changes are integrated smoothly. Git also provides tools for resolving conflicts when multiple developers make changes to the same code. Its use ensures code consistency, enables teamwork, and helps manage complex projects efficiently by tracking every change.

# In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?

Django is often used as a starting point for learning software development because it provides a well-structured and beginner-friendly framework with everything included. Its "batteries-included" philosophy offers built-in features like an admin panel, authentication, and database management, which help newcomers quickly build functional applications without needing extensive setup. Django emphasizes good development practices, including the DRY (Don't Repeat Yourself) principle, making it easier to learn clean, maintainable code.

# Why is the Django model called an ORM?

The Django model is called an ORM (Object-Relational Mapping) because it acts as a bridge between the relational database and the object-oriented programming model. In Django, models represent database tables, and each instance of a model corresponds to a row in the table. The ORM allows developers to interact with the database using Python code instead of writing raw SQL queries. It automatically converts Python objects (models) into database records and vice versa, simplifying database operations and making it easier to work with complex data relationships within a Python application.

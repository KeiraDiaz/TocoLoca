# TocoLoca 🛍️🌴
### Your favorite local shop for simple goodies!!

<details>

<summary>Assignment 3</summary>

## Explain why we need data delivery in implementing a platform.

EEffective data delivery is key to running a platform because it ensures that information reaches the right people or systems quickly and correctly. This helps the platform function smoothly, supports real-time decisions, keeps data secure, and makes sure everyone is using the latest information. Without good data delivery, platforms would struggle with performance, fail to meet user needs, and have trouble protecting sensitive information.

## In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?

Personally, I prefer JSON because it's structure and distinct appearance, making it much more human readable. According to [Amazon Web Services](https://aws.amazon.com/compare/the-difference-between-json-xml/#:~:text=JSON%20is%20simple%20and%20more,is%20complex%20and%20less%20flexible.&text=JSON%20supports%20numbers%2C%20objects%2C%20strings,dates%2C%20images%2C%20and%20namespaces.), JSON is faster to parse and better suited for APIs, mobile apps, and data interchange, while XML is ideal for complex data structures with multiple variables. JSON supports fewer data types but is generally more efficient and secure. 

## Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.'

The is_valid() method in Django forms checks whether the data entered meets the form’s validation rules, such as data type and length. If all fields contain valid data, it returns True and stores the cleaned data in the form’s cleaned_data attribute. This method is crucial for ensuring that user input is correct and ready to be processed or saved to the database. It simplifies error handling by verifying data before any further actions, helping to maintain data integrity and prevent invalid entries.

## Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?


The csrf_token is a crucial security feature in Django that protects web applications from Cross-Site Request Forgery (CSRF) attacks. These attacks occur when an attacker tricks an authenticated user into unknowingly submitting malicious requests, potentially leading to unauthorized actions like changing account details or transferring funds. The csrf_token ensures that every form submission or request comes from a legitimate source (the same domain) by embedding a unique token in each form. When the form is submitted, the server checks the token, and if it's missing or invalid, the request is rejected, preventing unauthorized actions and securing the user’s session.

## Explain how you implemented the checklist above step-by-step (not just following the tutorial).

<details>
<summary>POSTMAN Proof</summary>
![image](https://github.com/user-attachments/assets/e8ab748e-8410-4748-8e51-448778a10148)
![image](https://github.com/user-attachments/assets/b13d5cc0-19d7-4acf-bc77-abd4b30f52d5)
![image](https://github.com/user-attachments/assets/e09fe769-e139-4e48-aba4-02541c9d4a78)
![image](https://github.com/user-attachments/assets/a0a2acc8-eeea-4f9e-91f3-2c47a1efb522)
</details>

## Explain how you implemented the checklist above step-by-step

1. First thing I did was create a html template, all my pages will be following this template, and modified this line so that it would be accessible by the other html files.

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
```

```
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
```

2. After that, I changed a couple lines in the model.py so that any item entries will now have an id

```
import uuid
...
class ItemEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ...
```
3. 

</details>

<details>


<summary>Assignment 2</summary>

## Explain how you implemented the checklist above step-by-step.

### Create a new Django project.

First and Foremost, breaking down the problem step by step to have a clear vision on what to do. After analyzing, I realized that they were asking for a combination of tutorial 0 and 1.

```
env\Scripts\activate
```

This first line is to activate the previous virtual environment I had already created from the tutorials. The purpose of this virtual environment is to store all my dependencies and imports rather than importing them all to my computer.

```
django-admin startproject TocoLoca .
```

Next, it was time to set up the actual django project which I set as TocoLoca, which is a play on "toko lokal".

### Create an application with the name main in the project.

```
python manage.py startapp main
```
### Perform routing in the project so that the application main can run.
```
...
INSTALLED_APPS = [
    ...,
    'main'
]
...
```

I then created an application as part of my django project called main and added main as an installed app in my settings.py thats in my original TocoLoca Project.   Now, it's time to handle migrations. This involves creating a folder for migrations and applying migrations to the local database. 

```
python manage.py makemigrations
python manage.py migrate
```


### Create a model in the application main with the name Product and have the mandatory
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

```

Moving on, I started programmed a model to fit this program. 

### Create a function in views.py to return to an HTML template that displays the name of the application and your name and class.

```
from django.shortcuts import render

def show_main(request):
    context = {
        'Name' : 'TocaLoca',
        'Price': 'Keidi',
        'Desc': 'KKI'
    }

    return render(request, "main.html", context)
```

My function called show_main returns a HTML template based on the request.

### Create a routing in urls.py for the application main to map the function created in views.py.

```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
The above is in urls.py which is part of main.


## Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.

![image](https://github.com/user-attachments/assets/bcf23b23-161a-413f-b5f9-5d586b95a893)


## Explain the use of git in software development!

Git is a distributed version control system used in software development to track changes in code, facilitate collaboration, and maintain a history of revisions. It enables developers to create branches to work on new features or bug fixes without affecting the main codebase. These branches can be merged back into the main project after review, ensuring that changes are integrated smoothly. Git also provides tools for resolving conflicts when multiple developers make changes to the same code. Its use ensures code consistency, enables teamwork, and helps manage complex projects efficiently by tracking every change.

# In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?

Django is often used as a starting point for learning software development because it provides a well-structured and beginner-friendly framework with everything included. Its "batteries-included" philosophy offers built-in features like an admin panel, authentication, and database management, which help newcomers quickly build functional applications without needing extensive setup. Django emphasizes good development practices, including the DRY (Don't Repeat Yourself) principle, making it easier to learn clean, maintainable code.

# Why is the Django model called an ORM?

The Django model is called an ORM (Object-Relational Mapping) because it acts as a bridge between the relational database and the object-oriented programming model. In Django, models represent database tables, and each instance of a model corresponds to a row in the table. The ORM allows developers to interact with the database using Python code instead of writing raw SQL queries. It automatically converts Python objects (models) into database records and vice versa, simplifying database operations and making it easier to work with complex data relationships within a Python application.

</details>

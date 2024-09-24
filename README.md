# TocoLoca 🛍️🌴
### Your favorite local shop for simple goodies!!

<details>

<summary> Assignment 4
</summary>

## 1. Differences between HttpResponseRedirect() and redirect() 
* HttpResponseRedirect():
A built-in Django class that returns an HTTP 302 response to redirect to a specific URL.Typically used when we want more control and modification on the response before returning it (e.g., adding cookies or values into the website’s local storage).
* redirect():
A Django shortcut function that implicitly uses HttpResponseRedirect().
redirect() is more convenient because it can accept various parameters (URL, named URL patterns, model instances, etc.) and is more concise in syntax.

## 2. How the Product Model is Linked to the User Model
In this project, the ItemEntry model is usually linked to the User model using ForeignKey. This connects each item to a specific user.
```
class ItemEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    desc = models.TextField()

```
Each time a user creates a item entry, that entry is associated with exactly one logged-in User. ForeignKey is used to create a many-to-one relationship between ItemEntry and User. In other words, one user can have many products, but each product belongs to only one user.

## 3. Differences Between Authentication and Authorization and what happens when a user logs in.

Authentication is the process of verifying a user's identity, typically through credentials like a username and password. It ensures that only users with valid accounts can access the website. For example, when a user logs in with their credentials, their identity is authenticated. On the other hand, authorization determines what an authenticated user is allowed to access. It assigns specific permissions based on the user's role. For instance, after logging in, an admin can access the /admin panel, while a regular user cannot.

In Django, authentication verifies the user's credentials, and once successful, authorization checks their permissions to grant or restrict access to various resources. Django manages both processes using middleware. The authenticated user is stored as request.user in every request, making it easy to retrieve user information. Additionally, Django offers permissions and groups to control access at a granular level, allowing different levels of access for different users. Built-in decorators like @login_required and permission checks can be applied to views to ensure secure access.

## 4. How Django remembers logged-in users

Django remembers logged-in users using sessions and cookies.

After a user successfully logs in, Django creates a session for the user and stores the session ID in a cookie on the user’s browser.
The cookie contains user data, which is typically encrypted.
This cookie is then sent to the server with every subsequent request, so for each protected request, the user must include the cookie.
The cookie will be decrypted into the original user data, and the server will determine if the user data in the cookie is valid.
Other Uses of Cookies:

Cookies can be used to track user preferences, save shopping carts, or store other temporary data between requests. ## paragraph form please

Not all cookies are secure, and improperly protected cookies can be vulnerable to attacks such as Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF). To enhance security, Django provides several mechanisms for safeguarding cookies, including but not limited to:
* HttpOnly: Prevents cookies from being accessed via client-side JavaScript, protecting against XSS attacks.
* Secure: Ensures cookies are only sent over HTTPS, preventing them from being transmitted over insecure connections.


Here is the translation of your text to English:

1. Differences between HttpResponseRedirect() and redirect()
HttpResponseRedirect():

A built-in Django class that returns an HTTP 302 response to redirect to a specific URL.
Typically used when we want more control and modification on the response before returning it (e.g., adding cookies or values into the website’s local storage).
Example:
python
Copy code
.......
def login_user(request):
    if request.user.is_authenticated:
        return redirect('main:show_main')
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', datetime.datetime.now())
            return response

    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'auth/login.html', context)

# Authentication Views
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User has been created")
            return redirect('main:login')

    context = {'form': form}
    return render(request, 'auth/register.html', context)
.......
Main Difference: redirect() is a simpler way to perform redirects and is flexible with parameters, while HttpResponseRedirect() provides more control for modifications before sending the response.

## 2. How the Product Model is Linked to the User Model
In this project, the Product model is usually linked to the User model using ForeignKey. This connects each Product to a specific user.

```
class Product(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
```
How it works:
Each time a user creates a product entry, that entry is associated with exactly one logged-in User.
ForeignKey is used to create a many-to-one relationship between Product and User. In other words, one user can have many products, but each product belongs to only one user.

## 3. Differences Between Authentication and Authorization
Authentication is the process of verifying a user's identity, typically through credentials like a username and password. It ensures that only users with valid accounts can access the website. For example, when a user logs in with their credentials, their identity is authenticated. On the other hand, authorization determines what an authenticated user is allowed to access. It assigns specific permissions based on the user's role. For instance, after logging in, an admin can access the /admin panel, while a regular user cannot.

In Django, authentication verifies the user's credentials, and once successful, authorization checks their permissions to grant or restrict access to various resources. Django manages both processes using middleware. The authenticated user is stored as request.user in every request, making it easy to retrieve user information. Additionally, Django offers permissions and groups to control access at a granular level, allowing different levels of access for different users. Built-in decorators like @login_required and permission checks can be applied to views to ensure secure access.

## 4. How Django Remembers Logged-In Users
Authentication is the process of verifying a user's identity, typically through credentials like a username and password. It ensures that only users with valid accounts can access the website. For example, when a user logs in with their credentials, their identity is authenticated. On the other hand, authorization determines what an authenticated user is allowed to access. It assigns specific permissions based on the user's role. For instance, after logging in, an admin can access the /admin panel, while a regular user cannot.

In Django, authentication verifies the user's credentials, and once successful, authorization checks their permissions to grant or restrict access to various resources. Django manages both processes using middleware. The authenticated user is stored as request.user in every request, making it easy to retrieve user information. Additionally, Django offers permissions and groups to control access at a granular level, allowing different levels of access for different users. Built-in decorators like @login_required and permission checks can be applied to views to ensure secure access.

# Checklist Implementation Steps
### 1. Implementing User Registration, Login, and Logout Functions
a) Create a form in a view for new user registration using UserCreationForm
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
b) Create the auth/register.html template to display the registration form.
c) Create a login form in a view for registered users to log in
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
d) Create the auth/login.html template to display the login form
e) Create a logout form in a view for users to log out.
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
g) Add a logout link in the template for easy logout through a button
h) Finally, ensure all views are called through urls.py:
```
urlpatterns = [
    ...
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```

### 2. Linking Product Model to User
a) Create a Product model and add a ForeignKey to User so that each created product can be associated with a user.
```
import uuid 
from django.db import models
from django.contrib.auth.models import User

class ItemEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    desc = models.TextField()

```
b) Run migrations to apply the changes

### 3. Using Cookies
a) Set cookies when the user logs in
```
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
```

</details>

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

2. After that, I changed a couple lines in the `model.py` so that any item entries will now have an id

```
import uuid
...
class ItemEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ...
```

3. Moving on, we create a Form Input Data, where we will be adding the way our data will be stored in the database

```
from django.forms import ModelForm
from main.models import ItemEntry

class ItemEntryForm(ModelForm):
    class Meta:
        model = ItemEntry
        fields = ["name", "price", "desc"]
```

4. On `views.py`, we change this line of code so that we can allow redirects, in the same file, we create this new function so that we can request with method POST to our DB.

```
from django.shortcuts import render, redirect
```

```
def create_new_item(request):
    form = ItemEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_new_item.html", context)
```

5. I've also adjusted my `show_main` function like this

```
def show_main(request):
    item_entries = ItemEntry.objects.all()

    context = {
        'Name' : 'TocaLoca',
        'Price': 'Keira Diaz',
        'Desc': 'KKI',
        'item_entries' : item_entries
    }

    return render(request, "main.html", context)
```

Additionally, I've also created this functions, I'll explain below.

```
def show_xml(request):
    data = ItemEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ItemEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

6. To perform routing, I changed  `urls.py`, so that we imported all the functions and include their path in url_patterns.

```
from main.views import show_main, create_new_item, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_new_item', create_new_item, name='create_new_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

7. I then modified the html file for main and create new item
8. Back to representing data is JSON and XML, I needed to add some imports earlier, namely these two

```
from django.http import HttpResponse
from django.core import serializers
```
Serializer are what converts python data types to your desired data type and vice versa, in this case, XML and JSON. The functions earlier would combine all the the data in the database and represnt it as its respective form. The difference between with id and without id is that the function has an added filter. 

<details>
<summary>POSTMAN Proof</summary>
  
![image](https://github.com/user-attachments/assets/e8ab748e-8410-4748-8e51-448778a10148)

![image](https://github.com/user-attachments/assets/b13d5cc0-19d7-4acf-bc77-abd4b30f52d5)

![image](https://github.com/user-attachments/assets/e09fe769-e139-4e48-aba4-02541c9d4a78)

![image](https://github.com/user-attachments/assets/a0a2acc8-eeea-4f9e-91f3-2c47a1efb522)

</details>

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

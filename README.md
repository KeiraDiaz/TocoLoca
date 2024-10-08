# TocoLoca 🛍️🌴
### Your favorite local shop for simple goodies!!


<details>
<summary> Assignment 6 </summary>

##1. Benefits of Using JavaScript in Web Application Development

JavaScript is a very important programming language in web application development for several reasons:

- **Dynamic Interactivity:** JavaScript allows the creation of more interactive web pages, such as animations, responsive buttons, and manipulation of HTML elements without needing to reload the entire page.
- **Asynchronous Programming:** JavaScript supports asynchronous programming through techniques like AJAX and `fetch()`, which allow data to be retrieved from the server dynamically without affecting the user experience.
- **Frontend Validation:** JavaScript enables client-side input validation before it is sent to the server, reducing the number of errors that reach the backend.
- **Cross-Platform Compatibility:** JavaScript can be used across different platforms and browsers, making it a flexible and widely-used solution on various devices.

##2. The Function of `await` in `fetch()` and the Consequences of Not Using It

The `await` function in `fetch()` serves to wait for the completion of the fetch (asynchronous operation) before continuing the execution of the next line of code. This allows us to obtain the response data before using it further.

If we do not use `await`, the program will continue execution without waiting for the result of `fetch()`, which can lead to:

- **Promise Pending:** The result of `fetch()` will be a Promise that is still pending, so we cannot immediately use the fetched data.
- **Data Access Issues:** The variable that is supposed to hold the fetched data may be empty or not contain the data yet, leading to errors or unintended behavior in the application.

## 3. Why Use the `@csrf_exempt` Decorator on a View for AJAX POST Requests

CSRF (Cross-Site Request Forgery) is a security mechanism in Django that ensures POST requests come from a legitimate source. However, when using AJAX POST, these requests often do not automatically carry the CSRF token, which can trigger CSRF validation failures.

The `@csrf_exempt` decorator is used to disable CSRF checks on a specific view. This is useful in the following situations:

- **Requests from a trusted source:** For example, if the AJAX request comes from a part of the application that can only be accessed by verified users.
- **Preventing request failure:** Without this decorator, AJAX POST requests without a CSRF token will be rejected by Django.

However, it is important to use this decorator carefully as it disables an important security mechanism. Make sure to maintain security by ensuring that only safe requests can reach this view.

## 4. Reasons Why Input Data Cleansing is Done in the Backend, Not Just in the Frontend

Input data cleansing in the backend is still necessary even though validation has been performed in the frontend for several important reasons:

- **Security:** Frontend validation and data cleansing can be bypassed by users who manipulate requests using tools like Postman or by disabling JavaScript. The backend is a safer place to verify input data.
- **Data Integrity:** The backend is responsible for ensuring that all data entering the system complies with the predefined rules. If we rely solely on frontend validation, invalid data could still enter the database.
- **Handling Attacks:** Attacks such as injections (e.g., SQL injection or XSS) can occur if data is not properly sanitized in the backend. Input validation and cleansing in the backend are crucial to preventing such exploits.

## 5. How to Implement Checklist

1. Create our ajax function `views.py`
```
@csrf_exempt
@require_POST
def add_item_entry_ajax(request):
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        user = request.user

    
        if name and price and desc:
            new_item = ItemEntry(
                name=name, 
                price=price,
                desc=desc,
                user=user
            )
            new_item.save()

            return HttpResponse(status=201)
        else:
            return HttpResponse('Missing fields', status=400)
```
3. Implement urls and routing in `urls.py` in `main` directory
```
from main.views import show_main, create_item_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_item, delete_item, add_item_entry_ajax

...

urlpatterns = [
    ...
    path('add-item-entry-ajax/', add_item_entry_ajax, name='add_item_entry_ajax'),
]
```
5. Create JS Script to retrieve data using AJAX GET,add to database using AJAX POST, and post it to the website when done
```
function addItemEntry() {
    const form = document.querySelector('#ItemEntryForm'); // Define the form variable
    const formItems = new FormData(form);

    fetch("{% url 'main:add_item_entry_ajax' %}", {
      method: "POST",
      body: formItems,
    })
    .then(response => {
      if (response.ok) {
        refreshItemEntries();
        form.reset();
      } else {
        alert('Failed to add item.');
      }
    })
    .catch(error => {
      console.error('Error:', error);
      alert('An error occurred.');
    });

    return false;
  }

  async function getItemEntries() {
    return fetch("{% url 'main:show_json' %}").then((res) => res.json());
  }

  async function refreshItemEntries() {
    document.getElementById("item_entry_cards").innerHTML = "";
    document.getElementById("item_entry_cards").className = "";
    const itemEntries = await getItemEntries();
    let htmlString = "";
    let classNameString = "";

    if (itemEntries.length === 0) {
      classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
      htmlString = `
        <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
          <img src="{% static 'image/very-sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
          <p class="text-center text-gray-600 mt-4">No items in your shop yet :(</p>
        </div>
      `;
    } else {
      classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full";
      itemEntries.forEach((item) => {
        htmlString += `
          <div class="relative break-inside-avoid">
            <div class="relative top-5 bg-indigo-100 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-indigo-300 transform rotate-1 hover:rotate-0 transition-transform duration-300">
              <div class="bg-indigo-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-indigo-300">
                <h3 class="font-bold text-xl mb-2">${item.fields.name}</h3>
              </div>
              <div class="p-4">
                <p class="font-semibold text-lg mb-2">Price</p>
                <p class="text-gray-700 mb-2">
                  <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">${item.fields.price}</span>
                </p>
                <div class="mt-4">
                  <p class="text-gray-700 font-semibold mb-2">Description</p>
                  <p class="text-gray-700 mb-2">
                    <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">${item.fields.desc}</span>
                  </p>
                </div>
              </div>
            </div>
            <div class="absolute top-0 -right-4 flex space-x-1">
              <a href="/edit-item/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                </svg>
              </a>
              <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                </svg>
              </a>
            </div>
          </div>
        `;
      });
    }
    document.getElementById("item_entry_cards").className = classNameString;
    document.getElementById("item_entry_cards").innerHTML = htmlString;
  }

  function showModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modal.classList.remove('hidden'); 
    setTimeout(() => {
      modalContent.classList.remove('opacity-0', 'scale-95');
      modalContent.classList.add('opacity-100', 'scale-100');
    }, 50); 
  }

  function hideModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modalContent.classList.remove('opacity-100', 'scale-100');
    modalContent.classList.add('opacity-0', 'scale-95');

    setTimeout(() => {
      modal.classList.add('hidden');
    }, 150); 
  }

  document.getElementById("cancelButton").addEventListener("click", hideModal);
  document.getElementById("closeModalBtn").addEventListener("click", hideModal);
  refreshItemEntries();
  document.getElementById("ItemEntryForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addItemEntry();
    hideModal();
  });
</script>
```

</details>

<details>

<summary> Assignment 5
</summary>

## 1. Priority Order of CSS Selectors

Inline Style: Inline styles have the highest specificity since they are applied directly to the HTML element.
ID Selector: ID selectors are more specific than classes and element selectors.
Class, Pseudo Class, and Attribute Selectors: These have lower specificity than IDs but higher than element selectors.
Element Selector and Pseudo-Elements: These hold the lowest level of specificity.

## 2. Why Is Responsive Design Important in Web Application Development? 
Responsive design reduces data load and simplifies code by eliminating the need to create device-specific versions of a site. Its main goal is to ensure that web applications provide the best possible viewing and interaction experience across all devices.

Applications with Responsive Design:
GitHub: Provides a uniform experience on all devices.
Dropbox: Adapts its layout based on the device, offering a seamless experience across platforms. The mobile app simplifies tasks, while the desktop version enhances Windows Explorer, macOS Finder, and taskbar functionalities.

Applications without Responsive Design:
Older Government Websites: Some older local government portals lack responsive design, resulting in small text, misaligned elements, and non-functional features on mobile devices.
Legacy Corporate Portals: Some older intranet or corporate systems were designed exclusively for desktops, and without responsive updates, mobile users face issues like excessive zooming and scrolling.

## 3. Differences Between Margin, Border, and Padding

Margin: The space outside the element's border, used to clear an area around the element.
Border: A visible line around the padding and content of an element.
Padding: The space between the element’s content and its border.
How to Implement Them:
```
Margin:
css
Copy code
.element {
  margin: 20px;
}
.element {
  margin-top: 5px;
  margin-right: 10px;
  margin-bottom: 20px;
  margin-left: 30px;
}
Border:
css
Copy code
.element {
  border: 5px solid;
}
.element {
  border-top: 5px red;
  border-right: 5px green;
  border-bottom: 5px blue;
  border-left: 5px red;
}
Padding:
css
Copy code
.element {
  padding: 40px;
}
.element {
  padding-top: 15px;
  padding-right: 20px;
  padding-bottom: 25px;
  padding-left: 35px;
}
```
## 4. Concepts of Flexbox and Grid Layout

Flexbox: Flexbox allows for precise control over the alignment and distribution of space between items, working in one dimension (either row or column).
Uses:
Navigation Bars: Flexbox is often used to evenly space or center navigation items.
Responsive Layouts: Flexbox is effective for rearranging elements as screen sizes change, enhancing responsive design.
Grid: The grid system supports two-dimensional layouts, handling both rows and columns simultaneously, allowing for more complex designs.
Uses:
Dashboards: Ideal for organizing charts, tables, and widgets in a structured format.
Complex Page Layouts: Useful for building full web pages that require both rows and columns for content organization.
How I Implemented the Checklist

## 5. This section explains the step-by-step approach for implementing the features discussed in the assignment.
### Implement functions to delete and edit products.
1. Create two new functions in views.py to delete and edit products:
```
def edit_item(request, id):
    item = ItemEntry.objects.get(pk = id)
    form = ItemEntryForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def delete_item(request, id):
    item = ItemEntry.objects.get(pk = id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
2. Add necessary dependent imports
```
from django.shortcuts import .., reverse
from django.http import .., HttpResponseRedirect
```
3. Add those two functions and their urls to views.py
```
from main.views import show_main, create_new_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_item, delete_item
urlpatterns = [
    ...
    path('edit-item/<uuid:id>', edit_item, name='edit_item'),
    path('delete/<uuid:id>', delete_item, name='delete_item'),
]
```
### Customize the design of the HTML templates that have been created in previous assignments using CSS or a CSS framework (such as Bootstrap, Tailwind, Bulma) with the following conditions:
1. Create a folder called `static`in the root directory with two other folders called `images` and `css`. This will be where we put our necessary images and designs.
2. Modified `base.html` to reference TailWindCSS and using whitenoise.
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
  </head>
  <body>
    {% block content %} {% endblock content %}
  </body>
</html>

# THIS IS IN SETTINGS.PY
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ....

# THIS IS TO DEAL WITH STATIC
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static' # refers to /static root project in development mode
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static' 
```
3. Add any needed images to images. Create a css file called `global.css`. Here is a short snippet.
```
.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
}
.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
...
```
4. Using inline CSS, customized all html pages made from previous assignment.


### Create a navigation bar (navbar) for the features in the application that is responsive to different device sizes, especially mobile and desktop.
1. Created `navbar.html` in `templates` in root driectory. Here is a short snippet:
   ```
<nav class="bg-rose-800 shadow-lg fixed top-0 left-0 z-40 w-screen">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
    ...
   ```
      </details>

<details>
  
<summary>
  Assignment 4
</summary>

## 1. Differences between HttpResponseRedirect() and redirect() 
* HttpResponseRedirect():
A built-in Django class that returns an HTTP 302 response to redirect to a specific URL.Typically used when we want more control and modification on the response before returning it (e.g., adding cookies or values into the website’s local storage).
* redirect():
A Django shortcut function that implicitly uses HttpResponseRedirect().
redirect() is more convenient because it can accept various parameters (URL, named URL patterns, model instances, etc.) and is more concise in syntax.


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

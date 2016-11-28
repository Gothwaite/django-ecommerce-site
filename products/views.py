from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.template import Template, Context
from django.http import HttpResponse
from models import Products,Orders
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
import datetime

def index(request):
    loggedouttext = "Log Out"
    logged_in = "Logged in as "
    if not request.user.is_authenticated():
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        logged_in = "<a href='/login_or_create'>Login or Create An Account</a>"
        loggedouttext = ''
    else:
        logged_in+=request.user.username
    table = ''
    for item in Products.objects.all():
        price = item.price
        name = item.name
        quantity = item.quantity
        image = item.image
        product_id = item.id
        row = '<tr><td><img src="/static/products/' + image + '.jpg" alt="My image" height="150" width="200"/></td><td><a href="/product_page/'+ name + '">' + name + '</a></td><td>$' + price + '</td><td>' + quantity + '</td></tr>'
        table+=row
    fp = open('/home/gstamand/django_server/webstoredir/index.html')
    t = Template(fp.read())
    html = t.render(Context({'price': table, 'logged_in': logged_in, 'loggedouttext': loggedouttext}))
    return HttpResponse(html)

def product_page(request, name):
    if not request.user.is_authenticated():
        return redirect('/login_or_create/')
    unslug = name.replace('-', ' ')
    tag = Products.objects.get(name=unslug)
    fp = open('/home/gstamand/django_server/webstoredir/product_page.html')
    t = Template(fp.read())
    html = t.render(Context({'max_quantity': tag.quantity, 'price': tag.price, 'name': tag.name, 'image': tag.image}))
    return HttpResponse(html)

def place_order(request):
    productname = request.GET['name']
    old_quantity = Products.objects.get(name=productname)
    new_quantity = int(old_quantity.quantity) - int(request.GET['quantity'])
    old_quantity.quantity = new_quantity
    old_quantity.save()
    fullname = request.user.first_name + " " + request.user.last_name
    dbentry = Orders(product_name=productname, full_name=fullname, address=request.GET['address'], state=request.GET['state'], zipcode=request.GET['zipcode'], quantity=request.GET['quantity'], total=float(request.GET['quantity'])*float(old_quantity.price), ccnumber=request.GET['ccnumber'], ccexpiration=request.GET['ccexpiration'], city=request.GET['city'])
    dbentry.save()
    fp = open('/home/gstamand/django_server/webstoredir/order_placed.html')
    t = Template(fp.read())
    html = t.render(Context())
    return HttpResponse(html)
def login_or_create(request):
    fp = open('/home/gstamand/django_server/webstoredir/login.html')
    t = Template(fp.read())
    html = t.render(Context())
    return HttpResponse(html)
def login_usr(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            message = "Logged In"
            return popup(request, message)     
           
    else:
        message = "Invalid Credentials"
        return popup(request, message) 
def create_account(request):
    fp = open('/home/gstamand/django_server/webstoredir/create_account.html')
    t = Template(fp.read())
    html = t.render(Context())
    return HttpResponse(html)       
   
def create_usr(request):
    username = request.GET['username']
    password = request.GET['password']
    first_name = request.GET['first_name']
    last_name = request.GET['last_name']
    email = request.GET['email']
    user = User.objects.create_user(username, email, password)
    user.save()
    user.last_name = last_name
    user.first_name = first_name
    user.save()
    user = authenticate(username=username, password=password)
    login(request, user)
    request.session.set_expiry(1209600) # 2 weeks
    message = "Account created"
    return popup(request, message) 
def logout_view(request):
    logout(request)
    message = "Logged Out"
    return popup(request, message)      
def popup(request, message):
    display = message
    fp = open('/home/gstamand/django_server/webstoredir/logged_in.html')
    t = Template(fp.read())
    html = t.render(Context({'message': display}))
    return HttpResponse(html)



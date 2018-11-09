# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import People

# Create your views here.


def test(request):

    context = {'name': 'John'}
    template = 'test.html'
    return render(request, template, context)
    #return HttpResponse("<h1>Hello World!</h1> <h2> Hi guys, how are you? </h2>")


def test2(request):

    # Add a record to the database
    p = People(first_name = "John", last_name = "Doe", age = 22)
    p.save()

    # Get the first row in the database and assign to a variable called u
    u = People.objects.first()
    # Print the values in html directly
    return HttpResponse("firstname = %s, lastname = %s, age=%s" %(u.first_name, u.last_name, u.age))

def test3(request):

    # Get the first row in the database and assign to a variable called u
    u = People.objects.first()

    # Pass the object u to test2.html in which the fields of u (e.g., first_name, last_name and age) can be displayed
    context = {"person": u}
    template = 'test2.html'
    return render(request, template, context)

def viewRegister(request):
    # View the register page
    return render(request, 'register.html')


def index(request):
    # get the all people in the db and reverse order so that the last record appears first
    allPeople = People.objects.order_by('-id')

    # send allPeople object to the html where the fields of u (e.g., first_name, last_name and age) can be displayed
    context = {'people': allPeople}
    template = 'index.html'
    return render(request, template, context)

def addUser(request):

    # First check whether the form was sent through a post method
    # if so, then get the values
    if request.method == 'POST':

        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        age = request.POST.get("age")

        # Add a record to the database
        p = People(first_name = firstName, last_name = lastName, age = age)
        p.save()

        return redirect('index')
    else:
        return HttpResponse("Something went wrong!")

def deleteUser(request):
    People.objects.first().delete()
    return redirect('index')
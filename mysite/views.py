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

    # Get the first row in the database and assign it to a variable called u
    u = People.objects.first()
    # Print the values
    return HttpResponse("firstname = %s, lastname = %s, age=%s" %(u.first_name, u.last_name, u.age))

def test3(request):

    # Get the first row in the database and assign it to a variable called u
    u = People.objects.first()

    # Pass the object u to test2.html in which the fields of u (e.g., first_name, last_name and age) can be displayed
    context = {"person": u}
    template = 'test2.html'
    return render(request, template, context)


def index(request):
    # get all the records in the people table in db, and then reverse order them so that the last record appears first
    allPeople = People.objects.order_by('-id')

    # send allPeople object to the index.html where the fields of u (first_name, last_name and age) can be displayed
    context = {'people': allPeople}
    template = 'index.html'
    return render(request, template, context)

def viewRegister(request):
    # View the register page
    return render(request, 'register.html')


def addUser(request):

    # First check if the form has been sent by a post method
    # if so, then get the values
    if request.method == 'POST':

        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        age = request.POST.get("age")

        # Add a new record into the database
        p = People(first_name = firstName, last_name = lastName, age = age)
        p.save()
        # Redirect to the index.html
        return redirect('index')
    else:
        return HttpResponse("Something went wrong!")

def deleteUser(request):
    # Delete the first record in the db and then redirect to the index.html
    People.objects.first().delete()
    return redirect('index')
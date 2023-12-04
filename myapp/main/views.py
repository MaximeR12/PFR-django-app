
import os

from django import template
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from dotenv import load_dotenv
#load_dotenv()

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

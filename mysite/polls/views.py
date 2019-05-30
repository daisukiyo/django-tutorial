# combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text
from django.shortcuts import render
# each view you write is responsible for instantiating, populating, and returning an HttpResponse
from django.http import HttpResponse

# create index view
def index(request):
    return HttpResponse("Hello world. You're at the polls index.")

from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse
from .aiml_mod import qa_core

def search_post(request):

    result = ""

    if request.POST:
        question = request.POST['query']
        result = qa_core.query_function(question)
        print(result)

    template = loader.get_template('index.html')
    context = {
        'result': result,
    }

    return HttpResponse(template.render(context,request))

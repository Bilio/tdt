from django.http import HttpResponse
from django.template import loader
import os
import config

# Create your views here.
def index(request):
    template = loader.get_template("corpusconstruct/index.html")
    return HttpResponse(template.render(request))

def view_corpus(request):
    dir_list = os.walk(config.CORPUS_DATA_DIR)
    dir_list = map(lambda x: x[0].split(os.sep)[-1], list(dir_list))[1:]
    context = {'topic_list': dir_list}
    template = loader.get_template("corpusconstruct/topiclist.html")
    return HttpResponse(template.render(context, request))

def add_topic(request):
    return HttpResponse("Yet to implement")

def add_docs(request):
    return HttpResponse("Yet to implement")
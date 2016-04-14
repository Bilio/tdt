from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
import os
import config
from forms import TopicForm

# Create your views here.
def index(request):
    template = loader.get_template("corpusconstruct/index.html")
    return HttpResponse(template.render(request))

def view_corpus(request):
    dir_list = os.walk(config.TDT_CORPUS_DIR)
    dir_list = map(lambda x: x[0].split(os.sep)[-1].replace('_', ' '), list(dir_list))[1:]
    context = {'topic_list': dir_list}
    template = loader.get_template("corpusconstruct/topiclist.html")
    return HttpResponse(template.render(context, request))

def add_topic(request):
    form = TopicForm()
    template = loader.get_template("corpusconstruct/addnewtopic.html")
    return render(request, "corpusconstruct/addnewtopic.html", {'form':form})

def addtopic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic_name']
            topic = topic.replace(' ', '_')
            if not os.path.exists(os.path.join(config.TDT_CORPUS_DIR, topic)):
                os.mkdir(os.path.abspath(os.path.join(config.TDT_CORPUS_DIR, topic)))
            return HttpResponseRedirect('../view/')
    else:
        form = TopicForm()
    return render(request, "corpusconstruct/addnewtopic.html", {'form':form})


def add_docs(request):
    template = loader.get_template("corpusconstruct/adddocstotopic.html")
    return HttpResponse(template.render(request))
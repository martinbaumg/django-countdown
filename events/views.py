from django.shortcuts import render
from .forms import EventForm
from .models import Event
from django.shortcuts import redirect, HttpResponseRedirect

# Create your views here.


def index(request):
    event = Event.objects.all()
    return render(request, 'index.html', {'event': event})


def addevent(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/allevents")
    else:
        form = EventForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'addevent.html', {'form': form})

def deleteevent(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect('/allevents')

def showevent(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'showevent.html', {'event': event})

def editevent(request, id):
    event = Event.objects.get(id=id)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = EventForm(instance=event)
    return render(request, 'editevent.html', {'form': form})

def allevents(request):
    event = Event.objects.all()
    return render(request, 'allevents.html', {'event': event})

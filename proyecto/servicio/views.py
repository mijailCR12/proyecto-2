from django.shortcuts import render, redirect
from .forms import ServicioForm
from .models import Servicio

# Create your views here.


def servicio_list(request):
    context = {'servicio_list': Servicio.objects.all()}
    return render(request, "servicio/servicio_list.html", context)


def servicio_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ServicioForm()
        else:
            servicio = Servicio.objects.get(pk=id)
            form = ServicioForm(instance=servicio)
        return render(request, "servicio/servicio_form.html", {'form': form})
    else:
        if id == 0:
            form = ServicioForm(request.POST)
        else:
            servicio = Servicio.objects.get(pk=id)
            form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
        return redirect('/servicio/list')


def servicio_delete(request, id):
    servicio = Servicio.objects.get(pk=id)
    servicio.delete()
    return redirect('/servicio/list')

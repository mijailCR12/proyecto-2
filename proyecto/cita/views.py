from django.shortcuts import render, redirect
from .forms import ClienteForm, EmpleadoForm, ServicioForm
from .models import Cliente, Empleado, Servicio
# Create your views here.

# cliente


def cliente_list(request):
    context = {'cliente_list': Cliente.objects.all()}
    return render(request, "cliente/cliente_list.html", context)


def cliente_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ClienteForm()
        else:
            cliente = Cliente.objects.get(pk=id)
            form = ClienteForm(instance=cliente)
        return render(request, "cliente/cliente_form.html", {'form': form})
    else:
        if id == 0:
            form = ClienteForm(request.POST)
        else:
            cliente = Cliente.objects.get(pk=id)
            form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
        return redirect('/cliente/list')


def cliente_delete(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()
    return redirect('/cliente/list')


# empleado
def empleado_list(request):
    context = {'empleado_list': Empleado.objects.all()}
    return render(request, "empleado/empleado_list.html", context)


def empleado_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmpleadoForm()
        else:
            empleado = Empleado.objects.get(pk=id)
            form = EmpleadoForm(instance=empleado)
        return render(request, "empleado/empleado_form.html", {'form': form})
    else:
        if id == 0:
            form = EmpleadoForm(request.POST)
        else:
            empleado = Empleado.objects.get(pk=id)
            form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
        return redirect('/empleado/list')


def empleado_delete(request, id):
    empleado = Empleado.objects.get(pk=id)
    empleado.delete()
    return redirect('/empleado/list')

# servicio


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

from django.shortcuts import render, redirect
from .forms import ClienteForm, EmpleadoForm, ServicioForm, CitaForm
from .models import Cliente, Empleado, Servicio, Cita
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
# ...


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login/login.html", {'form': form})


def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "index/home.html")
    # En otro caso redireccionamos al login
    return redirect('/login')


def registro(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login/registro.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/login')
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

# cita


def cita_list(request):
    context = {'cita_list': Cita.objects.all()}
    return render(request, "cita/cita_list.html", context)


def cita_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CitaForm()
        else:
            cita = Cita.objects.get(pk=id)
            form = CitaForm(instance=cita)
        return render(request, "cita/cita_form.html", {'form': form})
    else:
        if id == 0:
            form = CitaForm(request.POST)
        else:
            cita = Cita.objects.get(pk=id)
            form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
        return redirect('/cita/list')


def cita_delete(request, id):
    cita = Cita.objects.get(pk=id)
    cita.delete()
    return redirect('/cita/list')

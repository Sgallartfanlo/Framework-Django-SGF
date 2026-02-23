from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Jugador, Titol
from .forms import FormulariJugador

# Llistar jugadors
def llista_jugadors(request):
    jugadors = Jugador.objects.all()
    return render(request, 'llista_jugadors.html', {'jugadors': jugadors})

# Afegir jugador
def afegir_jugador(request):
    if request.method == 'POST':
        form = FormulariJugador(request.POST)
        if form.is_valid():
            form.save()
            return redirect('llista_jugadors')
    else:
        form = FormulariJugador()

    return render(request, 'afegir_jugador.html', {'form': form})

# Editar jugador
def editar_jugador(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    if request.method == 'POST':
        form = FormulariJugador(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('llista_jugadors')
    else:
        form = FormulariJugador(instance=jugador)

    return render(request, 'afegir_jugador.html', {'form': form})

# Eliminar jugador
def eliminar_jugador(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    jugador.delete()
    return redirect('llista_jugadors')

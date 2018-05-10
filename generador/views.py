from django.shortcuts import render
from django.views.generic import ListView  # Vista generica de Objetos
from .forms import VariableL1ModelForm, VariableL2ModelForm
from .models import VariableLote1, VariableLote2
import random


def inicio(request):
    return render(request, "base.html", {})


def generadorLote1(request):
    minLote, maxLote = 0.333333, 0.397766
    r = round(random.random(), 6)
    x = round(round(maxLote - minLote, 6) * r + minLote, 6)

    form = VariableL1ModelForm(initial={'valor': x}, auto_id=False)

    context = {
        "elform": form,
        "title": "Lote 1 - 'Tiempo de Arribo'",
        "minymax": "Minimo: 0.333333 - Maximo: 0.397766",
    }

    if request.POST:
        formPost = VariableL1ModelForm(request.POST or None)

        if formPost.is_valid():
            valido = formPost.save(commit=False)
            valido.valor = x
            valido = formPost.save()
            print("Valor generado para el lote1: {}".format(x))
        else:
            print("error")

    return render(request, "lote.html", context)


def generadorLote2(request):
    minLote, maxLote = 0.003519, 0.008310

    r = round(random.random(), 6)
    x = round(round(maxLote - minLote, 6) * r + minLote, 6)

    form = VariableL2ModelForm(initial={'valor': x}, auto_id=False)

    context = {
        "elform": form,
        "title": "Lote 2 - 'Tiempo de Atencion'",
        "minymax": "Minimo: 0.003519 - Maximo: 0.008310",
    }

    if request.POST:
        formPost = VariableL2ModelForm(request.POST or None)

        if formPost.is_valid():
            valido = formPost.save(commit=False)
            valido.valor = x
            valido = formPost.save()
            print("Valor generado para el lote 2: {}".format(x))
        else:
            print("error")

    return render(request, "lote.html", context)


class HistorialLote1(ListView):
    model = VariableLote1
    # el template variablelote1_list.html


class HistorialLote2(ListView):
    model = VariableLote2
    # el template variablelote2_list.html

from django.db.models import Model
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cuber
from .forms import CuberForm

# Create your views here.

def cuber_list(request: HttpRequest):
    cubers = Cuber.objects.all()

    if request.method == 'POST':
        form = CuberForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cuber_list')

    else:
        form = CuberForm()
    
    return render(
        request,
        'cubers/cuber-list.html',
        {
            'cubers': cubers,
            'form': form
        }
    )

def cuber_edit(request: HttpRequest, cuber_id):

    cuber = get_object_or_404(Cuber, id=cuber_id)

    if request.method == 'POST':
        form = CuberForm(request.POST, instance=cuber)

        if form.is_valid():
            form.save()
            return redirect('cuber_list')

    else:
        form = CuberForm(instance=cuber)

    return render(
        request,
        'cubers/cuber-edit.html',
        {'form': form,
                'cuber': cuber}
    )

def cuber_delete(request: HttpRequest, cuber_id):

    cuber = get_object_or_404(Cuber, id=cuber_id)

    if request.method == 'POST':
        cuber.delete()
        return redirect('cuber_list')

    return render(
        request,
        'cubers/cuber-delete.html',
        {'cuber': cuber},
    )
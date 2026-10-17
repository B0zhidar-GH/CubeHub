from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CubeForm
from .models import Cube

# Create your views here.

'''def cube_list(request: HttpRequest):
    cubes = Cube.objects.all()

    return render(
        request,
        'cubes/cube-list.html',
        {'cubes': cubes}
    )'''

def cube_list(request: HttpRequest):
    cubes = Cube.objects.all()

    if request.method == 'POST':
        form = CubeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cube_list')

    else:
        form = CubeForm()

    return render(
        request,
        'cubes/cube-list.html',
        context= {
            'cubes': cubes,
            'form': form
        }
    )

def cube_edit(request: HttpRequest, cube_id):

    cube = get_object_or_404(Cube, id=cube_id)

    if request.method == 'POST':
        form = CubeForm(request.POST, instance=cube)

        if form.is_valid():
            form.save()
            return redirect('cube_list')

    else:
        form = CubeForm(instance=cube)

    return render(
        request,
        'cubes/cube-edit.html',
        {'form': form,
         'cube': cube}
    )

def cube_delete(request: HttpRequest, cube_id):

    cube = get_object_or_404(Cube, id=cube_id)

    if request.method == 'POST':
        cube.delete()
        return redirect('cube_list')

    return render(
        request,
        'cubes/cube-delete.html',
        {'cube': cube},
    )
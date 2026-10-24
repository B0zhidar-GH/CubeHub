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

    chosen_filter_1 = request.GET.get('cube', '')
    chosen_filter_2 = request.GET.get('category_event', '')
    chosen_filter_3 = request.GET.get( 'brand', '')
    chosen_filter_4 = request.GET.get('owner', '')

    #chosen_sort = request.GET.get('sort', 'owners__first_name')

    if chosen_filter_1:
        cubes = cubes.filter(cube=chosen_filter_1)
    if chosen_filter_2:
        cubes = cubes.filter(category_event=chosen_filter_2)
    if chosen_filter_3:
        cubes = cubes.filter(brand=chosen_filter_3)
    #if chosen_filter_4:
        #cubes = cubes.filter(owners=chosen_filter_4)

    #sorts_allowed = ['owners__first_name', '-owners__first_name']

    #if chosen_sort in sorts_allowed:
        #cubes = cubes.order_by(chosen_sort)

    cubes_type = Cube.CubeChoices.choices
    category_event_type = Cube.CategoryEvent.choices

    brand_type = (
        Cube.objects
        .values_list('brand', flat=True)
        .distinct()
        .order_by('brand')
    )

    return render(
        request,
        'cubes/cube-list.html',
        context= {
            'cubes': cubes,
            'cube': chosen_filter_1,
            'category_event': chosen_filter_2,
            'brand': chosen_filter_3,
            'cubes_type': cubes_type,
            'category_event_type': category_event_type,
            'brand_type': brand_type,
            #'owners': chosen_filter_4,
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
        form = CubeForm(
            instance=cube,
            initial={
                'registration_date': cube.date_of_registration
            })



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

def cube_details(request: HttpRequest, cube_id):

    cube = get_object_or_404(Cube, id=cube_id)

    return render(
        request,
        'cubes/cube-details.html',
        {'cube': cube}
    )
from django.db.models import Model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from cubers.models import Cuber
from cubes.models import Cube
from solves.forms import SolveForm
from solves.models import Solve


# Create your views here.

def solve_list(request: HttpRequest):



    solves = Solve.objects.all()

    if request.method == 'POST':
        form = SolveForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('solve_list')
    else:
        form = SolveForm()

    chosen_filter1 = request.GET.get('cube', '')
    chosen_filter2 = request.GET.get('cuber', '')
    chosen_filter3 = request.GET.get('scramble', '').strip()

    chosen_sort = request.GET.get('sort', 'time')

    sorts_allowed = ['time', '-time']

    if chosen_filter1:
        solves = solves.filter(cube=chosen_filter1)
    if chosen_filter2:
        solves = solves.filter(cuber=chosen_filter2)
    if chosen_filter3:
        solves = solves.filter(scramble__icontains=chosen_filter3)

    cubes_type = Cube.objects.all()
    cubers_type = Cuber.objects.all()

    if chosen_sort in sorts_allowed:
        solves = solves.order_by(chosen_sort)


    return render(
        request,
        'solves/solve-list.html',
        {
            'solves': solves,
            'cube': chosen_filter1,
            'cuber': chosen_filter2,
            'scramble': chosen_filter3,
            'cubes_type': cubes_type,
            'cubers_type': cubers_type,
            'chosen_sort': chosen_sort,
            #'scramble_type':
            'form': form,

         },
    )


def solve_edit(request: HttpRequest, solve_id):
    solve = get_object_or_404(Solve, id=solve_id)

    if request.method == "POST":
        form = SolveForm(request.POST, instance=solve)

        if form.is_valid():
            form.save()
            return redirect("solve_list")
    else:
        form = SolveForm(
            instance=solve,
            initial={
                'registration_date': solve.date_created
            }
        )

    return render(
        request,
        "solves/solve-edit.html",
        {"form": form, "solve": solve},
    )


def solve_delete(request: HttpRequest, solve_id):
    solve = get_object_or_404(Solve, id=solve_id)

    if request.method == 'POST':
        solve.delete()
        return redirect('solve_list')

    return render(
        request,
        'solves/solve-delete.html',
        {'solve': solve},
    )

def solve_details(request: HttpRequest, solve_id):
     solve = get_object_or_404(Solve, id=solve_id)

     return render(
         request,
         'solves/solve-details.html',
         {'solve': solve}
     )
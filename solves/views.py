from django.db.models import Model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from solves.forms import SolveForm
from solves.models import Solve


# Create your views here.

def solve_list(request: HttpRequest):

    if request.method == 'POST':
        form = SolveForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('solve_list')
    else:
        form = SolveForm()

    solves = Solve.objects.all()

    return render(
        request,
        'solves/solve-list.html',
        {
            'solves': solves,
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
        form = SolveForm(instance=solve)

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
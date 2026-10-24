from django.db.models import Model
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request

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
        form = CuberForm(

        )


    country_filter = request.GET.get('country', '')
    chosen_sort = request.GET.get('sort', 'first_name')

    if country_filter:
        cubers = cubers.filter(country=country_filter)

    sorts_allowed = ['first_name', 'last_name', '-first_name', '-last_name']

    if chosen_sort in sorts_allowed:
        cubers = cubers.order_by(chosen_sort)

    countries = (
        Cuber.objects
        .values_list('country', flat=True)
        .distinct()
        .order_by('country')
    )

    return render(
        request,
        'cubers/cuber-list.html',
        {
            'cubers': cubers,
            'countries': countries,
            'selected_country': country_filter,
            'selected_sort': chosen_sort,
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
        form = CuberForm(
            instance=cuber,
            initial={
                'registration_date': cuber.date_of_registration
            }
        )

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

def cuber_details(request: HttpRequest, cuber_id):

    cuber = get_object_or_404(Cuber, id=cuber_id)


    '''if request.method == 'POST':
        form = CuberForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cuber_list')

    else:
        form = CuberForm()'''

    return render(
        request,
        'cubers/cuber-details.html',
        {'cuber': cuber}
    )
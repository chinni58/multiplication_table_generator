# tablegen/views.py
from django.shortcuts import render
from .forms import TableForm

def index(request):
    result = None
    form = TableForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        base = form.cleaned_data['base']
        start = form.cleaned_data['start']
        end = form.cleaned_data['end']
        step = form.cleaned_data['step']

        # create a list of multipliers in intuitive order
        if start <= end:
            multipliers = list(range(start, end + 1, step))
        else:
            # descending sequence when start > end
            multipliers = list(range(start, end - 1, -abs(step)))

        # prepare results as list of tuples (multiplier, product)
        result = [(m, base * m) for m in multipliers]

    context = {
        'form': form,
        'result': result,
    }
    return render(request, 'tablegen/index.html', context)


# Create your views here.

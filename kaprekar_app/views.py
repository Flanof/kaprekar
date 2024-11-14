from django.shortcuts import render

def kaprekar_step(n):
    n_str = f"{n:04d}"
    asc = int("".join(sorted(n_str)))
    desc = int("".join(sorted(n_str, reverse=True)))
    return desc - asc

def kaprekar_routine(n):
    steps = []
    while n != 6174 and len(steps) < 10:  # Limita a 10 pasos por si acaso
        n = kaprekar_step(n)
        steps.append(n)
    return steps

def kaprekar_view(request):
    result = None
    steps = []

    if request.method == 'POST':
        number = request.POST.get('number')
        if number.isdigit() and len(number) == 4:
            number = int(number)
            steps = kaprekar_routine(number)
            result = steps[-1] == 6174  # Verificar si se llegó a 6174

    return render(request, 'index.html', {'result': result, 'steps': steps})



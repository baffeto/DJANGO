from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def omlet(request):
    context = {
        'recipe': {}
    }
    
    serving = int(request.GET.get("serving", 1))
    
    for dish, ingredients in DATA.items():
        if dish == 'omlet':
            context['recipe'][dish] = {}
            for ingredient, amount in ingredients.items():
                context['recipe'][dish][ingredient] = amount * serving
            
    return render(request=request, template_name='dish.html', context=context)

def pasta(request):
    context = {
        'recipe': {}
    }
    
    serving = int(request.GET.get("serving", 1))
    
    for dish, ingredients in DATA.items():
        if dish == 'pasta':
            context['recipe'][dish] = {}
            for ingredient, amount in ingredients.items():
                context['recipe'][dish][ingredient] = amount * serving
            
    return render(request=request, template_name='dish.html', context=context)

def buter(request):
    context = {
        'recipe': {}
    }
    
    serving = int(request.GET.get("serving", 1))
    
    for dish, ingredients in DATA.items():
        if dish == 'buter':
            context['recipe'][dish] = {}
            for ingredient, amount in ingredients.items():
                context['recipe'][dish][ingredient] = amount * serving
            
    return render(request=request, template_name='dish.html', context=context)

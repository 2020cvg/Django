from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.
from .models import Meals , Category

def meal_list(request):
    meal_list = Meals.objects.all().order_by("id")  # Ensure ordering to avoid pagination issues
    categories = Category.objects.all()

    # Add Pagination: 5 meals per page
    paginator = Paginator(meal_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "categories": categories,
    }

    return render(request, "Meals/list.html", context)



def meal_detail(request , slug):
    meal_detail = Meals.objects.get(slug=slug)

    context = {'meal_detail' : meal_detail}

    return render(request , 'Meals/detail.html' , context)
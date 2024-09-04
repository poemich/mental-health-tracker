from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245011',
        'name': 'Muhammad Fadhlan Karimuddin',
        'class': 'PBP F'
    }
    return render(request, "main.html", context)
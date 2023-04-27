from django.shortcuts import render

from aboutus.models import AboutUs


# Create your views here.
def aboutus(request):
    dt = AboutUs.objects.all()
    context = {"dt": dt}
    return render(request, "aboutus/index.html", context)

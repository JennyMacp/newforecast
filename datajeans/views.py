from django.shortcuts import render
# from jual.forms import FormDataJual
# from jual.models import DataJual

# Create your views here.
def index(request):
    return render(request, 'datajeans/index.html')
from django.shortcuts import render
from app1.models import place
from app1.models import team
# Create your views here.
def home(request):
    p=place.objects.all()
    t=team.objects.all()
    return render(request,'base.html', {'p':p ,'t':t})
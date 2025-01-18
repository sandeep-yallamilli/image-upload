from django.shortcuts import render

from imageapp.forms import ImageForm
from imageapp.models import Image
# Create your views here.
def home(request):
    if request.method=='POST':
        form=ImageForm(request.POST, request.FILES)
        if form.is_valid():
         form.save()
    img=Image.objects.all()  
    form=ImageForm()
    return render(request, 'home.html',{'form':form,'img':img})
from django.shortcuts import render,redirect
from .forms import ReserveForm
# Create your views here.
def reservefood(request):
    form=ReserveForm()
    if request.method=='POST':
        form=ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ReserveForm()
    return render(request,'reserve/reserve.html',{'form':form})
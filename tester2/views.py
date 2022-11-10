from django.shortcuts import render
from tester2.forms import enroll 
# Create your views here.
def index(request):
    if request.method=='POST':
        form=enroll(request.POST)
        if form.is_vaild():
            form.save()
            return render(request,enroll.html,{'form':form,'msg':"enroll successful"})
    else:
        form=enroll()
        return render(request,enroll.html,{'form':form})
        
        

from django.shortcuts import render
from .formlay import temForm,studentForm
# Create your views here.
def formfild(request):
    fm=studentForm()
    return render(request,'formfild.html',{'stuform':fm})

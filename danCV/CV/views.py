from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.
def home(request):
    return render(request,'home.html')
def pdf_view(request):
    fs=FileSystemStorage()
    filename="data/Resume_Danella.pdf"
    if fs.exists(filename):
        with fs,open(filename)as pdf:
            response=HttpResponse(pdf,content_type="application/pdf")
            response['Content-Disposition']='attachment: filename="data/Danella_Resume.pdf" '
            return response
    else:
        return HttpResponseNotFound("The Request does not found ")

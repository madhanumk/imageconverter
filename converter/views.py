from django.shortcuts import render
import base64

# Create your views here.


def jpgtobase64(request):
    if request.method == "POST":
        imagefile = request.FILES.get('uploadimage')      
        base64string = base64.b64encode(imagefile.read())
        context = {
            'converted' : True,
            'base64' : base64string.decode("utf-8")
        }        
    else:
        context = {}
    return render(request, 'jpg/jpgtobase64.html',context)

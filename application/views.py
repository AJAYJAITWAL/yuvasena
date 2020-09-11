from django.shortcuts import render,HttpResponse
from application.models import Bio,Register


# Create your views here.
def application(request):
    return render(request, 'home.html')


def card(request):
   allPosts = Register.objects.all()[0]
   context = {'allPosts' : allPosts}
   return render(request, 'card.html', context)


def register(request):
    if request.method=='POST':
         name = request.POST['name']
         address = request.POST['address']
         wnumber = request.POST['wnumber']
         assembly = request.POST['assembly']
         phone = request.POST['phone']
         email = request.POST['email']
         dob = request.POST['dob']
         post = request.POST['post']
         Tenure = request.POST['Tenure']
         position = request.POST['position']
         bgroup = request.POST['bgroup']
         education = request.POST['education']
         pyear = request.POST['pyear']
         occupation = request.POST['occupation']
         anumber = request.POST['anumber']
         img = request.POST['img']
        
         contact = Register(name=name, address=address, wnumber=wnumber, assembly=assembly, phone=phone,  email=email, dob=dob, post=post,  Tenure=Tenure, position=position, bgroup=bgroup, education=education, pyear=pyear, occupation=occupation, anumber=anumber, img=img)
         
         contact.save()
           
             
    return render(request, 'register.html')
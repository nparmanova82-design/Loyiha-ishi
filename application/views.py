

from django.shortcuts import render,redirect,get_object_or_404
from . import models

# Create your views here.

def mma(request):
    user = models.Student.objects.all()
    return render(request, 'app/index.html',context={'user':user})

def user_view(request,slug):
    user = models.Student.objects.get(slug=slug)
    return render(request, 'app/user_view.html', {'user': user})
#create

def user_create(request):
    if request.POST:
        name=request.POST.get('name')
        surename=request.POST.get('surname')
        age=request.POST.get('age')
        picture=request.FILES.get('picture')


        models.Student.objects.create(
    name=name,
    surname=surename,
    age=age,
    picture=picture,
)
        return redirect('users_list')
    return render(request,'app/user_create.html')

#update
def user_update(request, slug):
    user = get_object_or_404(models.User, slug=slug)

    if request.method == "POST":
        user.ism = request.POST.get("name")
        user.familiya = request.POST.get("surname")

        yosh = request.POST.get("yosh")
        if yosh and yosh.isdigit():
            user.yosh = int(yosh)
            return redirect('users_list')
        return render(request, 'user_update.html',{'user':user})        


    if request.FILES.get('image'):
        user.picture = request.FILES.get('image')
        user.save()
        return redirect(f'/user/{user.slug}')
    #delete
    from django.shortcuts import get_object_or_404, redirect
    from . import models

def user_delete(request, slug):
    user = get_object_or_404(models.User, slug=slug)
    user.delete()
    return redirect()
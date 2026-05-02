from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Student
from .forms import StudentForm


#listview
class UserListView(ListView):
    model = Student
    template_name = 'app/index.html'
    context_object_name = 'users'


#userdetail
class UserDetailView(DetailView):
    model = Student
    template_name = 'app/user_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'



def user_create(request):
    form = StudentForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        user = form.save()
        return redirect('user_detail', slug=user.slug)

    return render(request, 'app/user_create.html', {'form': form})


def user_update(request, slug):
    user = get_object_or_404(Student, slug=slug)

    if request.method == "POST":
        user.name = request.POST.get("name")
        user.surname = request.POST.get("surname")
        user.age = request.POST.get("age")
        user.email = request.POST.get("email")

        if request.FILES.get('picture'):
            user.picture = request.FILES.get('picture')

        user.save()
        return redirect('user_detail', slug=user.slug)

    return render(request, 'app/user_update.html', {'user': user})



def user_delete(request, id):
    user = get_object_or_404(Student, id=id)

    if request.method == "POST":
        user.delete()
        return redirect('users_list')

    return render(request, 'app/user_delete.html', {'user': user})
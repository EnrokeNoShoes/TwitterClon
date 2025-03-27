from django.shortcuts import render, redirect
from .models import Profile, Post, Relationship
from .forms import UserRegisterForm, PostForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def home(request):


    followed_users = request.user.profile.following()  
    followed_users = followed_users | User.objects.filter(id=request.user.id) 

    posts = Post.objects.filter(user__in=followed_users).order_by('-timestamp')
    #posts = Post.objects.all()

    users_to_follow = User.objects.exclude(id=request.user.id).exclude(id__in=followed_users.values('id'))

    following_list = request.user.profile.following() 
    followers_list = request.user.profile.followers()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    context = {'posts':posts, 'form': form,'users_to_follow': users_to_follow,'following_list': following_list,
        'followers_list': followers_list,}
    return render(request, 'twitter/newsfeed.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el usuario
            # Crea el perfil automáticamente para el usuario recién creado
            Profile.objects.create(user=user)
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request , 'twitter/register.html', context)

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('home')

def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    context = {'user':user, 'posts':posts}
    return render(request, 'twitter/profile.html', context)

@login_required
def editprofile(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {'u_form' : u_form, 'p_form' : p_form}
    return render(request, 'twitter/editar.html', context)

@login_required
def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username = username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user = to_user_id)
    rel.save()
    return redirect('home')

@login_required
def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username = username)
    to_user_id = to_user.id
    rel = Relationship.objects.get(from_user=current_user.id, to_user = to_user_id)
    rel.delete()
    return redirect('home')


def search_users(request):
    query = request.GET.get('query', '')  # Obtener el valor de la búsqueda desde la URL
    users = User.objects.filter(username__icontains=query)  # Filtrar usuarios por nombre de usuario
    return render(request, 'twitter/search_results.html', {'users': users, 'query': query})


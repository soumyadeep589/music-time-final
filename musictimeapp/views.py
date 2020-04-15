from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from musictimeapp.models import Follow, Post, Studio
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()
from django.db.models import Count
from django.http import Http404
from musictimeapp.forms import StudioForm
from django.core.mail import send_mail
from django.conf import settings


from .forms import CustomUserCreationForm
# Create your views here.

@login_required(login_url='/')
def index(request):
    current_user = request.user
    User = get_user_model()
    user = User.objects.get(id=current_user.id)
    followings = Follow.objects.filter(follower=user)
    followings_arr = [user]
    for following in followings:
        followings_arr.append(following.followed)

    posts = Post.objects.filter(author__in=followings_arr)
    print(posts)
    return render(request, 'index.html', {'posts': posts})

@csrf_exempt
def add_post(request):
    current_user = request.user
    received_json_data = json.loads(request.body)
    User = get_user_model()
    user = User.objects.get(id=current_user.id)
    newpost = Post.objects.create(body=received_json_data['post_body'], author=user)
    newpost.save()
    # received_json_data['post_body']
    responseObj = {
        'status': "done",
        'post_body': received_json_data['post_body']
    }
    return JsonResponse(responseObj)

@login_required(login_url='/')
def user(request, username):
    current_user = request.user
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user)
    following_count = Follow.objects.filter(follower=user).annotate(count=Count('follower'))
    followers_count = Follow.objects.filter(followed=user).annotate(count=Count('followed'))
    print(following_count)
    is_following = False
    if(Follow.objects.filter(follower=current_user, followed=user).count() > 0):
        is_following = True
    return render(request, 'user.html', {'user': user, 'posts': posts, 'is_following': is_following, 'following_count': following_count, 'followers_count': followers_count})


def follow(request, username):
    current_user = request.user
    User = get_user_model()
    user1 = User.objects.get(username=username)
    print(user)
    follower = Follow(follower=current_user, followed=user1)
    follower.save()
    return redirect(user, username=username)


def unfollow(request, username):
    current_user = request.user
    User = get_user_model()
    user1 = User.objects.get(username=username)
    print(user)
    Follow.objects.filter(follower=current_user, followed=user1).delete()

    return redirect(user, username=username)


def followers(request, username):
    try:
        user1 = User.objects.get(username=username)
        followers = Follow.objects.filter(followed=user1)
    except User.DoesNotExist:
        raise Http404('User does not exist')
    return render(request, 'followers.html', {'followers': followers})


def studios(request):
    studios = Studio.objects.all()
    return render(request, 'studios.html', {'studios': studios})


def addstudio(request):
    # studio_owner_user = get_object_or_404(User, pk=request.user.id)
    if request.method == 'POST':

        form = StudioForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print('hello')
            num = Studio.objects.all().count() + 2
            studio = form.save(commit=False)
            studio.studio_owner = request.user
            studio.save()
            return redirect(reverse('studiodetails', kwargs={'id': num}))
    else:
        form = StudioForm()
    return render(request, 'addstudio.html', {'form': form})


def studiodetails(request, id):
    studio = Studio.objects.get(id=id)

    return render(request, 'studiodetails.html', {'studio': studio})


def sendmail(request, username):
    user1 = User.objects.get(username=username)
    user_email = user1.email
    current_user = request.user
    subject = 'Request for Studio'
    message = "{} has requested your studio. You can contact him for further details. His Email: {}".format(current_user.username, current_user.email)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)
    return redirect('successmail')


def successmail(request):
    return render(request, 'successmail.html')


# class AddStudioView(CreateView):
#     model = Studio
#     fields = '__all__'

#     success_url = reverse_lazy('studios')
#     template_name = 'addstudio.html'

    # def form_valid(self, form):
    #     form.instance.studio_owner = self.request.user
    #     return super().form_valid(form)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# class login_view(LoginView):
#     # The line below overrides the default template path of <appname>/<modelname>_login.html
#     template_name = 'musictime/login.html'
#      # Where accounts/login.html is the path under the templates folder as defined in your settings.py file

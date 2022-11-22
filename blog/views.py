from django.shortcuts import render, redirect
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import authentication_classes, permission_classes
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotAllowed

posts = [
    {
        'author':'Alpha',
        'title':'Blog Post 1',
        'Content':'First Post content',
        'date_posted':'22 Nov 2022',
    },
    {
        'author': 'Alpha1',
        'title': 'Blog Post 2',
        'Content': '2nd Post content',
        'date_posted': '22 Nov 2022',
    },
    {
        'author': 'Alpha3',
        'title': 'Blog Post 3',
        'Content': '3rd Post content',
        'date_posted': '22 Nov 2022',
    }
]


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# @login_required(login_url='/login/')
def home(request):
    if request.GET.get('Token') == 'funsol12345':
        print('recieved token')

        context = {
            'posts': posts
        }
        return render(request, 'blog/index.html', context)
    else:
        return HttpResponseNotAllowed(request, 'Nothing to show')



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact'})


def search_result(request):
    return render(request, 'blog/search_result.html', {'title': 'Search Result'})


def single_post(request):
    return render(request, 'blog/single_post.html', {'title': 'Single Post'})


def category(request):
    return render(request, 'blog/category.html', {'title': 'Category'})


def login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, template_name='blog/login.html', context={'form': form})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(to='redirect_view')
        else:
            form = UserLoginForm()
            messages.error(request, 'Invalid User !!')
            return render(request, template_name='blog/login.html', context={'form': form})

@login_required(login_url='/login/')
def redirect_view(request):

    # if request.user.groups.filter(name='Fun-Mob-Coordinator').exists() or request.user.groups.filter(
    #         name='Fun-Mob-Viewer').exists() or request.user.groups.filter(
    #         name='Fun-Mob-Editor').exists() or request.user.groups.filter(name='Supervisor').exists():
        try:
            if f"{request.META['HTTP_REFERER']}".find('login'):
                pass
            else:
                messages.info(request, 'action not allowed')
        except:
            pass
            # messages.info(request, 'action not allowed')
        return redirect(to='fun-mob-home')

    # elif request.user.groups.filter(name='Fun-Ads-Coordinator').exists() or request.user.groups.filter(
    #         name='Fun-Ads-Viewer').exists() or request.user.groups.filter(
    #         name='Fun-Ads-Editor').exists() or request.user.groups.filter(name='Supervisor').exists():
    #     try:
    #         if f"{request.META['HTTP_REFERER']}".find('login'):
    #             pass
    #
    #         else:
    #             messages.info(request, 'action not allowed')
    #     except:
    #         pass
    #         # messages.info(request, 'action not allowed')
    #     return redirect(to='fun-ad-home')
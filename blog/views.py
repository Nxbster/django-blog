from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#----Halo API Imports----
#import requests
#import json

def home(request):
    context = {
        'posts': Post.objects.all()
    }

    #----More Halo API Stuff----
    #response = requests.get("https://www.haloapi.com/stats/h5/servicerecords/arena?players=Nebster9", headers={"Ocp-Apim-Subscription-Key" : "22b1ea1c61b64998935eaceda8acff7a"})
    #def jprint(obj):
    # create a formatted string of the Python JSON object
        #text = json.dumps(obj, sort_keys=True, indent=4)
        #print(text)
    #jprint(response.json())

    return render(request, 'blog/home.html', context)

class PostListView(ListView): #Home page
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<view_type>
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView): #Home page
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<view_type>
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
        

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
 
    def form_valid(self, form):
        form.instance.author = self.request.user #Set instance author to current logged-in user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
 
    def form_valid(self, form):
        form.instance.author = self.request.user #Set instance author to current logged-in user
        return super().form_valid(form)

    def test_func(self): #prevent users from updating other blog posts
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self): #prevent users from updating other blog posts
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


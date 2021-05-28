from django.shortcuts import render

# Create your views here.
from django import forms
from .models import Post
from django.shortcuts import render, redirect
from .forms import CreateUser
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        register_form = CreateUser(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form = CreateUser()
        context = {
            "form": register_form
        }
    return render(request, 'register.html', context=context)

class CreatePost(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['text', 'created_at', 'updated_at']
    template_name = 'create_post.html'
    success_url = reverse_lazy('index-page')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


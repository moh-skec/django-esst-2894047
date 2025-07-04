from django.shortcuts import render
from django.templatetags.static import static
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

class HomeView(TemplateView):
    """
    Render the home page.
    """
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'today': date.today(),
            'title': 'Home - SmartNote',
            'description': 'Welcome to SmartNote, your personal note-taking app.',
            'keywords': 'home, smartnote, note-taking, personal notes',
            'author': 'SmartNote Team',
            'og_title': 'SmartNote - Home',
            'og_description': 'Capture your thoughts, ideas, and tasks with ease.',
            'og_url': self.request.build_absolute_uri('/'),
            'og_type': 'website',
            'twitter_card': 'summary_large_image',
            'twitter_site': '@SmartNoteApp',
            'twitter_title': 'SmartNote - Home',
            'twitter_description': 'Capture your thoughts, ideas, and tasks with ease.',
            'og_image': static('images/og-image.png'),
            'twitter_image': static('images/twitter-image.png'),
            'twitter_creator': '@SmartNoteApp',
        })
        return context

class SignUpView(FormView):
    """
    User registration view.
    """
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # redirect to the login page on success

    def form_valid(self, form):
        # This saves the new user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'title': 'Sign Up - SmartNote',
            'description': 'Create a new SmartNote account.',
            'keywords': 'signup, register, smartnote, note-taking',
        })
        return ctx

class LoginView(LoginView):
    """
    Custom login view.
    """
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login - SmartNote'
        context['description'] = 'Login to your SmartNote account.'
        context['keywords'] = 'login, smartnote, note-taking, personal notes'
        return context
    
class LogoutView(LoginRequiredMixin, LogoutView):
    """
    Custom logout view.
    """
    next_page = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Logout - SmartNote'
        context['description'] = 'You have been logged out of your SmartNote account.'
        context['keywords'] = 'logout, smartnote, note-taking, personal notes'
        return context
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Note  # Adjust the import based on your project structure
from .forms import NoteForm  # Adjust the import based on your project structure

class NoteListView(ListView):
    model = Note  # Replace with your actual Note model
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return self.model.objects.order_by('-created_at')
    
class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note  # Replace with your actual Note model
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'

    def get_queryset(self):
        return self.model.objects  # Only show public notes

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note  # Replace with your actual Note model
    template_name = 'notes/note_form.html'
    success_url = '/notes/'  # Redirect to the note list after creation
    form_class = NoteForm  # Use the NoteForm defined in forms.py

    def form_valid(self, form):
        # assign the logged-in user as the author before saving
        form.instance.author = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note  # Replace with your actual Note model
    template_name = 'notes/note_form.html'
    success_url = '/notes/'  # Redirect to the note list after updating
    form_class = NoteForm  # Use the NoteForm defined in forms.py

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)  # Only allow updates by the author
    
class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note  # Replace with your actual Note model
    template_name = 'notes/note_confirm_delete.html'
    success_url = '/notes/'  # Redirect to the note list after deletion

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)  # Only allow deletions by the author
    
class NoteLikeView(LoginRequiredMixin, RedirectView):
    pattern_name = 'note_detail'  # named URL to reverse
    permanent = False

    def post(self, request, *args, **kwargs):
        note = get_object_or_404(Note, pk=kwargs['pk'])
        note.likes += 1
        note.save()
        # `get_redirect_url` will reverse `pattern_name` with kwargs
        return super().post(request, *args, **kwargs)

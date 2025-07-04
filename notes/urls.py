from django.urls import path
from .views import NoteDetailView, NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView, NoteLikeView

urlpatterns = [
    path("", NoteListView.as_view(), name="note_list"),
    path("<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("create/", NoteCreateView.as_view(), name="note_create"),
    path("edit/<int:pk>/", NoteUpdateView.as_view(), name="note_edit"),
    path("delete/<int:pk>/", NoteDeleteView.as_view(), name="note_delete"),
    path("like/<int:pk>/", NoteLikeView.as_view(), name="note_like"),
]
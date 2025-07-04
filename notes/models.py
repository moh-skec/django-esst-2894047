from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    is_public = models.BooleanField(default=False, help_text=_("Is this note publicly accessible?"))
    likes = models.PositiveIntegerField(default=0, help_text=_("Number of likes for this note"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        ordering = ['-created_at']  # Newest notes first
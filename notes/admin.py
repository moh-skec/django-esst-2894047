from django.contrib import admin

from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """
    Admin interface for managing notes.
    """
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    prepopulated_fields = {'title': ('content',)}  # Automatically fill title from content
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

admin.site.site_header = "SmartNote Admin"
admin.site.site_title = "SmartNote Admin Portal"
admin.site.index_title = "Welcome to SmartNote Admin"
admin.site.enable_nav_sidebar = False  # Disable the sidebar for a cleaner look
admin.site.site_url = None  # Disable the link to the site from the admin header
admin.site.empty_value_display = 'N/A'  # Display 'N/A' for empty fields in the admin interface
admin.site.default_permissions = ('add', 'change', 'delete', 'view')  # Set default permissions for the admin interface
# admin.site.register(Note, NoteAdmin)
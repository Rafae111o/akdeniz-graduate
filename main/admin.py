from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from parler.admin import TranslatableAdmin

from main.models import User, Post, Comment, Faq, Feedback, Testimonial

class PostAdmin(TranslatableAdmin):
    list_display = ('id', 'title')

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'short', 'image', 'date'),
        }),
    )


class FaqAdmin(TranslatableAdmin):
    list_display = ('id', 'title')

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'image'),
        }),
    )

class TestimonialAdmin(TranslatableAdmin):
    list_display = ('id', 'name')

    fieldsets = (
        (None, {
            'fields': ('name', 'content', 'image'),
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Feedback)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Faq, FaqAdmin)
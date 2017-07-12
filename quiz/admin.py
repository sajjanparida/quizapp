from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Question,User
from .forms import UserForm

class QuestionAdmin(admin.ModelAdmin):
    list_display=["__str__","timestamp"]
    class meta:
        model=Question

class UserAdmin(admin.ModelAdmin):
    list_display=["username"]
    form=UserForm
    class meta:
        model=User

admin.site.register(Question,QuestionAdmin)
admin.site.register(User,UserAdmin)
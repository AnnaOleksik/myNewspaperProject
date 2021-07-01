from django.contrib import admin
from .models import Article

class DisplayDate(admin.ModelAdmin):
    readonly_fields=("date",)

admin.site.register(Article,DisplayDate)

# Register your models here.

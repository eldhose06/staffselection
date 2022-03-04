from django.contrib import admin

# Register your models here.
# from staffapp.models import Users
#
from staffapp.models import User, Religion, Caste, Institutes, Post, Nationality

admin.site.register(User)

# admin.site.register(Religion)
@admin.register(Religion)
class ReligionAdmin(admin.ModelAdmin):
    list_display = ['id', 'religion']

# admin.site.register(Caste)
@admin.register(Caste)
class CasteAdmin(admin.ModelAdmin):
    list_display = ['id', 'religion', 'caste']

# admin.site.register(Nationality)
@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ['id', 'nationality']

# admin.site.register(Institutes)
@admin.register(Institutes)
class InstitutesAdmin(admin.ModelAdmin):
    list_display = ['id', 'instituteName']

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'institute', 'postName']




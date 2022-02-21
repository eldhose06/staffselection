from django.contrib import admin

# Register your models here.
# from staffapp.models import Users
#
from staffapp.models import User, Religion, Caste, Institutes, Post, QualificationDetails, ApplicantInfo, Nationality

admin.site.register(User)
admin.site.register(Religion)
admin.site.register(Caste)
admin.site.register(Nationality)
admin.site.register(Institutes)
admin.site.register(Post)
admin.site.register(QualificationDetails)
admin.site.register(ApplicantInfo)

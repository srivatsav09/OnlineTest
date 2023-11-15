from django.contrib import admin
from testApp.models import Exam, Question, UserResponse

# Register your models here.

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(UserResponse)

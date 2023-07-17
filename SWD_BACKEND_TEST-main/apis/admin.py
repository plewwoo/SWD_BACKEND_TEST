from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(SchoolStructure)
admin.site.register(Schools)
admin.site.register(Classes)
admin.site.register(Personnel)
admin.site.register(Subjects)
admin.site.register(StudentSubjectsScore)
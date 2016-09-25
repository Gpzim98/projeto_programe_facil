from django.contrib import admin
from core.models import Lead, Course, Member, Module, Class, CourseEnrollment, ModulesEnrollment

admin.site.register(Lead)
admin.site.register(CourseEnrollment)
admin.site.register(ModulesEnrollment)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Class)
admin.site.register(Member)

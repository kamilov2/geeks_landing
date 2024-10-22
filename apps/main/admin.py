from django.contrib import admin
from .models import Course, Lead, MentorStaje, StudentWorkProsent, FAQ, CourseFor, SpecialistCourse, CourseFAQ

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_modern', 'marque_text')
    search_fields = ('title',)

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone_number', 'course', 'status')
    list_filter = ('status',)

@admin.register(MentorStaje)
class MentorStajeAdmin(admin.ModelAdmin):
    list_display = ('year',)

@admin.register(StudentWorkProsent)
class StudentWorkProsentAdmin(admin.ModelAdmin):
    list_display = ('prosent',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')
    search_fields = ('question',)

@admin.register(CourseFor)
class CourseForAdmin(admin.ModelAdmin):
    list_display = ('course',)

@admin.register(SpecialistCourse)
class SpecialistCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'image')

@admin.register(CourseFAQ)
class CourseFAQAdmin(admin.ModelAdmin):
    list_display = ('course', 'question')

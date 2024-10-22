from rest_framework import serializers
from .models import Lead, FAQ, MentorStaje, StudentWorkProsent, Course, CourseFor, SpecialistCourse, CourseDescription, CourseFAQ

class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = ['id', 'first_name', 'age', 'phone_number', 'course']
        read_only_fields = ['id']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']



class MentorStajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorStaje
        fields = ['id', 'year']

class StudentWorkProsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentWorkProsent
        fields = ['id', 'prosent']

class CombinedStatsSerializer(serializers.Serializer):
    course_count = serializers.IntegerField()
    mentor_staje = MentorStajeSerializer()
    student_prosent = StudentWorkProsentSerializer()
class CourseForSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFor
        fields = ['id', 'text']

class SpecialistCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialistCourse
        fields = ['id', 'text', 'image']

class CourseDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDescription
        fields = ['id', 'title', 'description']

class CourseFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFAQ
        fields = ['id', 'question', 'answer']

class NestedCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'month_period', 'is_modern']

class CourseSerializer(serializers.ModelSerializer):
    course_for = CourseForSerializer(many=True, source='coursefor_set', read_only=True)
    specialist_courses = SpecialistCourseSerializer(many=True, source='specialistcourse_set', read_only=True)
    descriptions = CourseDescriptionSerializer(many=True, source='coursedescription', read_only=True)
    faqs = CourseFAQSerializer(many=True, source='coursefaq_set', read_only=True)
    other_courses = NestedCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'text_1', 'text_2', 'marque_text', 'marque_icon',
            'course_for', 'specialist_courses', 'descriptions', 'faqs', 'other_courses'
        ]
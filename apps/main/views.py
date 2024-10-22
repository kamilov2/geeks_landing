from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Lead, FAQ, MentorStaje, StudentWorkProsent, Course
from .serializers import LeadSerializer, FAQSerializer, MentorStajeSerializer, StudentWorkProsentSerializer, CombinedStatsSerializer, CourseSerializer, NestedCourseSerializer



def custom_response(data=None, message=None, status_code=200):
 
    response = {}
    if data is not None:
        response['data'] = data
    if message is not None:
        response['message'] = message
    return Response(response, status=status_code)

class BaseModelViewSet(viewsets.ModelViewSet):
 
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return custom_response(
            data=serializer.data,
            message={'status': 'success', 'text': 'Данные успешно получены!'}
        )
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return custom_response(
            data=serializer.data,
            message={'status': 'success', 'text': 'Данные успешно получены!'}
        )
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return custom_response(
            data=serializer.data,
            message={'status': 'success', 'text': 'Qabul qilindi!'},
            status_code=status.HTTP_201_CREATED
        )
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return custom_response(
            data=serializer.data,
            message={'status': 'success', 'text': 'Объект успешно обновлён!'}
        )
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return custom_response(
            message={'status': 'success', 'text': 'Объект успешно удалён!'}
        )
    
class BaseAPIView(APIView):
   
    permission_classes = [AllowAny]
    
    def get_response(self, data=None, message=None, status_code=200):
        return custom_response(data=data, message=message, status_code=status_code)
    
class LeadViewSet(BaseModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class FAQViewSet(BaseModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class CombinedStatsView(BaseAPIView):
   
    def get(self, request):
        course_count = Course.objects.count()
        mentor_staje = MentorStaje.objects.last() 
        student_prosent = StudentWorkProsent.objects.last()  

        data = {
            'course_count': course_count,
            'mentor_staje': MentorStajeSerializer(mentor_staje).data,
            'student_prosent': StudentWorkProsentSerializer(student_prosent).data,
        }

        message = {'status': 'success', 'text': "O'qituvchilar bo'limi!"}
        return self.get_response(data=data, message=message)

class CourseViewSet(BaseModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request, *args, **kwargs):
        course_id = request.query_params.get('id', None)

        if course_id and course_id.isdigit():
            course_id = int(course_id)
            course = Course.objects.filter(id=course_id).first()

            if not course:
                message = {'status': 'error', 'text': 'Курс не найден'}
                return Response({'data': {}, 'message': message}, status=404)

            other_courses = Course.objects.exclude(id=course_id)[:4]
            course_data = self.get_serializer(course).data
            course_data['other_courses'] = NestedCourseSerializer(other_courses, many=True).data

            message = {'status': 'success', 'text': 'Детальная информация о курсе!'}
            return Response({'data': course_data, 'message': message})

        # Если ID не передан, возвращаем все курсы
        courses = Course.objects.all()
        courses_data = self.get_serializer(courses, many=True).data

        message = {'status': 'success', 'text': 'Все курсы успешно получены!'}
        return Response({'data': courses_data, 'message': message})

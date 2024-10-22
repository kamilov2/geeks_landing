from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, FAQViewSet, CombinedStatsView, CourseViewSet

router = DefaultRouter()
router.register(r'leads', LeadViewSet)
router.register(r'faqs', FAQViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('combined/', CombinedStatsView.as_view(), name='combined-stats'),
    path('courses/', CourseViewSet.as_view({'get': 'list'}), name='courses'),
]
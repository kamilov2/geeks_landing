from django.db import models
from django.urls import reverse

class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Course Title", help_text="Enter the official name of the course (no more than 255 characters)")
    text_1 = models.TextField(verbose_name="About the Course")
    text_2 = models.TextField()
    month_period = models.IntegerField()
    marque_text = models.CharField(max_length=155)
    marque_icon = models.CharField(max_length=155)
    is_modern = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('coursefor', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['title']


class CourseFor(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course", help_text="Select a course")
    text = models.TextField()

    def __str__(self):
        return f"{self.course.title} for"


class SpecialistCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course", help_text="Select a course")
    text = models.TextField()
    image = models.ImageField(upload_to='specialist_courses/')

    def __str__(self):
        return f"Specialist Course: {self.course.title}"


class Lead(models.Model):
    STATUS_CHOICES = [
        ('pending', 'No Response'),
        ('confirmed', 'Will Attend'),
        ('declined', 'Will Not Attend'),
        ('no_call', 'Not Called'),
    ]

    first_name = models.CharField(max_length=100, verbose_name="First Name", help_text="Enter the lead's first name (no more than 100 characters)")
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number", help_text="Enter the lead's phone number (no more than 20 characters)")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course", help_text="Select a course")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='no_call', verbose_name="Status", help_text="Select the lead's status")

    def __str__(self):
        return f'{self.first_name} — {self.phone_number} ({self.get_status_display()})'

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"


class CourseDescription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='coursedescription', verbose_name="Course", help_text="Select a course")
    title = models.CharField(max_length=155, verbose_name="Description Title", help_text="Enter the title of the description")
    description = models.TextField(verbose_name="Description", help_text="Enter complete information about the course", null=True, blank=True)

    def __str__(self):
        return f"{self.course.title} Description"


class MentorStaje(models.Model):
    year = models.PositiveIntegerField(verbose_name="Year", help_text="Enter the mentor's experience for the specified year")

    def __str__(self):
        return f'{self.year} Year Experience'

    class Meta:
        verbose_name = "Mentor Experience"
        verbose_name_plural = "Mentor Experiences"
        ordering = ['year']


class StudentWorkProsent(models.Model):
    prosent = models.PositiveIntegerField(verbose_name="Employment Percentage", help_text="Enter the employment rate of graduates")

    def __str__(self):
        return f'{self.prosent}% of graduates are employed'

    class Meta:
        verbose_name = "Graduate Employment Percentage"
        verbose_name_plural = "Graduate Employment Percentages"


class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name="Question", help_text="Frequently Asked Question")
    answer = models.TextField(verbose_name="Answer", help_text="Answer to the question")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At", help_text="Date and time when the question was created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At", help_text="Date and time of the last update")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Frequently Asked Question"
        verbose_name_plural = "Frequently Asked Questions"
        ordering = ['-created_at']


class CourseFAQ(models.Model):
    course = models.ForeignKey(Course, verbose_name='Course', on_delete=models.CASCADE)
    question = models.CharField(max_length=255, verbose_name="Question", help_text="Frequently Asked Question")
    answer = models.TextField(verbose_name="Answer", help_text="Answer to the question")

    def __str__(self):
        return f'{self.course.title} - Question: {self.question}'

    class Meta:
        verbose_name = "Course FAQ"
        verbose_name_plural = "Course FAQs"

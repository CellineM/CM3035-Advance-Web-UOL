from django.contrib import admin
from .models import StudentsData

@admin.register(StudentsData)
class adminStudentsData(admin.ModelAdmin):
    list_display = ('student_id',
                   'age',
                   'gender',
                   'ethnicity',
                   'parental_education',
                   'study_time_weekly',
                   'absences',
                   'tutoring',
                   'parental_support',
                   'extracurricular',
                   'sports',
                   'music',
                   'volunteering',
                   'gpa',
                   'grade_class')
    
    search_fields = ('student_id',
                   'age',
                   'gender',
                   'ethnicity',
                   'parental_education',
                   'study_time_weekly',
                   'absences',
                   'tutoring',
                   'parental_support',
                   'extracurricular',
                   'sports',
                   'music',
                   'volunteering',
                   'gpa',
                   'grade_class')

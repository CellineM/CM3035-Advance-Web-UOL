from django.db import models

class StudentsData(models.Model):
    # choices for gender, ethnicity and parent education, by having names instead of numbers to prevent confusion
    genderOption = [(0, 'Male'), (1, 'Female')]
    ethnicOption = [(0, 'Caucasian'), (1, 'African-American'), (2, 'Asian'), (3, 'Other')]
    parentEdu_option = [(0, 'None'), (1, 'High School'), (2, 'Some College'), (3, 'Bachelor'), (4, 'Higher')]


    student_id = models.AutoField(primary_key = True) # pk of the model
    # fields - each data with its appropriate types and options/choices.
    age = models.IntegerField()
    gender = models.IntegerField(choices = genderOption)
    ethnicity = models.IntegerField(choices = ethnicOption)
    parental_education = models.IntegerField(choices = parentEdu_option)
    study_time_weekly = models.FloatField()
    absences = models.IntegerField()
    tutoring = models.BooleanField()
    parental_support = models.IntegerField()
    extracurricular = models.BooleanField()
    sports = models.BooleanField()
    music = models.BooleanField()
    volunteering = models.BooleanField()
    gpa = models.FloatField()
    grade_class = models.FloatField()

    
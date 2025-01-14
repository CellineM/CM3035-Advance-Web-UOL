import csv
from django.core.management.base import BaseCommand
from students.models import StudentsData

class Command(BaseCommand):
    help = 'Load data from CSV file into the database'

    def handle(self, *args, **kwargs):
        # the location of the student performance data csv
        file_path = 'students/csv/Student_performance_data.csv'  # Update this path
        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # create new student data onjects for each row in csv
                    StudentsData.objects.create(
                        age=int(row['Age']), # covert age to int
                        gender=int(row['Gender']),
                        ethnicity=int(row['Ethnicity']),
                        parental_education=int(row['ParentalEducation']),
                        study_time_weekly=float(row['StudyTimeWeekly']), # convert study time weekly into float type
                        absences=int(row['Absences']),
                        tutoring=bool(int(row['Tutoring'])), # convert to boolean (yes or no)
                        parental_support=int(row['ParentalSupport']),
                        extracurricular=bool(int(row['Extracurricular'])),
                        sports=bool(int(row['Sports'])),
                        music=bool(int(row['Music'])),
                        volunteering=bool(int(row['Volunteering'])),
                        gpa=float(row['GPA']),
                        grade_class=float(row['GradeClass'])
                    )
                    # to handle the error if it occurs during data processing
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error processing row {row}: {e}"))
                    self.stdout.write(self.style.SUCCESS('Data loaded successfully'))

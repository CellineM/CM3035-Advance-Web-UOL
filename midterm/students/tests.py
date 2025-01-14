from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
# from rest_framework.test import APIClient
from rest_framework import status
from .models import StudentsData

class StudentsDataTesting(TestCase):
    def setUp(self):
        # Create a couple of test records
        StudentsData.objects.create(
            age=16,
            gender=1,
            ethnicity=2,
            parental_education=2,
            study_time_weekly=15,
            absences=2,
            tutoring=True,
            parental_support=3,
            extracurricular=True,
            sports=False,
            music=False,
            volunteering=False,
            gpa=3.5,
            grade_class=0
        )

        StudentsData.objects.create(
            age=16,
            gender=0,
            ethnicity=3,
            parental_education=1,
            study_time_weekly=10,
            absences=5,
            tutoring=True,
            parental_support=2,
            extracurricular=True,
            sports=True,
            music=True,
            volunteering=True,
            gpa=2.25,
            grade_class=3
        )

    def test_create_record(self):
        url = reverse('create_record')
        data = {
            'age': 15,
            'gender': 0,
            'ethnicity': 1,
            'parental_education': 4,
            'study_time_weekly': 15,
            'absences': 0,
            'tutoring': True,
            'parental_support': 3,
            'extracurricular': True,
            'sports': True,
            'music': False,
            'volunteering': True,
            'gpa': 3.95,
            'grade_class': 0
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        def testing_ageGpa(self):
            url = reverse('ageGpa')
            response = self.client.get(url, format = 'json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def testing_parent_highGpa(self):
            url = reverse('parent_highGpa')
            response = self.client.get(url, format = 'json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def testing_ethnic(self):
            url = reverse('ethnic')
            response = self.client.get(url, format = 'json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def testing_latestGet(self):
            url = reverse('latest_record')
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
    
        def test_latestPut(self):
            url = reverse('latest_record')
            data = {
                'age': 17  # Example 
            }
            response = self.client.put(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_latestDelete(self):
            url = reverse('latest_record')
            response = self.client.delete(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_fullList(self):
            url = reverse('fullLists')
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)



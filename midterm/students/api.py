from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import Min, Max, Avg
from .models import StudentsData
from .serializers import MainSerializer

class CreateNewRecord(generics.CreateAPIView):
    # API endpoint to create new record
    queryset = StudentsData.objects.all()
    serializer_class = MainSerializer

class LatestRecord(APIView):
    # handling the GET request to get the latest reocrd of the student
    def get(self, request, *args, **kwargs):
        try:
            # this will retrieve the latest record based on the student id
            latest_record = StudentsData.objects.latest('student_id')
            # serialize and return the student record
            serializer = MainSerializer(latest_record)
            return Response(serializer.data)
        except StudentsData.DoesNotExist:
            return Response({'message': 'There is no student record found'}, status=status.HTTP_404_NOT_FOUND)

    # handle the PUT request for updating the student data 
    def put(self, request, *args, **kwargs):
        try:
            latest_record = StudentsData.objects.latest('student_id')
            # this will desrialize first then when input the data to be input, it will partially update it
            serializer = MainSerializer(latest_record, data=request.data, partial=True)
            # making sure that the data is valid
            if serializer.is_valid():
                # if yes, it will save the latest record to the data.
                serializer.save()
                return Response({'status': 'success', 'message': 'Latest student record has been updated.'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StudentsData.DoesNotExist:
            return Response({'message': 'There is no student record found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            latest_record = StudentsData.objects.latest('student_id')
            # will delete the latest record of the student data and remove it from the actual data.
            latest_record.delete()
            return Response({'status': 'successful', 'message': 'The latest record has been successfully deleted.'}, status=status.HTTP_200_OK)
        except StudentsData.DoesNotExist:
            return Response({'message': 'There is no student record found'}, status=status.HTTP_404_NOT_FOUND)

class AvgAgeGpa(generics.GenericAPIView):
    # endpoint to calculate the average GPA of the students by age
    def get (get, request, *args, **kwargs):
        result = StudentsData.objects.values('age').annotate(gpa_avg_age = Avg('gpa'))
        return Response (result)
    
    
class ParentStudentGpa(generics.ListAPIView):
    serializer_class = MainSerializer

    # filter from the dataset and get the parental education where they have high education based on the min gpa of 3 
    def get_queryset(self):
       return StudentsData.objects.filter(parental_education__gte=3, gpa__gt=3.0)
    
class EthnicGpa(generics.GenericAPIView):

    # get the minimum, maximum, and the average gpa based on the ethnicity
    def get (self, request, *args, **kwargs):
        result = StudentsData.objects.values('ethnicity').annotate(
            minimumGpa = Min('gpa'),
            maximumGpa = Max('gpa'),
            averageGpa = Avg('gpa')
        ) 
        return Response(result)
    
class fullList(generics.GenericAPIView):
    queryset = StudentsData.objects.all().order_by('-student_id')
    serializer_class = MainSerializer
    
    def get(self, request, *args, **kwargs):
        # Getting the information data from the database
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
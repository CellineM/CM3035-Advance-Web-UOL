from django.contrib import admin
from django.urls import path
from .views import home

from .api import ( CreateNewRecord, AvgAgeGpa, ParentStudentGpa,
                    EthnicGpa, fullList, LatestRecord)

urlpatterns = [
    # url for the homepage
    path('', home, name = 'homepage'),
    # the url for the admin site usernamr and password
    path('admin/', admin.site.urls),
    # the endpoints for each category (shown in api.py) like create new record, avg gpa by age, etc.
    path('api/students/create/', CreateNewRecord.as_view(), name = 'create_record'),
    path('api/students/latest/', LatestRecord.as_view(), name='latest_record'),
    path('api/students/gpa/age/', AvgAgeGpa.as_view(), name = 'ageGpa'),
    path('api/students/gpa/parent/', ParentStudentGpa.as_view(), name = 'parent_highGpa'),
    path('api/students/gpa/ethnic/', EthnicGpa.as_view(), name = 'ethnic'),
    path('api/students/fullList/', fullList.as_view(), name = 'fullLists'),
]
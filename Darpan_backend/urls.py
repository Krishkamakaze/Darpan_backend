from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentListCreate.as_view() ),
    path('studentapi/<int:rollnumber>', views.StudentRetrieveUpdate.as_view() ),
    path('studentsearch/', views.StatusSearch.as_view() ),
]

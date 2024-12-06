from django.contrib import admin
from django.urls import path, include

from app01 import views
from app01.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.getStudents, name='get_students'),  # Root URL for listing students
    path('create/', views.createStudent, name='create_student'),  # URL for creating a student
    path('delete/<int:id>/', views.deleteStudent, name='delete_student'),  # URL for deleting a student
    path('update/<int:id>/', views.updateStudent, name='update_student'),
path('accounts/', include('django.contrib.auth.urls')),
path('logout/', logout_view, name='logout'),

]

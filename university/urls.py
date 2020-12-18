from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	 
	path('', views.home, name="home"),
	path('home/', views.home, name="home"),
    
	path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),
	path('verification/', views.verification, name="verification"),
	path('signup/', views.signup, name="signup"),
	path('registrationdata/', views.registrationdata, name="registrationdata"),
	path('professorhome/', views.professorhome, name="professorhome"),
	path('studenthome/', views.studenthome, name="studenthome"),
	path('addcourse/', views.addcourse, name="addcourse"),
	path('addcoursefunc/', views.addcoursefunc, name="addcoursefunc"),
	path('addcprofessor/<int:id>', views.addcprofessor, name="addcourse"),
	path('addcstudent/<int:id>', views.addcstudent, name="addcoursestudent"),
	path('allcourse/', views.allcourse, name="allcourse"),
	path('course/<int:id>', views.course, name="course"),

]
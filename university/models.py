from django_mysql.models import ListCharField
from django.db import models,migrations


class Student(models.Model):
	firstname = models.CharField(max_length=200,null=True)
	lastname = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200,null=True)
	password = models.CharField(max_length=200,null=True)
	
	def __str__(self):
		return str(self.id)

class Professor(models.Model):
	firstname = models.CharField(max_length=200,null=True)
	lastname = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200,null=True)
	password = models.CharField(max_length=200,null=True)

	def __str__(self):
		return str(self.id)

class Course(models.Model):
	name = models.CharField(max_length=200,null=True)
	description =  models.CharField(max_length=200,null=True)

	def __str__(self):
		return str(self.id)

class ProfessorCourse(models.Model):
	professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)
	course = models.ForeignKey(Course,on_delete=models.CASCADE, null=True)
	
	def __str__(self):
		return str(self.id)

class StudentCourse(models.Model):
	course = models.ForeignKey(Course,on_delete=models.CASCADE, null=True)
	student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
	
	def __str__(self):
		return str(self.id)


from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.conf import settings
import math, random
import json
import random
from .models import Student,Professor,Course,ProfessorCourse,StudentCourse
from django.views.decorators.csrf import csrf_exempt

def login(request):
    context = {}
    context.update(csrf(request))
    print("login................")
    return render(request, 'login.html', context)

def verification(request):
    context = {}
    email = request.POST.get('email')
    selectsp = request.POST.get('selectsp')
    password = request.POST.get('password')
    if selectsp == "Student":
        for i in Student.objects.all():
            if email == i.email and password == i.password:
                request.session['name'] = i.firstname.capitalize()
                request.session['email'] = i.email
                request.session['cid'] = i.id 
                request.session['sp'] = selectsp
                print("verification.................")
                print (request.session.get('name'))
                print (request.session.get('cid'))
                return HttpResponseRedirect('/studenthome')
        else:
            return render(request, 'login.html', {'error': 'Email Or Password is incorrect.'})
    elif selectsp == "Professor":
        for i in Professor.objects.all():
            if email == i.email and password == i.password:
                request.session['name'] = i.firstname.capitalize()
                request.session['email'] = i.email
                request.session['cid'] = i.id 
                request.session['sp'] = selectsp
                print("verification.................")
                print (request.session.get('name'))
                print (request.session.get('cid'))
                return HttpResponseRedirect('/professorhome')
        else:
            return render(request, 'login.html', {'error': 'Email Or Password is incorrect.'})   

def signup(request):
    context = {}
    context.update(csrf(request))
    print("signup...............")
    return render(request, 'signup.html', context)

def registrationdata(request):
    context = {}
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    selectsp = request.POST.get('selectsp')
    email = request.POST.get('email')
    pass1 = request.POST.get('password')
    pass2 = request.POST.get('confirmpassword')
    print("registrationdata..................")
    if selectsp == "Student":
        for i in Student.objects.all():
            if email == i.email:
                return render(request, 'signup.html', {'error': 'This email is already in use!!'})
        if pass1 == pass2:
            s = Student(firstname=firstname, lastname=lastname, email=email, password=pass1)
            s.save()
            return HttpResponseRedirect('/login/')
        else:
            return render(request, 'signup.html', {'error': 'Re Enter same password!!'})
    if selectsp == "Professor":
        for i in Professor.objects.all():
            if email == i.email:
                return render(request, 'signup.html', {'error': 'This email is already in use!!'})
        if pass1 == pass2:
            s = Professor(firstname=firstname, lastname=lastname, email=email, password=pass1)
            s.save()
            return HttpResponseRedirect('/login/')
        else:
            return render(request, 'signup.html', {'error': 'Re Enter same password!!'})

def home(request):
    context={}
    if request.session.get('name') and request.session.get('cid'):
        name = request.session.get('name')
        cid = request.session.get('cid')
        context['name'] = request.session.get('name')
    return render(request, 'home.html', context)

def logout(request):
    del request.session['name']
    del request.session['cid']
    print("logout................")
    return HttpResponseRedirect('/home/')

def studenthome(request):
    context={}
    context['sp'] = request.session.get('sp')
    if request.session.get('name') and request.session.get('cid'):
        context['name'] = request.session.get('name')
        name = request.session.get('name')
        cid = request.session.get('cid')
        xstudent=Student.objects.get(id=cid)

        for coursea in StudentCourse.objects.all():
            print(coursea.student.id)
            if coursea.student.id == xstudent.id :
                context.setdefault("courses",[]).append([coursea.course.id,coursea.course.name,coursea.course.description])
        print("home.......................")
        print("student.,,:::",cid,name,xstudent)
        print (context)
    return render(request, 'studenthome.html', context)


def professorhome(request):
    context={}
    context['sp'] = request.session.get('sp')
    if request.session.get('name') and request.session.get('cid'):
        context['name'] = request.session.get('name')
        cid = request.session.get('cid')
        xprofessor=Professor.objects.get(id=cid)

        for coursea in ProfessorCourse.objects.all():
            print(coursea)
            if coursea.professor.id == xprofessor.id :
                context.setdefault("courses",[]).append([coursea.course.id,coursea.course.name,coursea.course.description, coursea.professor.firstname])
        else:
            print("else.......")
        print("home.......................")
        print("professor..:::",cid,xprofessor)
        print (context)
    return render(request, 'professorhome.html', context)

def course(request,id):
    context={}
    context['sp'] = request.session.get('sp')
    if request.session.get('name'):
        name = request.session.get('name')
        context['name']= name
    course = Course.objects.get(id=id)
    context['course']=course
    
    return render(request, 'course.html', context)

def addcourse(request):
    context={}
    context['sp'] = request.session.get('sp')
    if request.session.get('name'):
        context['name']= request.session.get('name')
        name = request.POST.get('name')
        
    return render(request, 'addcourse.html', context)

def addcoursefunc(request):
    print("addcoursefunc..................")
    context={}
    context['sp'] = request.session.get('sp')
    if request.session.get('name'):
        context['name']= request.session.get('name')
        name = request.POST.get('name')
        description = request.POST.get('description')    
        c = Course(name=name,description=description)
        c.save()
        cid = request.session.get('cid')
        xprofessor=Professor.objects.get(id=cid)
        ca = ProfessorCourse(course=c,professor=xprofessor)
        ca.save()
        return HttpResponseRedirect('/professorhome/')

def addcprofessor(request,id):
    context={}
    if request.session.get('name') and request.session.get('cid'):
        context['name'] = request.session.get('name')
        cid = request.session.get('cid')
        
        for coursea in ProfessorCourse.objects.all():
                print(coursea)
                if coursea.course.id == id and coursea.professor.id == cid :
                    return HttpResponseRedirect('/professorhome/')
        course = Course.objects.get(id=id)
        xprofessor=Professor.objects.get(id=cid)
        ca = ProfessorCourse(course=course,professor=xprofessor)
        ca.save()
        return HttpResponseRedirect('/professorhome/')

def addcstudent(request,id):
    context={}
    if request.session.get('name') and request.session.get('cid'):
        context['name'] = request.session.get('name')
        cid = request.session.get('cid')
        
        for coursea in StudentCourse.objects.all():
                print(coursea)
                if coursea.course.id == id and coursea.student.id == cid :
                    return HttpResponseRedirect('/studenthome/')
        course = Course.objects.get(id=id)
        xstudent=Student.objects.get(id=cid)
        ca = StudentCourse(course=course,student=xstudent)
        ca.save()
        return HttpResponseRedirect('/studenthome/')

def allcourse(request):
    context={}
    context['name'] = request.session.get('name')
    selectsp = request.POST.get('selectsp')
    context['sp'] = request.session.get('sp')
    
    for coursea in Course.objects.all():
        context.setdefault("courses",[]).append([coursea.id,coursea.name,coursea.description, "ypypypy"])
        
    return render(request, 'allcourse.html', context)


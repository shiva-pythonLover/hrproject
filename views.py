from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib import messages
from app_ADVANCED_LEARNING_INSTITUTE.forms import ContactForm, AdminLoginForm, AddCourseForm, FeedBackForm
from app_ADVANCED_LEARNING_INSTITUTE.models import ContactModel, AddCourseModel, FeedBackModel


def mainpage(request):
    return render(request,"homepage.html")


class Contact(View):
    def get(self,request):
        return render(request,"contact.html",{'contact_form':ContactForm})
    def post(self,request):
        form=ContactForm(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        courses = request.POST['courses']
        shifts =request.POST['shifts']
        location = request.POST['location']
        gender = request.POST['gender']
        start_date = request.POST['start_date']
        ContactModel(name=name,email=email,phone=phone,courses=courses,shifts=shifts,location=location,gender=gender,start_date=start_date).save()
        messages.success(request,'CONTACT DETAILS SUCCESSFULLY SAVED')
        return redirect('contact')


class AdminLogin(View):
    def get(self, request):
        return render(request, "admin.html", {'adminlogin_form': AdminLoginForm})
    def post(self,request):
        form=AdminLoginForm(request.POST)
        user_name=request.POST['User_Name']
        password=request.POST['Password']
        if user_name=='admin' and password=='admin':
            return render(request,"admin_homepage.html")


class AddCourse(View):
    def get(self, request):
        return render(request, "admin_homepage.html", {'add_course_form': AddCourseForm})
    def post(self,request):
        form=AddCourseForm(request.POST)
        course_id = request.POST['course_id']
        course_name = request.POST['course_name']
        course_duration = request.POST['course_duration']
        course_fee = request.POST['course_fee']
        course_start_date = request.POST['course_start_date']
        course_start_time = request.POST['course_start_time']
        course_trainer_name = request.POST['course_trainer_name']
        course_trainer_exp = request.POST['course_trainer_exp']
        AddCourseModel(course_id=course_id,course_name=course_name,course_duration=course_duration,course_fee=course_fee,course_start_date=course_start_date,course_start_time=course_start_time,course_trainer_name=course_trainer_name,course_trainer_exp=course_trainer_exp).save()
        messages.success(request,'CORSE DETAILS SUCCESSFULLY ADDED')
        return redirect('add_course')


class FeedBack(View):
    def get(self, request):
        x = FeedBackModel.objects.all()
        return render(request, "feedback.html", {'feedback_form': FeedBackForm,'feedback_objects':x})
    def post(self,request):
        name=request.POST['name']
        rating=request.POST['rating']
        feedback=request.POST['feedback']
        feedback_date=request.POST['date_time']
        FeedBackModel(name=name,rating=rating,feedback=feedback,feedback_date=feedback_date).save()
        x=FeedBackModel.objects.all()

        messages.success(request,'FEEDBACK SUCCESFULLY SENT')
        return render(request,'feedback.html',{'feedback_objects':x,'feedback_form':FeedBackForm})

def view_all_courses(request):
    x=AddCourseModel.objects.all()
    return render(request,"admin_homepage.html",{'view_all_courses':x})



class Update(View):
    def get(self, request):
        x=AddCourseModel.objects.all()
        return render(request, "admin_homepage.html",{'update':x})


def show_all_courses(request):
    x = AddCourseModel.objects.all()
    return render(request, "homepage.html", {'show_all_courses': x})


def view_all_students(request):
    x=ContactModel.objects.all()
    return render(request,"admin_homepage.html",{'view_all_students':x})
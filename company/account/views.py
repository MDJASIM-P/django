from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View   # class View import from module views of django
from .forms import *  # /RegiForm  # class RegiForm import from module forms on same app/account
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import *

# Create your views here.

# def home(request):
#     if request.method == "GET":
#         return render(request, "home.html")

class Home(View):       # inheritance of View
    def get(self, request):     # get method for get request
        user_obj = request.user
        fname =  request.session['fname']
        return render(request, 'home.html', {'user':user_obj, 'fname':fname})

class Login(View):
    def get(self,request,*args,**kwargs):
        return render(request, "login.html")
    def post(self,request,*args,**kwargs):
        email=request.POST.get("email")
        fname = email.split('@')[0]
        pswd =request.POST.get("psw")
        return HttpResponse("Hi "+fname+",<br>Username: "+email+"<br>Password: "+pswd)
    
class Add(View):
    def get(self,request, *args, **kwargs):
        return render(request, "addition.html")
    def post(self,request, *args, **kwargs):
        f = request.POST.get("fnum")
        s = request.POST.get("snum")
        res = int(f)+int(s)
        return render(request, "addition.html", {"data":res})

 
# class Count_word(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "num_words.html")
#     def post(self, request, *args, **kwargs):
#         sentence = request.POST.get("sntc")
#         words = sentence.split()
#         count = {}
#         for i in words:
#             if i in count:
#                 count[i] += 1
#             else:
#                 count[i] = 1
#         return render(request, "num_words.html", {"data":count})

class Count_word(View):
    def get(self, request, *args, **kwargs):
        form = CountForm()
        return render(request, "num_words.html", {"form":form})
    def post(self, request, *args, **kwargs):
        form_data = CountForm(data=request.POST)
        if form_data.is_valid():    # is_valid form class Form
            sentence = form_data.cleaned_data.get("text")
            words = sentence.split()
            count = {}
            for i in words:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1
            # return render(request, "num_words.html", {"form":form, "data":count})
            return redirect("home")     # after submition go to Home page : url_name
        else:
            # return HttpResponse(form_data.errors)
            return render(request, "num_words.html", {"form":form_data})            
     
class Calculator(View):
    def get(self, request, *args, **kwargs):
        user_obj = request.user
        return render(request, "calculator.html", {'user':user_obj})
    def post(self, request, *args, **kwargs):
        value = request.POST.get("line")
        return render(request, "calculator.html", {"data": eval(value)})
    
# The following classes using django.forms to create forms
class Registration(View):
    def get(self, request,*args, **kwargs):
        form = RegForm()   # constructor calling : constructed an object in RegiForm()
        return render(request, "reg.html", {"form":form})
    def post(self, request, *args, **kwargs):
        # form = LogForm()    # constructed an object in LogForm()
        # return render(request, "log.html", {"form":form, "alert": "Submitted"})
        # print(request.POST)
        form_data = RegForm(data=request.POST)
        if form_data.is_valid():    # is_valid form class Form
            print(form_data.cleaned_data)   # cleaned_data make dict of inputs
            print(form_data.cleaned_data.get("first_name")) 
            fname = form_data.cleaned_data.get("first_name")
            lname = form_data.cleaned_data.get("last_name")
            uname = form_data.cleaned_data.get("user_name")
            email = form_data.cleaned_data.get("email")
            psw = form_data.cleaned_data.get("password")
            age = form_data.cleaned_data.get("age")
            Employee.objects.create(firstname = fname, lastname = lname, username = uname, email = email, password = psw, age = age)
            messages.success(request, "Registration succesfull")
            messages.info(request, "You can Login now")
            return redirect('home')
        else:
            messages.error(request, "Registration failed")
            # return HttpResponse(form_data.errors)
            return render(request, "reg.html", {"form": form_data})

class Login_form(View):
    def get(self, request, *args, **kwargs):
        form = LogForm()
        return render(request, "log.html", {"form":form})
    def post(self, request, *args, **kwargs):
        form_data = LogForm(data=request.POST)
        if form_data.is_valid():    # is_valid form class Form
            messages.success(request, "Login succesfull")
            return render(request, "profile.html")
        else:
            messages.error(request, "Login failed")
            return render(request, "log.html", {"form":form_data})
        
class Emp_details(View):
    def get(self, request, *args, **kwargs):
        data = Employee.objects.all()
        return render(request, "emp_table.html" , {"data":data})

class Emp_delete(View):
    def get(self, request, *args, **kwargs):
        eid = kwargs.get('eid')
        emp = Employee.objects.get(id=eid)
        emp.delete()
        messages.success(request, "Employee deleted")
        return redirect("emp_data")
  
class Emp_update(View):
    def get(self, request, *args, **kwargs):
        eid= kwargs.get("eid")
        emp = Employee.objects.get(id=eid)
        form = RegForm(initial={"first_name":emp.firstname,"last_name":emp.lastname,"email":emp.email,"age":emp.age,"user_name":emp.username, })
        return render(request, 'emp_update.html', {"form":form})
    def post(self, request, *args, **kwargs):
        id = kwargs.get("eid")
        emp = Employee.objects.get(id=id)
        form_data = RegForm(data=request.POST)
        if form_data.is_valid():
            fname = form_data.cleaned_data.get("first_name")
            lname = form_data.cleaned_data.get("last_name")
            uname = form_data.cleaned_data.get("user_name")
            email = form_data.cleaned_data.get("email")
            age = form_data.cleaned_data.get("age")
            emp.firstname = fname
            emp.lastname = lname
            emp.username = uname
            emp.email = email
            emp.age = age
            emp.save()
            messages.success(request, "Employee updated")
            return redirect("emp_data")
        else:
            return render(request, "emp_update.html", {"form":form_data})


class Mng_reg(View):
    def get(self, request, *args, **kwargs):
        form = Mng_ModelForm()
        return render(request, "manager_reg.html", {"form":form})
    def post(self, request, *args, **kwargs):
        form_data = Mng_ModelForm(data=request.POST, files=request.FILES)  # request.POST only reading plain texts
        fn = request.POST.get("first_name")
        request.session['fname']=fn     # go to home
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Manager data added")
            return redirect("home")
        else:
            return render(request, "manager_reg.html", {"from":form_data})

class Mng_table(View):
    def get(self, request, *args, **kwargs):
        data = Mng_model.objects.all()
        return render(request, "mng_table.html", {"data":data})

class Mng_delete(View):
    def get(self, request, *args, **kwargs):
        mid = kwargs.get('mid')
        mng = Mng_model.objects.get(id=mid).first_name
        Mng_model.objects.filter(id=mid).delete() 
        messages.success(request, "%s deleted"%mng)
        return redirect("mng_data")

class Mng_update(View):
    def get(self, request, *args, **kwargs):
        mid = kwargs.get("mid")
        mng = Mng_model.objects.get(id=mid)
        form = Mng_ModelForm(instance=mng)  # instace attribute refer to assign values of mng obj to form fields
        return render(request, "mng_update.html", {"form":form})
    def post(self, request, *args, **kwargs):
        mid = kwargs.get("mid")
        mng = Mng_model.objects.get(id=mid)
        form_data = Mng_ModelForm(data=request.POST, files=request.FILES, instance=mng)
        if form_data.is_valid():
            mng_name = mng.first_name
            form_data.save()
            messages.success(request, "Manager:%s data added"%mng_name)
            return redirect("mng_data")
        else:
            return render(request, "mng_update.html", {"form":form_data}) 

# admin and user 
# for User
class SignUp(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, "SignUp.html", {"form":form})
    def post(self, request, *args, **kwargs):
        form_data = SignUpForm(data = request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Registration Success")
            return redirect('home')
        else:
            return render(request, "SignUP.html", {"form":form_data})
        
from django.contrib.auth import authenticate
class SignIn(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, "SignIn.html", {"form":form})
    def post(self, request, *args, **kwargs):
        form_data = SignInForm(data = request.POST)
        if form_data.is_valid():
            uname = form_data.cleaned_data.get("username")
            pswd = form_data.cleaned_data.get("password")
            user = authenticate(request, username= uname, password = pswd)
            if user:
                login(request, user)
                messages.success(request, "Sign in completed")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or Password")
                return render(request, "SignIn.html", {"form":form_data})
        else:
            return render(request, "SignIn.html", {"form":form_data})



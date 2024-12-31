from django.shortcuts import render
from .models import *
# from django.http import HttpResponse

# Create your views here.

# def about(request):
#     return render(request,"testapplication/about.html")

# def contact(request):
#     return render(request,"testapplication/contact.html")

# def profile(request):
#     return render(request, "testapplication/profilepage.html")

def home(request):
    return render(request,"testapplication/index.html")

def login(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id = uid)
            context = {
                "uid" : uid,
                "cid" : cid,
            }
            return render(request,"testapplication/index.html",context)
    else:
        if request.POST:
            print("------->button clicked")
            email = request.POST['email']
            password = request.POST['password']
            print("------>email",email)
            print("------->password",password)

            # print("-------->uid: ",uid)
            # print("-------->role: ",uid.role)
            # print("-------->password: ",uid.password)
            try:
                uid = User.objects.get(email = email)
                print("uid: ",uid.email)
                if uid.password == password:
                    if uid.role == "Chairman":
                        cid = Chairman.objects.get(user_id = uid)
                        print("welcome chairman")
                        context = {
                            "uid" : uid,
                            "cid" : cid,
                        }
                        # store email in session
                        request.session['email'] = email
                        return render(request,"testapplication/index.html",context)
                    else:
                        print("welcome member")
                else:
                    e_msg = "invalid password"
                    return render(request,"testapplication/login.html",{'e_msg' : e_msg})
            except Exception as e:
                print("ERROR: ",e)
                e_msg = "invalid email"
                return render(request,"testapplication/login.html",{'e_msg' : e_msg})
        else:
            print("--------->only page refresh")
        return render(request, "testapplication/login.html")

def profile(request):
    return render(request,"testapplication/profile.html")

def logout(request):
    if "email" in request.session:
        del request.session["email"]
        return render(request,"testapplication/login.html")
    else:
        return render(request,"testapplication/login.html")
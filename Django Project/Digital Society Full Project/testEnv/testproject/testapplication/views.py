from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random
from .utils import *

# Create your views here.

# def about(request):
#     return render(request,"testapplication/about.html")

# def contact(request):
#     return render(request,"testapplication/contact.html")

# def profile(request):
#     return render(request, "testapplication/profilepage.html")

def index(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        mcount = Members.objects.all().count()
        n_count = Notice.objects.all().count()

        context = {
            'uid' : uid,
            'cid' : cid,
            'mcount' : mcount,
            'n_count' : n_count
        }
        return render(request,"testapplication/index.html",context)
    else:
        return render(request,"testapplication/index.html")

def member_index(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        mid = Members.objects.get(user_id = uid)
        mcount = Members.objects.all().count()
        n_count = Notice.objects.all().count()

        context = {
            'uid' : uid,
            'mid' : mid,
            'mcount' : mcount,
            'n_count' : n_count
        }
        return render(request,"testapplication/member_index.html",context)
    else:
        return render(request,"testapplication/member_index.html")

def login(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == 'Chairman':
            cid = Chairman.objects.get(user_id=uid)
            mcount = Members.objects.all().count()
            n_count = Notice.objects.all().count()

            context = {
                'uid': uid,
                'cid': cid,
                'mcount': mcount,
                'n_count': n_count,
            }
            return render(request, "testapplication/index.html", context)
        else:
            mid = Members.objects.get(user_id=uid)
            mcount = Members.objects.all().count()
            n_count = Notice.objects.all().count()
            context = {
                'uid': uid,
                'mid': mid,
                'mcount': mcount,
                'n_count': n_count,
            }
            return render(request, "testapplication/member_index.html", context)
    else:
        if request.method == "POST":
            print("------->button clicked")
            email = request.POST.get('email')
            password = request.POST.get('password')
            print("------>email", email)
            print("------->password", password)

            try:
                uid = User.objects.get(email=email)
                print("uid: ", uid.email)
                if uid.password == password:
                    if uid.role == "Chairman":
                        cid = Chairman.objects.get(user_id=uid)
                        print("welcome chairman")
                        context = {
                            "uid": uid,
                            "cid": cid,
                        }
                        # Store email in session
                        request.session['email'] = email
                        return render(request, "testapplication/index.html", context)
                    else:
                        print("welcome member")
                        mid = Members.objects.get(user_id=uid)
                        context = {
                            "uid": uid,
                            "mid": mid,
                        }
                        # Store email in session
                        request.session['email'] = email
                        return render(request, "testapplication/member_index.html", context)
                else:
                    e_msg = "Invalid password"
                    return render(request, "testapplication/login.html", {'e_msg': e_msg})
            except Exception as e:
                print("ERROR: ", e)
                e_msg = "Invalid email"
                return render(request, "testapplication/login.html", {'e_msg': e_msg})

        else:
            print("--------->only page refresh")
            return render(request, "testapplication/login.html")

def profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)
            context = {
            'uid' : uid,
            'cid' : cid
            }
            return render(request,"testapplication/profile.html",context)
        else:
            mid = Members.objects.get(user_id = uid)
            context = {
                'uid' : uid,
                'mid' : mid,
            }
            return render(request,"testapplication/member_profile.html",context)
    else:
        return render(request,"testapplication/login.html")

def logout(request):
    if "email" in request.session:
        del request.session["email"]
        return render(request,"testapplication/login.html")
    else:
        return render(request,"testapplication/login.html")

def notfound(request):
    print("not found page")
    return render(request,"testapplication/page404.html")

def change_password(request):
    if request.POST:
        currentPassword = request.POST['currentpassword']
        newPassword = request.POST['newpassword']

        uid = User.objects.get(email = request.session['email'])

        if uid.password == currentPassword:
            uid.password = newPassword
            uid.save() # update
            del request.session['email']
            s_msg = "Successfully password Reset. Please Login again"
            return render(request,"testapplication/login.html",{'s_msg': s_msg})
        else:
            e_msg = "Invaild password"
            del request.session['email'] # logout logic
            return render(request,"testapplication/login.html",{'e_msg': e_msg})
    else:
        return render(request,"testapplication/login.html")


def update_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)
            if request.POST:
                cid.firstname = request.POST['firstname']
                cid.lastname = request.POST['lastname']
                cid.contact_no = request.POST['contact_no']
                if "pic" in request.FILES:
                    cid.pic = request.FILES['pic']
                    cid.save()
                    print("------>>>> working")

                cid.save()
                context = {
                    "uid" : uid,
                    "cid" : cid,
                }
                return render(request,"testapplication/profile.html",context)
        else:
            mid = Members.objects.get(user_id = uid)
            if request.POST:
                mid.firstname = request.POST['firstname']
                mid.lastname = request.POST['lastname']
                mid.contact_no = request.POST['contact_no']
                if "pic" in request.FILES:
                    mid.pic = request.FILES['pic']
                    mid.save()
                    print("------>>>> working")

                mid.save()
                context = {
                    "uid" : uid,
                    "mid" : mid,
                }
                return render(request,"testapplication/member_profile.html",context)
    else:
        return render(request,"testapplication/login.html")

def add_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            contact_no = request.POST['contact_no']
            email = request.POST['email']

            l1 = ["CS8234d","df74f","SD83f","DF843F","VC8SD","4FAS4","F8CE","E84FDFD"]
            password = email[3:6] + random.choice(l1) + contact_no[3:6]

            user_id = User.objects.create(email = email,password = password,role="member")
            m_id = Members.objects.create(
                user_id = user_id,
                house_no = request.POST['house_no'],
                block_no = request.POST['block_no'],
                firstname = request.POST['firstname'],
                lastname = request.POST['lastname'],
                contact_no = contact_no,
                no_family_members = request.POST['no_family_members'],
                vehicle_details = request.POST['vehicle_details'],
                blood_group = request.POST['blood_group'],
                job_description = request.POST['job_description'],
                job_address = request.POST['job_address'],
                pic = request.FILES['pic'] 
                )
                
            if m_id:
                s_msg = "Successfully member created!"
                context = {
                    "uid" : uid,
                    "cid" : cid,
                    "s_msg" : s_msg
                }
                mySendMail("Authentication","mail_template_password",[email],password)
            else:
                e_msg = "Failed to create member!"
                context = {
                    "uid" : uid,
                    "cid" : cid,
                    "e_msg" : e_msg
                }
            return render(request,"testapplication/add_member.html",context)
        context = {
            "uid": uid,
            "cid": cid,
        }
        return render(request, "testapplication/add_member.html", context)
    else:
        return render(request,"testapplication/add_member.html")


def all_members(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)

            # Fetch members for all block
            m_all = Members.objects.all() # fetch all society members from the member model
            a_block = Members.objects.filter(block_no='A')
            b_block = Members.objects.filter(block_no='B')
            c_block = Members.objects.filter(block_no='C')
            d_block = Members.objects.filter(block_no='D')

            context = {
                "uid": uid,
                "cid": cid,
                "m_all" : m_all,
                "a_block": a_block,
                "b_block": b_block,
                "c_block": c_block,
                "d_block": d_block,
            }
            return render(request,"testapplication/members.html", context)
        else:
            mid = Members.objects.get(user_id = uid)

            # Fetch members for all block
            m_all = Members.objects.all() # fetch all society members from the member model
            a_block = Members.objects.filter(block_no='A')
            b_block = Members.objects.filter(block_no='B')
            c_block = Members.objects.filter(block_no='C')
            d_block = Members.objects.filter(block_no='D')

            context = {
                "uid": uid,
                "mid": mid,
                "m_all" : m_all,
                "a_block": a_block,
                "b_block": b_block,
                "c_block": c_block,
                "d_block": d_block,
            }
            return render(request,"testapplication/member_view_members.html", context)
    else:
        return render(request,"testapplication/login.html")


def add_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            if "pic" in request.FILES:
                nid = Notice.objects.create(
                    user_id = uid,
                    notice_title = request.POST['notice_title'],
                    notice_description = request.POST['notice_description'],
                    notice_category = request.POST['notice_category'],
                    pic = request.FILES['pic']
                )
                s_msg = "Successfully Notice created!"
                context = {
                    "uid" : uid,
                    "cid" : cid,
                    "s_msg" : s_msg
                }
                return render(request,"testapplication/add-notice.html",context)
            else:
                nid = Notice.objects.create(
                    user_id = uid,
                    notice_title = request.POST['notice_title'],
                    notice_category = request.POST['notice_category'],
                    notice_description = request.POST['notice_description']
                )

                all_members = User.objects.filter(role="member")
                print("======>>",all_members)
                all_member_email_list = []
                for member in all_members:
                    all_member_email_list.append(member.email)
                print("======>>email list: ",all_member_email_list)
                
                mySendMail("New Notice Notification","notice_template",all_member_email_list,request.POST['notice_description'])
                
                s_msg = "Successfully Notice created!"
                context = {
                    "uid" : uid,
                    "cid" : cid,
                    "s_msg" : s_msg
                }
                return render(request,"testapplication/add-notice.html",context)
        else:
            context = { 
            "uid": uid,
            "cid": cid,
            }
            return render(request, "testapplication/add-notice.html", context)
    else:
        return render(request,"testapplication/login.html")


def view_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)

            nall = Notice.objects.all().order_by("-created_at")
            context = { 
                "uid": uid,
                "cid": cid,
                "nall" : nall
                }
            return render(request,"testapplication/notice-list.html",context)
        else:
            mid = Members.objects.get(user_id = uid)

            nall = Notice.objects.all().order_by("-created_at")
            context = { 
                "uid": uid,
                "mid": mid,
                "nall" : nall
                }
            return render(request,"testapplication/member_notice-list.html",context)
    else:
        return render(request,"testapplication/login.html")


def del_notice(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        nid = Notice.objects.get(id = pk)
        nid.delete()

        nall = Notice.objects.all().order_by("-created_at")
        context = { 
            "uid": uid,
            "cid": cid,
            "nall" : nall
            }
        return render(request,"testapplication/notice-list.html",context)


def edit_notice(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        nid = Notice.objects.get(id = pk)
        context = { 
            "uid": uid,
            "cid": cid,
            "nid" : nid
            }
        return render(request,"testapplication/edit-notice.html",context)

def update_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        if request.POST:
            nid = request.POST['nid']
            notice_title = request.POST['notice_title']
            notice_description = request.POST['notice_description']

            notice_id = Notice.objects.get(id = nid)
            
            notice_id.notice_title = notice_title
            notice_id.notice_description = notice_description

            notice_id.save()

            if "pic" in request.FILES:
                pic = request.FILES['pic']
                notice_id.pic = pic
                notice_id.save()
            
            nall = Notice.objects.all().order_by("-created_at")
            context = { 
                "uid": uid,
                "cid": cid,
                "nall" : nall
                }
            return render(request,"testapplication/notice-list.html",context)
        else:
            context = { 
                "uid": uid,
                "cid": cid,
                }
            return render(request,"testapplication/index.html",context)


def forgot_password(request):
    if request.POST:
        email = request.POST['email']
        try:
            uid = User.objects.get(email = email)
            otp = random.randint(1111,9999)
            uid.otp = otp
            uid.save() # update
            mySendMail("Forgot Password","mail_template_otp",[email],otp)
            context = {
                'email' : email
            }
            return render(request,"testapplication/reset_password.html",context)
        except Exception as e:
            print("===========>>Exception:   ",e)
            context = {
                'email' : "Invalid email address"
            }
            return render(request,"testapplication/forgot_password.html",context)
    else:
        return render(request,"testapplication/forgot_password.html")


def reset_password(request):
    if request.POST:
        email = request.POST['email']
        otp = request.POST['otp']
        newpassword = request.POST['newpassword']
        repassword = request.POST['repassword']

        uid = User.objects.get(email = email)
        
        if str(uid.otp) == otp:
            if newpassword == repassword:
                uid.otp = random.randint(1111,9999)
                uid.password = newpassword
                uid.save()

                context = {
                    's_msg' : "Successfully password reset!"
                }
                return render(request,"testapplication/login.html",context)
            else:
                context = {
                    'e_msg' : "New password and re-password didn't match"
                }
                return render(request,"testapplication/reset_password.html",context)
        else:
            context = {
                'e_msg' : "Invalid OTP"
            }
            return render(request,"testapplication/login.html",context)
    else:
        return render(request,"testapplication/login.html")

def add_event(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        if request.POST:
            eid = Event.objects.create(
                user = uid,
                event_title = request.POST['event_title'],
                event_description = request.POST['event_description'],
                event_location = request.POST['event_location'],
                event_date = request.POST['event_date'],
                event_time = request.POST['event_time'],
            )
            s_msg = "Successfully Event created!"
            context = {
                "uid" : uid,
                "cid" : cid,
                "s_msg" : s_msg
            }
            return render(request,"testapplication/add-event.html",context)
        else:
            context = { 
            "uid": uid,
            "cid": cid,
            }
            return render(request, "testapplication/add-event.html", context)
    else:
        return render(request,"testapplication/login.html")


def view_event(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Chairman":
            cid = Chairman.objects.get(user_id = uid)

            eall = Event.objects.all().order_by("-created_at")
            context = { 
                "uid": uid,
                "cid": cid,
                "eall" : eall
                }
            return render(request,"testapplication/event_list.html",context)
        else:
            mid = Members.objects.get(user_id = uid)

            eall = Event.objects.all().order_by("-created_at")
            context = { 
                "uid": uid,
                "mid": mid,
                "eall" : eall
                }
            return render(request,"testapplication/member_event_list.html",context)
    else:
        return render(request,"testapplication/login.html")


def add_complaints(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        mid = Members.objects.get(user_id = uid)
        if request.POST:
            complaint_id = Complaint.objects.create(
                user = uid,
                member=mid,
                complaint_title = request.POST['complaint_title'],
                complaint_text = request.POST['complaint_text']
            )
            s_msg = "Successfully Complaint sent!"
            context = {
                "uid" : uid,
                "mid" : mid,
                "s_msg" : s_msg
            }
            return render(request,"testapplication/add-complaint.html",context)
        else:
            context = {
            "uid": uid,
            "mid": mid,
            }
            return render(request, "testapplication/add-complaint.html", context)
    else:
        return render(request,"testapplication/login.html")


def view_complaints(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        call = Complaint.objects.all().order_by("-created_at")
        context = { 
            "uid": uid,
            "cid": cid,
            "call" : call
            }
        return render(request,"testapplication/complaints.html",context)
    else:
        return render(request,"testapplication/index.html")
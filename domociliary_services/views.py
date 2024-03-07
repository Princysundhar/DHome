import datetime
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from domociliary_services.models import *
# Create your views here.


def login_table(request):
    return render(request,'index.html')

def login_post(request):
    un=request.POST['textfield']
    pa=request.POST['textfield2']
    res=login.objects.filter(username=un,password=pa)
    if res.exists():
        request.session['lid']=res[0].id
        request.session['lg']="lin"
        if res[0].usertype=='admin':
            return redirect('/admin_home')
        if res[0].usertype=='staff':
            return redirect('/Staff_home')
        else:
            return HttpResponse('<script>alert("invalid");window.location="/"</script>')
    else:
        return HttpResponse('<script>alert("no such user");window.location="/"</script>')


def logout(request):
    request.session['lg'] = ""
    return HttpResponse('<script>alert("logout sucessful");window.location="/"</script>')

def admin_home(request):
    return render(request,'Admin_module/admin_index.html')

# CATEGORY MANAGEMENT................

def add_category(request):
    return render(request,'Admin_module/admcategory.html')

def add_category_post(request):
    ct=request.POST['textfield']
    obj=category()
    obj.category_name=ct
    obj.save()
    return HttpResponse('<script>alert("Added successfully");window.location="/admin_home"</script>')

def view_category(request):
    ces=category.objects.all()
    return render(request,'Admin_module/viewcategry.html',{'data':ces})

def admin_edit_category(request,id):
    if request.session['lid'] == '':
        return HttpResponse('<script>alert("logout sucessful");window.location="/"</script>')
    else:
        res=category.objects.get(id=id)
        return render(request,"Admin_module/edit_category.html",{'id':id,'data':res})

def admin_edit_category_post(request,id):
    ct = request.POST['textfield']
    category.objects.filter(id=id).update(category_name=ct)
    return HttpResponse('<script>alert("updated");window.location="/view_category"</script>')

def delete_category(request,id):
    category.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("updated");window.location="/view_category"</script>')

# ........... STAFF MANAGEMENT .....................

def add_staff(request):
    return render(request,'Admin_module/addstaff.html')

def add_staff_post(request):
    st=request.POST['textfield']
    po=request.POST['textfield2']
    pl=request.POST['textfield3']
    pin=request.POST['textfield4']
    cn=request.POST['textfield5']
    ema=request.POST['textfield6']
    lati = request.POST['textfield8']
    longi = request.POST['textfield9']
    ps=random.randint(0000,9999)

    obj1=login()
    obj1.username=ema
    obj1.password=ps
    obj1.usertype='staff'
    obj1.save()

    obj=staff()
    obj.staffname=st
    obj.staffpost=po
    obj.staffplace=pl
    obj.staffpin=pin
    obj.staffcontact_no=cn
    obj.staffemail=ema
    obj.stafflatitude = lati
    obj.stafflongitude = longi
    obj.LOGIN=obj1
    obj.save()

    import smtplib

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("digitalhome108@gmail.com", "klvz fbnw tgzk muuw")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "digitalhome108@gmail.com"
    msg['To'] = ema
    msg['Subject'] = "Your Login Password for D-Home is"
    body = "Your Password is:- - " + str(ps)
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)

    return HttpResponse('<script>alert("Added successfully");window.location="/admin_home"</script>')


def view_staff(request):
    stf=staff.objects.all()
    return render(request,'Admin_module/viewstaff.html',{'data':stf})

def admin_edit_staff(request,id):
    if request.session['lid'] == '':
        return HttpResponse('<script>alert("logout sucessful");window.location="/"</script>')
    else:
        ree=staff.objects.get(id=id)
        return render(request,"Admin_module/edit_staff.html",{'id':id,'data':ree})

def admin_edit_staff_post(request,id):
    st = request.POST['textfield']
    po = request.POST['textfield2']
    pl = request.POST['textfield3']
    pin = request.POST['textfield4']
    cn = request.POST['textfield5']
    ema = request.POST['textfield6']
    staff.objects.filter(id=id).update(staffname=st ,staffpost=po,staffplace=pl,staffpin=pin,staffcontact_no=cn,staffemail=ema)
    return HttpResponse('<script>alert("updated");window.location="/view_staff"</script>')

def delete_staff(request,id):
    staff.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("updated");window.location="/view_staff"</script>')

#..........AREA MANAGEMENT ..................


def add_area(request):
    return render(request,'Admin_module/addcity.html')

def add_area_post(request):
    ar=request.POST['textfield']
    obj=area()
    obj.cityname=ar
    obj.save()
    return HttpResponse('<script>alert("Added successfully");window.location="/admin_home"</script>')


def view_area(request):
    res=area.objects.all()
    return render(request,'Admin_module/viewarea.html',{'data':res})

def admin_edit_city(request,id):
    if request.session['lid'] == '':
        return HttpResponse('<script>alert("logout sucessful");window.location="/"</script>')
    else:
        re=area.objects.get(id=id)
        return render(request,"Admin_module/edit_city.html",{'id':id,'data':re})

def admin_edit_city_post(request,id):
    ar = request.POST['textfield']
    area.objects.filter(id=id).update(cityname=ar)
    return HttpResponse('<script>alert("updated");window.location="/view_area"</script>')

def delete_city(request,id):
    area.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("updated");window.location="/view_area"</script>')


# ..........AREA ALLOCATION ............




# def allocate_service(request):
#     return render(request,'Admin_module/allctsrvctostff.html')

def area_allocation(request):
    res=area.objects.all()
    ree=staff.objects.all()
    return render(request,'Admin_module/areaallocationtostaf.html',{'data':res,'data1':ree})

def area_allocation_post(request):
    area=request.POST['select']
    staff=request.POST['select2']
    obj=areaallocation()
    obj.AREA_id=area
    obj.STAFF_id=staff
    obj.save()
    return HttpResponse('<script>alert("Added successfully");window.location="/admin_home"</script>')

def area_allocated(request):
    res=areaallocation.objects.all()
    print(res)
    return render(request,'Admin_module/viewareaallocation.html',{'data':res})

def delete_allocation(request,id):
    areaallocation.objects.get(id=id).delete()
    return HttpResponse('<script>alert("Deleted successfully");window.location="/admin_home"</script>')

# ................SERVICE MANAGEMNT ...........

def add_service(request):
    res=category.objects.all()
    return render(request,'Admin_module/add service.html',{'data':res})

def add_service_post(request):
    service_name=request.POST['textfield']
    amount=request.POST['amount']
    CATEGORY=request.POST['cat']
    obj=service()
    obj.service_name=service_name
    obj.amount=amount
    obj.CATEGORY_id=CATEGORY
    obj.save()
    return HttpResponse('<script>alert("Added successfully");window.location="/admin_home"</script>')

def view_service(request):
    res=service.objects.all()
    print(res)
    return render(request,'Admin_module/viewservice.html',{'data':res})

def edit_service(request,id):
    if request.session['lid'] == '':
        return HttpResponse('<script>alert("logout sucessful");window.location="/"</script>')
    else:
        res=service.objects.get(id=id)
        r=category.objects.all()
        return render(request,'Admin_module/editservice.html',{'data':r,'id':res})
def edit_service_post(request,id):
    service_name = request.POST['textfield']
    amount = request.POST['amount']
    CATEGORY = request.POST['cat']
    service.objects.filter(id=id).update(service_name=service_name,amount=amount,CATEGORY=CATEGORY)
    return HttpResponse('<script>alert("Edited successfully");window.location="/admin_home"</script>')

def delete_service(request,id):
    service.objects.filter(id=id).delete()
    return HttpResponse('<script>alert("Deleted successfully");window.location="/admin_home"</script>')


def view_request(request):
    res=requestss.objects.all()
    return render(request,'Admin_module/viewrequest.html',{'data':res})

def alct_staff(request,id):
    if request.session['lid'] == '':
        return HttpResponse('<script>alert("logout sucessful");window.location="/"</script>')
    else:
        ree=staff.objects.all()
        return render(request,'Admin_module/allctsrvctostff.html',{'data':ree,'id':id})

def alct_staff_post(request,id):
    staff=request.POST['select']
    import datetime
    obj=allocate_service()
    obj.STAFF_id=staff
    obj.REQUEST_id=id
    obj.status='pending'
    obj.date=datetime.datetime.now().strftime("%Y-%m-%d")
    obj.save()
    return HttpResponse('<script>alert("Added successfully");window.location="/admin_home"</script>')



#
# def view_allocatedservice(request):
#     return render(request,'Admin_module/viewallctdservce.html')

def view_allocation(request):
    res=allocate_service.objects.filter(status='pending')
    return render(request,'Admin_module/viewallocation.html',{'data':res})

def view_payment(request,id):
    pay=payment.objects.filter(REQUEST_id=id)
    return render(request,'Admin_module/view_payment.html',{'data':pay})


def cancel_allocation_status(request,id):
    allocate_service.objects.filter(id=id).update(status='cancelled')
    return HttpResponse('<script>alert("cancelled");window.location="/admin_home"</script>')





# ================================================================================================ STAFF MOFULE

def Staff_home(request):
    return render(request,'staff_module/staff_index.html')

def view_profile(request):
    res=staff.objects.get(LOGIN=request.session['lid'])
    return render(request,'staff_module/view profile.html',{'data':res})

def view_allocated_area(request):
    re=areaallocation.objects.filter(STAFF__LOGIN_id=request.session['lid'])
    return render(request,'staff_module/view_allocated_area.html',{'data':re})

def view_allocated_work_verify(request):
    res=allocate_service.objects.filter(STAFF__LOGIN_id=request.session['lid'],status='pending')
    return render(request,'staff_module/view_allocated_work_verify.html',{"data":res})

def approve(request,id):
    allocate_service.objects.filter(id=id).update(status='Approved')
    return HttpResponse('<script>alert("Approved successfully");window.location="/view_allocated_work_verify"</script>')

def reject(request,id):
    allocate_service.objects.filter(id=id).update(status='Rejected')
    return HttpResponse('<script>alert("Rejected");window.location="/view_allocated_work_verify"</script>')


def view_allocated_work_verified(request):
    res=allocate_service.objects.filter(STAFF__LOGIN_id=request.session['lid'],status='Approved')
    return render(request,'staff_module/view_allocated_work_verified.html',{"data":res})

def update_status(request,id):
    requestss.objects.filter(id=id).update(status='completed')
    return HttpResponse('<script>alert("Status Updated");window.location="/view_allocated_work_verified"</script>')




# ..................................................................................... CUSTOMER (ANDROID)

def and_login(request):
    username = request.POST['username']
    password = request.POST['password']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        lid = data[0].id
        type = data[0].usertype
        res = customer.objects.get(LOGIN=lid)
        name = res.name
        email = res.email
        # photo = res.image
        return JsonResponse({"status":"ok","lid":lid,"type":type,"name":name,"email":email})
    else:
        return JsonResponse({"status":None})


def android_user_registration(request):
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['phone']
    password = request.POST['password']
    image = request.FILES['pic']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\my_home\domociliary_services\static\photo\\" + dt + '.jpg',image)
    path = '/static/photo/' + dt + '.jpg'
    data = login.objects.filter(username=email,password=password)
    if data.exists():
        return HttpResponse("<script>alert('Already exists');window.location='/'</script>")
    else:

        log_obj = login()
        log_obj.username = email
        log_obj.password = password
        log_obj.usertype = 'user'
        log_obj.save()

        obj = customer()
        obj.name = name
        obj.email = email
        obj.phone = contact
        obj.image = path
        obj.LOGIN = log_obj
        obj.save()
        return JsonResponse({"status":"ok"})

def android_change_password(request):
    lid = request.POST['lid']
    current_password = request.POST['crp']
    new_password = request.POST['new_password']
    confirm_password =request.POST['confirm_password']
    data = login.objects.filter(password=current_password,id= lid)
    if data.exists():
        if new_password == confirm_password:
            if login.objects.filter(password=new_password).exists():
                return JsonResponse({"status":"No"})
            else:
                login.objects.filter(id=lid).update(password=confirm_password)
                return JsonResponse({"status":"ok"})
        else:
            return JsonResponse({"status":"mismatch"})
    else:
        return JsonResponse({"status":"error"})


def customer_view_category(request):
    res = category.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "cid":i.id,
                "category_name":i.category_name
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def and_view_service(request):

    sid = request.POST['cid']
    res = service.objects.filter(CATEGORY=sid)
    ar = []
    for i in res:

        ar.append(
            {
                "sid":i.id,
                "category_name":i.CATEGORY.category_name,
                "service":i.service_name,
                "amount":i.amount
            }
        )
    return JsonResponse({"status":"ok","data":ar})


def and_send_request(request):
    sid = request.POST['sid']
    lid = request.POST['lid']
    amount = request.POST['amount']
    obj = requestss()
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.amount = amount
    obj.status = 'pending'
    obj.SERVICE_id = sid
    obj.CUSTOMER = customer.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({"status":"ok"})

def and_view_request(request):
    lid = request.POST['lid']
    res = requestss.objects.filter(CUSTOMER__LOGIN=lid,status='allocated')
    ar = []
    for i in res:
        ar.append(
            {
                "rid":i.id,
                "service_name":i.SERVICE.service_name,
                "category_name":i.SERVICE.CATEGORY.category_name,
                "date":i.date,
                "amount":i.amount
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def and_offline_payment(request):
    # mode = request.POST['mode']
    lid = request.POST['lid']
    rid = request.POST['rid']
    amount = request.POST['amount']
    obj = payment()
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.time = datetime.datetime.now().strftime("%H-%M-%S")
    obj.amount = amount
    obj.REQUEST_id = rid
    obj.CUSTOMER = customer.objects.get(LOGIN=lid)
    obj.payment_status = 'offline'
    obj.save()
    return JsonResponse({"status":"ok"})

def android_online_payment(request):
    # mode = request.POST['mode']
    lid = request.POST['lid']
    rid = request.POST['rid']
    amount = request.POST['amount']
    obj = payment()
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.time = datetime.datetime.now().strftime("%H-%M-%S")
    obj.amount = amount
    obj.REQUEST_id = rid
    obj.CUSTOMER = customer.objects.get(LOGIN=lid)
    obj.payment_status = 'online'
    obj.save()
    return JsonResponse({"status":"ok"})

def and_view_allocated_staff(request):
    res = areaallocation.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "aid":i.id,
                "staff_name":i.STAFF.staffname,
                "staff_latitude":i.STAFF.stafflatitude,
                "staff_longitude":i.STAFF.stafflongitude,
                "area_name":i.AREA.cityname
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def and_send_Feedback(request):
    feedbacks = request.POST['feedback']
    lid = request.POST['lid']
    obj = feedback()
    obj.feedback = feedbacks
    obj.date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.CUSTOMER = customer.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({"status":"ok"})

def and_view_feedback(request):
    lid = request.POST['lid']
    res = feedback.objects.filter(CUSTOMER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "fid":i.id,
                "feedback":i.feedback,
                "date":i.date,
                "name":i.CUSTOMER.name,
                "email":i.CUSTOMER.email
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def and_delete_feedback(request):
    fid = request.POST['fid']
    feedback.objects.get(id=fid).delete()
    return JsonResponse({"status":"ok"})




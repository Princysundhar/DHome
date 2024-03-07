from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)

class category(models.Model):
    category_name=models.CharField(max_length=200)


class staff(models.Model):
    staffname=models.CharField(max_length=200)
    staffpost=models.CharField(max_length=200)
    staffplace=models.CharField(max_length=200)
    staffpin=models.CharField(max_length=200)
    staffcontact_no=models.CharField(max_length=200)
    staffemail=models.CharField(max_length=200)
    stafflatitude=models.CharField(max_length=200)
    stafflongitude=models.CharField(max_length=200)

    LOGIN=models.ForeignKey(login,default=1,on_delete=models.CASCADE)


class area(models.Model):
    cityname=models.CharField(max_length=200)
    
class service(models.Model):
    CATEGORY = models.ForeignKey(category, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
class areaallocation(models.Model):
    AREA=models.ForeignKey(area, on_delete=models.CASCADE)
    STAFF=models.ForeignKey(staff, on_delete=models.CASCADE)


class customer(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    LOGIN= models.ForeignKey(login, on_delete=models.CASCADE)


class requestss(models.Model):
    date=models.CharField(max_length=200)
    amount=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    SERVICE=models.ForeignKey(service, on_delete=models.CASCADE)
    CUSTOMER= models.ForeignKey(customer, on_delete=models.CASCADE)


class allocate_service(models.Model):
    date=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    STAFF=models.ForeignKey(staff,on_delete=models.CASCADE)
    REQUEST=models.ForeignKey(requestss,on_delete=models.CASCADE)

class payment(models.Model):
    date=models.CharField(max_length=200)
    time=models.CharField(max_length=200)
    amount=models.CharField(max_length=200)
    payment_status=models.CharField(max_length=200)
    REQUEST= models.ForeignKey(requestss, on_delete=models.CASCADE)
    CUSTOMER = models.ForeignKey(customer, on_delete=models.CASCADE)

class feedback(models.Model):
    date=models.CharField(max_length=200)
    feedback=models.CharField(max_length=200)
    CUSTOMER=models.ForeignKey(customer, on_delete=models.CASCADE)

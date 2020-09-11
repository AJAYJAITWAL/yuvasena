from django.db import models


# Create your models here.
class Bio(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=200)
    wnumber = models.IntegerField()
    assembly = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    dob = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    Tenure = models.CharField(max_length=50)
    position = models.CharField(max_length=225)
    bgroup = models.CharField(max_length=225)
    education = models.CharField(max_length=225)
    pyear = models.IntegerField()
    occupation = models.CharField(max_length=225)
    anumber = models.IntegerField()
    img = models.ImageField()
    
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email



# Create your models here.
class Register(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=200)
    wnumber = models.IntegerField()
    assembly = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    dob = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    Tenure = models.CharField(max_length=50)
    position = models.CharField(max_length=225)
    bgroup = models.CharField(max_length=225)
    education = models.CharField(max_length=225)
    pyear = models.IntegerField()
    occupation = models.CharField(max_length=225)
    anumber = models.IntegerField()
    img = models.ImageField()
    
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email

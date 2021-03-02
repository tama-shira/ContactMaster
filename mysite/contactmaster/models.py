from django.db import models

# Create your models here.
class System(models.Model):
    env = models.CharField(max_length=200)
    identifier = models.CharField(max_length=10)
    system_name = models.CharField(max_length=500)
    start_date = models.DateTimeField(blank=True, null=True)
    tel = models.CharField(max_length=12)
    mail = models.CharField(max_length=12)
    #severity = models.CharField(max_length=200)
    remarks = models.CharField(max_length=500)
    business_day = models.CharField(max_length=18)
    business_hour_stat = models.TimeField(blank=True, null=True)
    business_hour_end = models.TimeField(blank=True, null=True)


    def __str__(self):
        return self.identifier + ' | ' + self.system_name

class NormalContact(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    no = models.IntegerField()
    deployment = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    tel_business_hours = models.CharField(max_length=200)
    tel_not_business_hours = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.system.system_name + ' | ' + str(self.no)

class FaultContact(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    no = models.IntegerField()
    deployment = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    tel_business_hours = models.CharField(max_length=200)
    tel_not_business_hours = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.system.system_name + ' | ' + str(self.no)

class LargeFaultContact(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    no = models.IntegerField()
    deployment = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    tel_business_hours = models.CharField(max_length=200)
    tel_not_business_hours = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.system.system_name + ' | ' + str(self.no)
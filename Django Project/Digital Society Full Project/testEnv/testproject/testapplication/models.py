from django.db import models
import math
from django.utils import timezone
# Create your models here.

# python manage.py makemigrations  (it will generate script of model file)
# python manage.py migrate         (it will execute script)

class User(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=20)
    otp = models.IntegerField(default=456)
    role = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=15)
    pic = models.FileField(upload_to='media/images/',default='media/defaultpic.png')

    def __str__(self):
        return self.firstname


class Members(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    house_no = models.CharField(max_length=10)
    block_no = models.CharField(max_length=10)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=15)
    no_family_members = models.CharField(max_length=15)
    vehicle_details = models.CharField(max_length=30)
    blood_group = models.CharField(max_length=20)
    job_description = models.CharField(max_length=30)
    job_address = models.TextField()
    pic = models.FileField(upload_to='media/images/',default='media/defaultpic.png')

    def __str__(self):
        return self.firstname + " " + self.lastname 


class Notice(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    notice_title = models.CharField(max_length=255)
    notice_category = models.CharField(max_length=100,default="Uncategorized")
    notice_description = models.TextField()
    pic = models.ImageField(upload_to='media/images/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.notice_title

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"
            else:
                return str(seconds) + "seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minute ago"
            else:
                return str(minutes) + "minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hour ago"
            else:
                return str(hours) + "hours ago"

        # 1 days to 30 days
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + "day ago"
            else:
                return str(days) + "days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "years ago"


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, default=None)
    event_title = models.CharField(max_length=255)
    event_description = models.TextField()
    event_location = models.CharField(max_length=255)
    event_date = models.DateField()
    event_time = models.TimeField()
    created_at = models.DateTimeField(auto_now=True)
    # likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.event_title

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"
            else:
                return str(seconds) + "seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minute ago"
            else:
                return str(minutes) + "minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hour ago"
            else:
                return str(hours) + "hours ago"

        # 1 days to 30 days
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + "day ago"
            else:
                return str(days) + "days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "years ago"


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, default=None)
    member = models.ForeignKey(Members, on_delete=models.CASCADE,null=True, blank=True, default=None)
    complaint_title = models.CharField(max_length=255)
    complaint_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.complaint_title

    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"
            else:
                return str(seconds) + "seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minute ago"
            else:
                return str(minutes) + "minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hour ago"
            else:
                return str(hours) + "hours ago"

        # 1 days to 30 days
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + "day ago"
            else:
                return str(days) + "days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "years ago"
from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

CHOICE_GENDER = ((1, 'Male'), (2, 'Female'))
CHOICE_account_type = ((1, "Individual"), (2, "Expert"))
# Create your models here.

class UserSettingModel(models.Model):
    name = models.CharField(max_length=100)
    gender = models.IntegerField(choices=CHOICE_GENDER)
    account_type = models.IntegerField(choices=CHOICE_account_type)
    birthday = models.DateField()
    age = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def get_user(self):
        birthday1= self.birthday
        today = date.today()
        age1 = today.year - birthday1.year -((today.month, today.day) < (birthday1.month, birthday1.day))
        return age1


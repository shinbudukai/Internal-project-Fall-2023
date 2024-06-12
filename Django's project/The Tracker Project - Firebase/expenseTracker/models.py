

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
#Create your models here.
SELECT_CATEGORY_CHOICES = [
    ("Food","Food"),
    ("Travel","Travel"),
    ("Shopping","Shopping"),
    ("Necessities","Necessities"),
    ("Entertainment","Entertainment"),
    ("Other","Other")
 ]
ADD_EXPENSE_CHOICES = [
     ("Expense","Expense"),
     ("Income","Income")
 ]
PROFESSION_CHOICES =[
    ("Employee","Employee"),
    ("Business","Business"),
    ("Student","Student"),
    ("Other","Other")
]
class Addmoney_info(models.Model):
    user = models.ForeignKey(User,default = 1, on_delete=models.CASCADE)
    add_money = models.CharField(max_length = 10 , choices = ADD_EXPENSE_CHOICES )
    quantity = models.BigIntegerField()
    Date = models.DateField(default = now)
    Category = models.CharField( max_length = 20, choices = SELECT_CATEGORY_CHOICES , default ='Food')
    class Meta:
        db_table:'addmoney'
        
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profession = models.CharField(max_length = 10, choices=PROFESSION_CHOICES)
    Savings = models.IntegerField( null=True, blank=True)
    income = models.BigIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image',blank=True)
    def __str__(self):
       return self.user.username

# FityFeed's models
# class Customer(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     name=models.CharField(max_length=200,null=True)
#     email=models.CharField(max_length=200,null=True)
#     date_created=models.DateTimeField(auto_now_add=True,null=True)
    
#     def __str__(self):
#         return str(self.name)

# class Category(models.Model):
#     options=(
#         ('breakfast','breakfast'),
#         ('lunch','lunch'),
#         ('dinner','dinner'),
#         ('snacks','snacks'),
#     )
#     name=models.CharField(max_length=50,choices=options)
#     def __str__(self):
#         return self.name

# class Fooditem(models.Model):
#     name = models.CharField(max_length=200)
#     category = models.ManyToManyField(Category)
#     carbohydrate = models.DecimalField(max_digits=5,decimal_places=2,default=0)
#     fats = models.DecimalField(max_digits=5,decimal_places=2,default=0)
#     protein = models.DecimalField(max_digits=5,decimal_places=2,default=0)
#     calorie=models.DecimalField(max_digits=5,decimal_places=2,default=0,blank=True)
#     quantity = models.IntegerField(default=1,null=True,blank=True)
    
#     def __str__(self):
#         return str(self.name)

# #for user page-------------------------------------------------------------
# class UserFooditem(models.Model):
#     customer = models.ManyToManyField(UserProfile,blank=True)   #(customer,blank=True)
#     fooditem=models.ManyToManyField(Fooditem)
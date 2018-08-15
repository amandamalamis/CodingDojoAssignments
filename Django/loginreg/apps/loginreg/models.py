from django.db import models

# Create your models here.

# class UserManager(models.Manager):
#    def basic_validator(self, postData):
#        errors = {}
#        if len(postData['first_name']) < 2:
#            errors["first_name"] = "First name should be at least 2 characters"
#        if len(postData['last_name']) < 2:
#            errors["last_name"] = "Last name should be at least 2 characters"
#        if not EMAIL_REGEX.match(postData['email']):
#            errors["email"] = "Invalid email"
#        if len(postData['password']) < 8:
#            errors["password"] = "Password should be at least 8 characters"
#        if postData['password'] != postData['conpassword']:
#            errors["conpassword"] = "Passwords must match"
#        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.TextField()
    password1= models.CharField(max_length=255)
    password2= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
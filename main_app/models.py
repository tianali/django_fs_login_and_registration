from django.db import models
import re

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-_]+\.[a-zA-]+$')

        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must be 2 characters or more.'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must be 2 characters or more.'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Email address invalid.'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters.'
        if postData['password'] != postData['confirm_pw']:
            errors['password'] = 'Passwords do not match'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class PublicSpeaking(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Sports(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class STEM(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class SummerCamps(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Tutoring(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class YouthEmployment(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
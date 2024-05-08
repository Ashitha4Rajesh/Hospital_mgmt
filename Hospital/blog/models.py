from django.db import models

class post(models.Model):
    category = ( 
    ("Covid19", "Covid19"), 
    ("Heart Disease", "Heart Disease"),
    ("Immunization","Immunization"), 
    ("Mental Health","Mental Health"),    
    ) 
    category = models.CharField(max_length=50,choices = category)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to="blog/")
    summary = models.TextField()
    content = models.TextField()
    draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.

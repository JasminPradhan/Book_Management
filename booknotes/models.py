from django.db import models

# Create your models here.

class Notes(models.Model):
    READING_STATUS={
        "To be Read":"To be Read",
        "Reading":"Reading",
        "Read":"Read"
    }
    title=models.TextField(null=True, blank=True)
    body=models.TextField(null=True, blank=True)
    author=models.TextField(null=True,blank=True)
    status=models.CharField(null=True, max_length=10, choices=READING_STATUS)
    updated = models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]
from email.policy import default
from django.db import models   
    
class Login(models.Model):
    
    senha = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False)
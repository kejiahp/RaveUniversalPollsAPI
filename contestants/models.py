from django.db import models
import secrets


#DEFINING THE PURCHASE REGISTRAION MODEL
class RegistrationPurchase(models.Model):
    ref = models.CharField(max_length=200)
    email = models.EmailField(blank=False)
    phonenumber = models.CharField(max_length=15,blank=False)
    verified = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True , blank=True)

    def __str__(self):
        return f"Email:{self.email}|id:{self.id}"

    def save(self,*args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = RegistrationPurchase.objects.filter(ref = ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

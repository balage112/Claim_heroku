from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField

# Create your models here.


class Claim(models.Model):
    #user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, help_text='Enter a brief description of the claim')
    price_tranche = MoneyField(max_digits=14,
                               decimal_places=0,
                               blank=True,
                               null=True,
                               help_text="Enter available amount",
                               currency_choices=[('CZK', 'Czech Koruna')])
    min_price_tranche = MoneyField(max_digits=14,
                                   decimal_places=0,
                                   blank=True,
                                   null=True,
                                   help_text="Enter a minimum price purchase",
                                   currency_choices=[('CZK', 'Czech Koruna')])
    remaining_ammount = MoneyField(max_digits=14,
                                   decimal_places=0,
                                   blank=True,
                                   null=True,
                                   currency_choices=[('CZK', 'Czech Koruna')])
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=True)
    purchased = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images/", blank=True)
    pdf = models.FileField(upload_to="files/", blank=True)

    #total_claim_ammount = models.IntegerField(default=0)

    class Meta:
        ordering = ['-due_date']

    def __str__(self):
        return self.title


class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=200, blank=False)
    l_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=False)
    phone = models.CharField(max_length=200)
    customer_has_claim = models.ManyToManyField(Claim)

    def __str__(self):
        return self.f_name + ' ' + self.l_name

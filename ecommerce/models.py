from django.db import models

# Create your models here.


class UserAccount(models.Model):
    name = models.CharField(max_length=120)
    bith_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    expiration = models.DateField()
    prace = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Sale(models.Model):
    buyer = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    date = models.DateField(null=False)
    products_buyed = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.buyer}'

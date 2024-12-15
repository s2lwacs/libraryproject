from django.db import models

# One-to-Many Relationship
class Address(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name


# Many-to-Many Relationship
class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city



class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2, related_name='students')
    def __str__(self):
        return self.name

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title

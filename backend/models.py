from django.db import models

class DisabledPerson(models.Model):
    name = models.CharField(max_length=100)
    disability_type = models.CharField(max_length=100)
    contact = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class User(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=20)
    profilePicture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    region = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    levelOfEducation = models.CharField(max_length=100)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.fullname

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=50)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.skill_name} ({self.user.fullname})"

class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='works')
    work_title = models.CharField(max_length=100)
    work_description = models.TextField()
    work_type = models.CharField(max_length=50)
    work_experience = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.work_title} ({self.user.fullname})"

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    productName = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.productName

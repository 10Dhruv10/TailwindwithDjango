from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ChaiVariety(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='chais/')
    types_of_chai_tuple=[
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ("PL", 'PLAIN'),
        ("KW", 'KIWI'),
        ('EL', 'ELAICHI'),
    ]
    type = models.CharField(max_length=20, choices = types_of_chai_tuple)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name

#one-to-many relation     #one tea can have many reviews
class ChaiReview(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name = 'reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'


#many-to-many  #many restaurants can have many teas
class Store(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')

    def __str__(self):
        return self.name


#one-to-one   #unique student will have unique certificate
class ChaiCertificate(models.Model):
    chai_varieties = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai_varieties.name}'
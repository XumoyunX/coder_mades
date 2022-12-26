from django.db import models

from client.models import User




class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Darsni nomi")

    def __str__(self):
        return self.name

class Kurs(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey('client.User', null=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to="images/")
    price = models.PositiveBigIntegerField()
    dars_soni = models.IntegerField()

    def __str__(self):
        return self.subject_uz

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"


class Video(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.RESTRICT)
    content = models.TextField()
    video = models.FileField(upload_to="video/")



class Profile(models.Model):
    user = models.ForeignKey('client.User', null=True, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, null=True, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, null=True, on_delete=models.CASCADE)
    number = models.CharField(max_length=250)


class Teachir(models.Model):
    photo = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete = models.CASCADE)


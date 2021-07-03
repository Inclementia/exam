from django.db import models



class Students(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

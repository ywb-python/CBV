from django.db import models


class Student(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    sex = models.BooleanField(verbose_name="性别", default=1)
    class_null = models.CharField(verbose_name="班级编号", max_length=5)

    class Meta:
        db_table = "to_student"

# Create your models here.

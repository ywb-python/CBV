from django.db import models


class Student(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=32)
    age = models.IntegerField(verbose_name="年龄")
    sex = models.BooleanField(verbose_name="性别", default=1)
    class_null = models.CharField(verbose_name="班级编号", max_length=5)

    class Meta:
        db_table = "to_student"


class Book(models.Model):
    title = models.CharField(verbose_name="书籍名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")
    pub_date = models.DateField(verbose_name="出版日期")
    bread = models.IntegerField(verbose_name="阅读量")
    bcomment = models.IntegerField(verbose_name="评论量")
    publish = models.ForeignKey('Publish', verbose_name="出版社", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Publish(models.Model):
    name = models.CharField(verbose_name="出版社名称", max_length=32)
    email = models.EmailField(verbose_name="出版社邮箱")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(verbose_name="作者", max_length=32)
    age = models.IntegerField(verbose_name="年龄")

    def __str__(self):
        return self.name
# Create your models here.

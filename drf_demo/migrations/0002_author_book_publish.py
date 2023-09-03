# Generated by Django 3.2.20 on 2023-09-03 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drf_demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='作者')),
                ('age', models.IntegerField(verbose_name='年龄')),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='出版社名称')),
                ('email', models.EmailField(max_length=254, verbose_name='出版社邮箱')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='书籍名称')),
                ('price', models.IntegerField(verbose_name='价格')),
                ('pub_date', models.DateField(verbose_name='出版日期')),
                ('bread', models.IntegerField(verbose_name='阅读量')),
                ('bcomment', models.IntegerField(verbose_name='评论量')),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drf_demo.publish', verbose_name='出版社')),
            ],
        ),
    ]

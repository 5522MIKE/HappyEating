# Generated by Django 3.1.4 on 2020-12-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20201220_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=120, verbose_name='内容')),
                ('picture', models.FileField(upload_to='', verbose_name='图片')),
            ],
        ),
        migrations.RemoveField(
            model_name='diary',
            name='author',
        ),
    ]

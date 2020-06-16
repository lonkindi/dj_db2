# Generated by Django 3.0.6 on 2020-06-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m2m', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Секция')),
                ('is_main', models.BooleanField(verbose_name='Основная секция')),
                ('articles', models.ManyToManyField(related_name='sections', to='m2m.Article')),
            ],
        ),
    ]
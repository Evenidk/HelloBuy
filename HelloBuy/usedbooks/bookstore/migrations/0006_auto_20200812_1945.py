# Generated by Django 3.1 on 2020-08-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_auto_20200808_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='stream',
            field=models.CharField(choices=[('Humanities', 'Humanities'), ('Medical', 'Medical'), ('Engineering', 'Engineering'), ('Commerce', 'Commerce')], default='Engineering', max_length=15),
        ),
    ]

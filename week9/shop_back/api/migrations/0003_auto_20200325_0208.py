# Generated by Django 3.0.4 on 2020-03-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='prod', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
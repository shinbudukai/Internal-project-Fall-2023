# Generated by Django 3.1.1 on 2023-04-01 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languageDetectApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='languagedetect',
            name='venue_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='languagedetect',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
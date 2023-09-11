# Generated by Django 4.0.3 on 2023-04-17 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseTracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner'), ('snacks', 'snacks')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fooditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('carbohydrate', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('fats', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('calorie', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5)),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('category', models.ManyToManyField(to='expenseTracker.category')),
            ],
        ),
        migrations.CreateModel(
            name='UserFooditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ManyToManyField(blank=True, to='expenseTracker.userprofile')),
                ('fooditem', models.ManyToManyField(to='expenseTracker.fooditem')),
            ],
        ),
    ]
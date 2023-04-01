# Generated by Django 4.1.4 on 2022-12-26 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_country_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='state_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Statename', models.CharField(max_length=20)),
                ('Countryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.country_tb')),
            ],
        ),
    ]
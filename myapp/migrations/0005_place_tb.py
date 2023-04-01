# Generated by Django 4.1.4 on 2022-12-26 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_state_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='place_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place', models.CharField(max_length=20)),
                ('Country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.country_tb')),
                ('State', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.state_tb')),
            ],
        ),
    ]
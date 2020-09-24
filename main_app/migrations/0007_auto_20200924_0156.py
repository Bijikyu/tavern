# Generated by Django 3.0.8 on 2020-09-24 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200924_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='date',
            field=models.DateTimeField(blank=True, verbose_name='date of next session'),
        ),
        migrations.AlterField(
            model_name='group',
            name='details',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='group',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='group',
            name='looking',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='system',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.System'),
        ),
    ]
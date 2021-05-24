# Generated by Django 2.0.1 on 2021-05-23 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_auto_20210523_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('no_workers', models.IntegerField(default=0)),
                ('capacity', models.IntegerField(default=0)),
                ('opening_hours', models.CharField(max_length=55)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('store_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.StoreBranch')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
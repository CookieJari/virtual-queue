# Generated by Django 2.0.1 on 2021-06-19 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210523_1123'),
        ('orders', '0002_auto_20210617_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='store_branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.StoreBranch'),
        ),
    ]
# Generated by Django 2.1.5 on 2019-02-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracked_prices', '0003_auto_20190213_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.URLField(max_length=100)),
            ],
        ),
    ]
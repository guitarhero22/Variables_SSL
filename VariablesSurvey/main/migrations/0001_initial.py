# Generated by Django 2.2.6 on 2019-11-24 09:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_code', models.CharField(max_length=50)),
                ('form_name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
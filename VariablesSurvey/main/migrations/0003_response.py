# Generated by Django 2.2.3 on 2019-11-25 01:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_option_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single', models.CharField(default='', max_length=100)),
                ('single_int', models.IntegerField(default=0)),
                ('para', models.TextField(default='')),
                ('options', models.CharField(default='', max_length=100)),
                ('multi_option', models.CharField(default='', max_length=100)),
                ('q_id', models.ForeignKey(on_delete='CASCADE', to='main.question')),
                ('user', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.1 on 2022-09-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, db_index=True, max_length=15, null=True, unique=True)),
                ('permission', models.CharField(choices=[('OWNER', 'owner'), ('ADMIN', 'admin'), ('MEMBER', 'member')], default='member', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
# Generated by Django 4.0.2 on 2022-02-25 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_team', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accounts_fullname', models.CharField(max_length=200)),
                ('accounts_key', models.CharField(max_length=50, unique=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('key_vendor', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('address', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('mail', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('link_image_facebook', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('link_telegram', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('status', models.BooleanField(default=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

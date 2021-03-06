# Generated by Django 3.2.9 on 2021-11-24 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, verbose_name='User name')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(blank=True, max_length=250, verbose_name='Task')),
                ('is_completed', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='to_do.card')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.AddField(
            model_name='card',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='to_do.user'),
        ),
    ]

from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField('User name', max_length=250, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name


class Card(models.Model):
    user = models.ForeignKey(
        User, related_name='card', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):
        return 'Card'


class Task(models.Model):
    task = models.CharField('Task', max_length=250, blank=True)
    card = models.ForeignKey(
        'Card', related_name='task', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.task

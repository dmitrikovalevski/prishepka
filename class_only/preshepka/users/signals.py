from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import UserInfo


@receiver(post_save, sender=User)
def create_userinfo(instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)


@receiver(post_save, sender=User)
def add_user_for_groups(instance, created, **kwargs):
    if created:
        try:
            group = Group.objects.get(name='user')
        except:
            group = Group.objects.create(name='user')
            instance.groups.add(group)
            print(f'Группа user создана. {instance} добавлен к группе user')
        else:
            instance.groups.add(group)
            print(f'{instance} добавлен к группе user')





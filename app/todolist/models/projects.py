from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(
        verbose_name='Project Name',
        max_length=200,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Description',
        max_length=2000,
        null=False,
        blank=False
    )
    start_date = models.DateField(
        verbose_name='Start date',
        null=False,
        blank=False
    )
    end_date = models.DateField(
        verbose_name='End date',
        null=False,
        blank=True,
        default=None
    )
    is_deleted = models.BooleanField(
        verbose_name='Deleted',
        default=False, null=False
    )
    # users = models.ManyToMany(User, related_name='projects', blank=True, through=User,)


    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
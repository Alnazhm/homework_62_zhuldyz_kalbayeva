from django.db import models
from django.utils import timezone


class Tasks(models.Model):
    summary = models.CharField(verbose_name='Summary', max_length=200)
    description = models.TextField(verbose_name='Description', null=True, blank=True,max_length=2000)
    status = models.ForeignKey(
        to='todolist.Status',
        verbose_name='Статус задачи',
        related_name='statuses',
        on_delete=models.PROTECT)
    type = models.ManyToManyField(
        to='todolist.Type',
        verbose_name='Тип задачи',
        related_name='tasks',
        blank=True)
    project = models.ForeignKey(
        to='todolist.Project',
        verbose_name='Проект',
        related_name='tasks',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Время изменения',
        auto_now=True)
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False, null=False
    )

    def __str__(self):
        return f"{self.summary} - {self.type.name} - {self.status}"

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
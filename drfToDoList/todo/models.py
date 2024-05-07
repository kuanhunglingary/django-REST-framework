from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Task"

    def __str__(self):
        return self.title


class Log(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    action = models.IntegerField(choices=((1, '新增'), (2, '刪除'), (3, '修改'), (4, '查詢')))
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "Log"

    @classmethod
    def create_log(cls, action, task=None):
        log = cls(action=action, task=task)
        log.save()
        return log

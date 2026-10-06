from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    STATUS = (
        ('✔️', '✔️'),
        ('⌛', '⌛'),
        ('❌', '❌')
    )
    status = models.CharField(max_length=100, choices=STATUS)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
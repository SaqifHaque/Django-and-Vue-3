from django.db import models

class Jobs (models.Model):
    job_title = models.CharField(max_length=250)
    location = models.TextField()

    def __str__(self):
        return self.job_title

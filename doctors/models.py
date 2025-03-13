from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    image = models.URLField()
    views = models.IntegerField()
    rating = models.FloatField()
    crm = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    description = models.TextField()
    conditions = models.TextField()
    patient_groups = models.CharField(max_length=255)
    insurance = models.CharField(max_length=100)
    follow_up = models.CharField(max_length=100)
    experience = models.TextField()
    education = models.JSONField()
    video_url = models.URLField()
    consultation_fee = models.FloatField()
    additional_data = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name

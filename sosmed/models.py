from django.db import models


class AkunSosmed(models.Model):
    PLATFORM_CHOICES = [
        ('instagram', 'Instagram'),
        ('tiktok', 'TikTok'),
        ('facebook', 'Facebook'),
        ('twitter', 'X / Twitter'),
    ]

    nama_depan = models.CharField(max_length=100)
    nama_belakang = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)

    def __str__(self):
        return f"{self.username} - {self.platform}"

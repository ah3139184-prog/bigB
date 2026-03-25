from django.contrib.auth.models import User
from django.db import models


class DataSource(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    details = models.TextField (blank=True, null=True, default='none')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="data_sources")
    metadata = models.JSONField(null=True, blank=True)
    status = models.CharField(
                max_length=50,
                choices=[
                    ("uploaded", "Uploaded"),
                    ("processing", "Processing"),
                    ("ready", "Ready"),
                    ("error", "Error")
                ],
                default="uploaded"
                        )

    def __str__(self):
        return self.name


class DataRecord(models.Model):
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE, related_name="records")
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record {self.id} from {self.source.name}"


class AIQuery(models.Model):
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE, related_name="queries")
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.question[:50]


class AnalysisResult(models.Model):
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE, related_name="analyses")
    result = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    
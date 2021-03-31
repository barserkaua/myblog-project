from django.db import models


# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=60)
    post_date = models.DateTimeField()
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='event_images/')

    def get_summary(self):
        return self.post_text[:70]+'...'
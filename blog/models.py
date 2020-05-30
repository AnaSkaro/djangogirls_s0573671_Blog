from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # gibt an, dass das Post-Model ein Django-Model ist, so weiß Django, dass es in
    # der Datenbank gespeichert werden soll.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

from django.db import models

from hashlib import md5


class TinyURL(models.Model):
    url = models.URLField()
    hash = models.CharField(max_length=32, db_index=True, blank=True, unique=True)
    
    def save(self, **kw):
        self.hash = md5(self.url).hexdigest()
        super(TinyURL, self).save(**kw)
        
    def get_absolute_url(self):
        return '/tinyurl/%s/' % self.hash

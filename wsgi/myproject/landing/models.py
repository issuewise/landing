from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Email(models.Model):

    email = models.EmailField(_('email of the user'))
    submission_time = models.DateTimeField(_('time when email was submitted'),
        auto_now = True)
    ip = models.GenericIPAddressField(_('ip address of the user at the time of \
    submission'))
    browser = models.CharField(_('browser used by the user at the time of \
    submission'), max_length=200)
    
    class Meta:
        app_label = 'landing'
    
    
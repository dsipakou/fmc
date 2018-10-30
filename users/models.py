from django.db import models
from django.utils.timezone import now as datetime_now
from django.utils.translation import ugettext_lazy as _

from users.validators import AsteriskRestrictedEmailValidator


class User(models.Model):
    email = models.EmailField(_('email address'), max_length=255, unique=True,
                              db_index=True, validators=[AsteriskRestrictedEmailValidator])
    password = models.CharField(_('password'), max_length=128, blank=True)
    first_name = models.CharField(_('first name'), max_length=255, blank=True)
    last_name = models.CharField(_('last name'), max_length=255, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=datetime_now)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True, null=True)
    uuid = models.CharField(_('user uuid'), max_length=36, null=True, blank=True)
    is_active = models.BooleanField(_('active'), default=True)

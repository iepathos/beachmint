from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from datetime import datetime

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    GENDER_CHOICES = (
    	(1, _('Male')),
    	(2, _('Female')),
    )

    gender = models.PositiveSmallIntegerField(_('Gender'),
											choices=GENDER_CHOICES,
									      	blank=True,
									      	null=True)
    location = models.CharField(_('Location'), max_length=255, blank=True)
    birth_date = models.DateField(_('Birth date'), blank=True, null=True)
    about_me = models.TextField(_('About me'), blank=True)

    

    # social authentication
    #twitter_username = models.CharField(_('Twitter username'), max_length=100, null=True, blank=True)
    #fb_username = models.CharField(_('Facebook username'), max_length=100, null=True, blank=True)
    #linkedin_username = models.CharField(_('LinkedIn username'), max_length=100, null=True, blank=True)
    #google_username = models.CharField(_('Google username'), max_length=100, null=True, blank=True)
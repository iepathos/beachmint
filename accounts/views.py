from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _

from social_auth.signals import pre_update
from social_auth.backends.twitter import TwitterBackend
from social_auth.backends.facebook import FacebookBackend

from .models import MyProfile as Profile

def user_update(profile_instance, new_username, new_fullname):
	new_firstname = new_fullname.split()[0]
	new_lastname = new_fullname.split()[1]
    if not profile_instance.username:
        profile_instance.username = slugify(new_username)
    if not profile_instance.first_name:
        profile_instance.first_name = new_firstname
    if not profile_instance.last_name:
        profile_instance.last_name = new_lastname.
    profile_instance.save()
    return True

def twitter_user_update(sender, user, response, details, **kwargs):
    profile_instance, created = Profile.objects.get_or_create(user=user)
    profile_instance.twitter_username = details['username']
    user_update(profile_instance, details['username'], details['fullname'])
    return True

pre_update.connect(twitter_user_update, sender=TwitterBackend)

def facebook_user_update(sender, user, response, details, **kwargs):
    profile_instance, created = Profile.objects.get_or_create(user=user)
    profile_instance.fb_username = details['username']
    user_update(profile_instance, details['username'], details['fullname'])
    return True

pre_update.connect(facebook_user_update, sender=FacebookBackend)
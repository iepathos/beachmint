# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

from social_auth.backends.twitter import TwitterBackend
from social_auth.backends.facebook import FacebookBackend

def social_associate_and_load_data(backend, details, response, uid, user,
                                   social_user=None, *args, **kwargs):
    """
    The combination of associate_user and load_extra_data functions
    of django-social-auth. The reason for combining these two pipeline
    functions is to decrease the number of database visits.
    """
    extra_data = backend.extra_data(user, uid, response, details)
    created = False
    if not social_user and user:
        social_user, created = UserSocialAuth.objects.get_or_create(
            user_id=user.id,
            provider=backend.name,
            uid=uid,
            defaults={'extra_data': extra_data})

    if not created and extra_data and social_user.extra_data != extra_data:
        social_user.extra_data.update(extra_data)
        social_user.save()
    return {'social_user': social_user}

def get_user_avatar(backend, details, response, social_user, uid,\
                    user, *args, **kwargs):
    url = None
    if backend.__class__ == FacebookBackend:
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
 
    elif backend.__class__ == TwitterBackend:
        url = response.get('profile_image_url', '').replace('_normal', '')
 
    if url:
        profile = user.get_profile()
        avatar = urlopen(url).read()
        fout = open(filepath, "wb") #filepath is where to save the image
        fout.write(avatar)
        fout.close()
        profile.photo = url_to_image # depends on where you saved it
        profile.save()

def get_user_gender(backend, details, response, social_user, uid,\
                    user, *args, **kwargs):
    gender = None
    if backend.__class__ == FacebookBackend:
        gender = response['gender']

    elif backend.__class__ == TwitterBackend:
        gender = response['gender']

    if gender:
        profile = user.get_profile()
        profile.gender = gender
        profile.save()
    return {'gender': gender}

def get_user_location(backend, details, response, social_user, uid,\
                      user, *args, **kwargs):
    location = None
    if backend.__class__ == FacebookBackend:
        location = response['location']

    elif backend.__class__ == TwitterBackend:
        location = response['location']

    if location:
        profile = user.get_profile()
        profile.location = location
        profile.save()
    return {'location': location}

def get_user_fullname(backend, details, response, social_user, uid,\
                      user, *args, **kwargs):
    fullname = None
    if backend.__class__ == FacebookBackend:
        fullname = response['fullname']

    elif backend.__class__ == TwitterBackend:
        fullname = response['fullname']

    if fullname:
        firstname = fullname.split()[0]
        lastname = fullname.split()[1]
        profile = user.get_profile()
        profile.first_name = firstname
        profile.last_name = lastname
        profile.save()
    return {'fullname': fullname,
            'first_name': firstname,
            'last_name': lastname,}

# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.utils.translation import ugettext as _

# My BaseModel just provides creation and modified timestamps
from core.models import BaseModel

from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

import os
import shutil
import itertools

from settings import BASE_DIRECTORY_PATH


def clean_path(path):
	"""
		Utility function for cleaning directory changing
		characters from incoming path strings.
	"""
	cleaned_path = str(path).replace('..', '').strip()
	return cleaned_path

class AcmeManager(models.Manager):
	"""
		Base Manager for FileManager.
	"""

	def by_user(self, user):
		return self.get_query_set().filter(user=user)

class FileManager(AcmeManager):
	"""
		File Manager manages both File and Folder type
		objects.  Handles creation of files	and folders.
		Handles providing sorted lists to views.
	"""
	def by_realpath(self, realpath, user):
		"""
			Returns the file or folder at a given path.  
			The expected path is the realpath on the filesystem.
		"""
		base_slice = len(str(os.path.join(BASE_DIRECTORY_PATH, user.username)))
		relative_path = realpath[base_slice:]
		return self.get_query_set.filter(path=relative_path)

	def by_path(self, path):
		"""
			Returns the file or folder at a given path.  
			The expected path is relative to a user's home 
			directory path.  The user's username should 
			already be in the path.
		"""
		return self.get_query_set().filter(path=path)

	def create_file(self, path, user):
		cleaned_path = clean_path(path)
		try:
			newfile = open(os.path.join(BASE_DIRECTORY_PATH, str(user.username), cleaned_path), 'w+')
			newfile.close()
		except OSError, e:
			print e.args
		file = self.create(path=cleaned_path, user=user)
		#file.name = os.path.basename(cleaned_path)
		#file.parent = self.objects.folders.filter(path=str(os.path.join(BASE_DIRECTORY_PATH, str(file.user.username), file.path, '..')))[0]
		file.save()
		return file

	def files(self, **kwargs):
		return self.filter(isDir=False, **kwargs)

	def create_folder(self, path, user):
		cleaned_path = clean_path(path)
		try:
			os.makedirs(os.path.join(BASE_DIRECTORY_PATH, str(user.username), cleaned_path))
		except OSError, e:
			print e.args
		folder = self.create(path=cleaned_path, user=user)
		#folder.name = os.path.basename(cleaned_path)
		#folder.parent = self.objects.folders.filter(path=str(os.path.join(BASE_DIRECTORY_PATH, str(folder.user.username), folder.path, '..')))[0]
		folder.save()
		return folder

	def folders(self, **kwargs):
		return self.filter(isDir=True, **kwargs)

def get_reversed_object_paths():
	reversed_object_paths = sorted(list(itertools.chain(File.objects.files(), Folder.objects.folders())))
	reversed_object_paths.reverse()
	return reversed_object_paths

class Acme(BaseModel):
	"""
		Acme abstract base class for File and Folder
		objects.  Only requires a User and Path to
		create this type of object.  The name is just
		the end part of the path.
	"""
	path = models.CharField(_('Path'), max_length=255)
	
	user = models.ForeignKey(User, null=True)

	# Not going to require a name for model 
	# creation functions. Instead, taking name 
	# from end of path during object instantiation.
	name = models.CharField(_('Name'), max_length=255, blank=True, editable=False)
	slug = models.SlugField(_('Slug'), max_length=255, blank=True, editable=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		self.name = self.path.split('/')[-1]
		super(Acme, self).save(*args, **kwargs)

	def rename(self, newname):
		cleaned_newname = clean_path(newname)
		try:
			os.rename(
				os.path.join(BASE_DIRECTORY_PATH, str(self.user.username), self.path),
				os.path.join(BASE_DIRECTORY_PATH, str(self.user.username), cleaned_newname))
		except OSError, e:
			print e.args
		self.path = self.path[len(self.name):] + cleaned_newname
		self.name = cleaned_newname
		self.save()

	def self_destruct(self):
		# Self-destruct database reference
		print 'Tried to read file or folder at', self.path
		print 'Object does not exist on filesystem.'
		print 'Removing database reference object.'
		self.delete()

	class Meta:
		abstract = True # More efficient database storage

	def __unicode__(self):
		return self.path

class File(Acme):
	"""
		File class represents file type objects on the server.

	"""
	isDir = models.BooleanField(_('File'), default=False, editable=False)

	#parent = models.ForeignKey(Folder, blank=True)

	objects = FileManager()

	def read(self):
		try:
			f = open(os.path.join(BASE_DIRECTORY_PATH, str(self.user.username), self.path), 'r')
			file_contents = f.read()
			f.close()
			return file_contents
		except IOError:
			self.self_destruct()

	def delete(self):
		# Deletes the file at the path recursively
		# Path should be safe, but just because this is an
		# extra dangerous method we'll have an extra safety
		# check.
		cleaned_path = clean_path(self.path)
		try:
			os.remove(os.path.join(BASE_DIRECTORY_PATH, str(self.user.username), cleaned_path))
			# Remove squiggly '~' copy on system
			os.remove(os.path.join(BASE_DIRECTORY_PATH, str(self.user.username), cleaned_path+'~'))
		except OSError, e:
			if e.args[0] == 2: # Does Not Exist
				print 'File not found.  Removing database reference object.'
				pass
			else:
				print e.args
		super(File, self).delete()

	def get_absolute_url(self):
		return reverse("file_detail", kwargs={'username': self.user.username, "pk": self.pk})


class Folder(Acme):
	"""
		Folder class represents folder type objects on the server.
		
	"""
	isDir = models.BooleanField(_('Folder'), default=True, editable=False)

	#children_files = models.ManyToManyField(File)
	#children_folders = models.ManyToManyField('self', symmetrical=False)

	#parent = models.ForeignKey('self', blank=True)

	objects = FileManager()

	def __init__(self, *args, **kwargs):
		super(Folder, self).__init__(*args, **kwargs)

	def read(self):
		try:
			folder_contents = os.listdir(os.path.join(BASE_DIRECTORY_PATH, str(self.user.username), self.path))
			return folder_contents
		except OSError, e:
			if e.args[0] == 2: # Does Not Exist
				self.delete()
				pass
			else:
				print e.args

	def delete(self):
		# Deletes the directory at the path recursively
		# Path should be safe, but just because this is an
		# extra dangerous method we'll have an extra safety
		# check.
		cleaned_path = clean_path(self.path)
		try:
			# Remove child folder and file reference
			# objects from the database.

			# Remove folder recursively from file system.
			shutil.rmtree(os.path.join(BASE_DIRECTORY_PATH, str(self.user.username), cleaned_path))
		except OSError, e:
			if e.args[0] == 2: # Does Not Exist
				#print 'Folder not found.  Removing database reference object.'
				pass
			else:
				print e.args
		super(Folder, self).delete()

	def rename(self, newname):
		# Need to rename paths recursively for children in folder
		super(Folder, self).rename()

	def get_absolute_url(self):
		return reverse("folder_detail", kwargs={'username': self.user.username, 'pk': self.pk})

#def FileSystemToDatabaseSync():
	# This is called after each folder is removed
	# And will be called if a file or folder/directory
	# is directly uploaded.  

	#for file in File.objects.all():
		# Check if file exists at path
		# remove database reference if it doesn't


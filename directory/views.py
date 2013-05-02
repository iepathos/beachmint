import os
import sys
from django.contrib.auth.models import User

from django.contrib import messages

from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView

from braces.views import LoginRequiredMixin

from settings import BASE_DIRECTORY_PATH

from .models import File, Folder



def contract_path(path):
	"""
		Utility function takes an actual path for 
		a user's files or folders and returns a 
		sliced path that will work for 
		the database reference path.
	"""
	username = path[len(BASE_DIRECTORY_PATH)+1:].split('/')[0]
	return path[len(str(os.path.join(BASE_DIRECTORY_PATH, username))):]

def expand_path(user, path):
	"""
		This function is the opposite of contract_path()

	"""
	return str(os.path.join(BASE_DIRECTORY_PATH, user.username, path))


def get_user_by_path(path):
	"""
		Takes an expanded path and determines
		the user who owns that file.  Returns
		a user object.
	"""
	base_slice = path[len(BASE_DIRECTORY_PATH):] # Slice everything but the username and path
	username = base_slice.split('/')[0]
	return User.objects.get(username=username)

def get_parent_path(path):
	if path.endswith('/'):
		file_name = path.split('/')[-2]
		parent_path = path[:-(len(file_name)+2)] # Added 2 for '/'s
		return parent_path
	else:
		file_name = path.split('/')[-1]
		parent_path = path[:-(len(file_name)+1)]
		return parent_path

def get_parent_by_path(path):
	"""
		Takes a contracted path, returns parent object.
	"""
	return Folder.objects.get(path=get_parent_path(path))

def get_child_paths(path):
	# Just take a single directories items
	children_paths = []
	if os.isdir(path):
		for child in os.listdir(path):
			children_paths += path+'/'+child
		return children_paths
	else:
		return 'Error path object is not a directory.'

def get_all_child_paths(path):
	# Returns all paths of all files and folders
	# within a given folder.  Recursive, finds all
	# descendents.
	# Takes expanded paths
	# Returns contracted paths.
	children_paths = []
	for root, dirnames, filenames in os.walk(path):
		children_paths.append(contract_path(root))
		for file in filenames:
			children_paths.append(contract_path(root) +'/'+ file)
	return children_paths

def create_user_homedir(user):
	os.makedirs(os.path.join(BASE_DIRECTORY_PATH, str(user.username)))
	homedir_path = str(os.path.join(BASE_DIRECTORY_PATH, str(user.username)))
	return homedir_path

def generateReferenceObjects(user):
	"""
		Scans through a user's directory and generates 
		file and folder reference objects in the database 
		from any paths.

	"""
		
	homedir_path = str(os.path.join(BASE_DIRECTORY_PATH, user.username))
	print 'User Home Directory Path:', homedir_path

	try:
		directory_list = os.listdir(homedir_path)
	except:
		create_user_homedir(user)
		directory_list = os.listdir(homedir_path)

	# reference will be relative to user homedir
	reference_paths = get_all_child_paths(homedir_path)
	print 'References Paths:', reference_paths

	if reference_paths != None:
		for path in reference_paths:
			# get or create file/folder
			if os.path.isdir(path):
				# create folder if one not found
				Folder.objects.get_or_create(user=user, path=path)
			else:
				# create file if one not found
				File.objects.get_or_create(user=user, path=path)

def cleanReferenceObjects(user):
	"""
		Cleans references objects found in database
		that no longer correspond to files or folders
		on the system.

	"""
	for folder in Folder.objects.by_user(user):
		if not os.isdir(expand_path(user, folder.path)):
			folder.delete()

	for file in File.objects.by_user(user):
		file.read()


class DirectoryView(LoginRequiredMixin, TemplateView):
	"""
		DirectoryView is the main homepage view.

	def get_context_data(self, **
		Display sidebar on left for directory_navigation.

		File and folder viewing section based on 
		selected object in directory_navigation.
	"""
	template_name = 'directory/directory_home.html'

	def get_context_data(self, **kwargs):
	    context = super(DirectoryView, self).get_context_data(**kwargs)
	    try:
	    	homedir_path = str(os.path.join(BASE_DIRECTORY_PATH, str(self.request.user.username)))
	    except OSError, e:
	    	if e.args[0] == '2': # Does Not Exist
	    		homedir_path = create_user_homedir(self.request.user)
	    		print 'Home directory not found.  Creating home directory.'
		    	pass
	    	else:
				print e.args
		context['homedir'] = homedir_path
	    #context['directory_list'] = get_all_child_paths(expand_path(self.request.user, homedir_path))
	    context['files'] = File.objects.by_user(self.request.user)
	    context['folders'] = Folder.objects.by_user(self.request.user)
	    

	    return context

class ActionMixin(object):
	@property
	def action(self):
		msg = "{0} is missing action.".format(self.__class__)
		raise NotImplementedError(msg)

class FileActionMixin(ActionMixin):
	def form_valid(self, form):
		msg = "File {0}!".format(self.action)
		messages.info(self.request, msg)
		return super(FileActionMixin, self).form_valid(form)

class FolderActionMixin(ActionMixin):
	def form_valid(self, form):
		msg = "Folder {0}!".format(self.action)
		messages.info(self.request, msg)
		return super(FolderActionMixin, self).form_valid(form)

class FileListView(LoginRequiredMixin, ListView):
	model = File

class FileCreateView(LoginRequiredMixin, CreateView):
	model = File
	#action = 'created'

class FileUpdateView(LoginRequiredMixin, UpdateView):
	model = File
	#action = 'updated'

class FileDetailView(LoginRequiredMixin, DetailView):
	model = File

class FolderCreateView(LoginRequiredMixin, CreateView):
	model = Folder
	#action = 'created'

class FolderUpdateView(LoginRequiredMixin, UpdateView):
	model = Folder
	#action = 'updated'

class FolderDetailView(LoginRequiredMixin, DetailView):
	model = Folder


"""
class DirectoryWalkerMixin(object):

	def user_directory_list(self):
		fileList = []
		rootdir = os.path.join(BASE_DIRECTORY_PATH, str(request.user.username))
		for root, subFolders, files in os.walk(rootdir):
		    for file in files:
		        fileList.append(os.path.join(root,file))
		return fileList
	

	#directory_list
	# Match the paths given by user_directory_list
	# with their respective file and folder objects
	# in the database.
	directory_navigation = {} # Dictionary of File/Folder names : urls
	directory_list = user_directory_list(request.user.username)
	for path in directory_list:
		for folder in Folder.objects.by_user(object.owner):
			if os.path.join(BASE_DIRECTORY_PATH, str(object.owner.username), file.path) == path:
				directory_navigation['folder_'+folder.name] = folder.get_absolute_url()
				# Later TemplateTag: 
				# for key in directory_navigation: 
				#   if key.startswith('folder_'): 
				#	  - make expandable dropdown menu for folder

		for file in File.objects.by_user(object.owner):
			if os.path.join(BASE_DIRECTORY_PATH, str(object.owner.username), file.path) == path:
				directory_navigation['file_'+file.name] = file.get_absolute_url()
"""


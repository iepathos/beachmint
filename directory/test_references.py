# Test for database object reference generator
# and reference objects cleaner for keeping
# the file system and database references in sync.
from directory.models import File, Folder
from django.contrib.auth.models import User
import os
from settings import BASE_DIRECTORY_PATH

from directory.views import generateReferenceObjects, cleanReferenceObjects

user = User.objects.get(username='iepathos')
homedir_path = str(os.path.join(BASE_DIRECTORY_PATH, user.username))

# Create files in directory that aren't already
# referenced by database
newfile = open(os.path.join(BASE_DIRECTORY_PATH, str(user.username), 'unreferencedfile'), 'w+')
newfile.close()

generateReferenceObjects(user)
# Test currently failing

from directory.views import contract_path
# Testing get_all_child_paths
#from directory.views import get_all_child_paths
children_paths = []
for root, dirnames, filenames in os.walk(homedir_path):
	children_paths.append(contract_path(root))
	for file in filenames:
		children_paths.append(contract_path(root) +'/'+ file)
	print children_paths
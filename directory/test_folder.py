# Tests for the Acme Folder model
from directory.models import Folder
from django.contrib.auth.models import User
import os
from settings import BASE_DIRECTORY_PATH

# FOLDER CREATE TEST
folder_creation_test = False
user = User.objects.get(username='iepathos')
folder = Folder.objects.create_folder('testfolder', user)

folder.path
folder.name
folder.slug


# FOLDER RECURSIVE DELETE TEST
folder2 = Folder.objects.create_folder('testfolder/testfolder2', user)
folder3 = Folder.objects.create_folder('testfolder/testfolder2/testfolder3', user)

children_paths = os.listdir(os.path.join(BASE_DIRECTORY_PATH, str(folder.owner.username), folder.path))
for children_paths in os.listdir(os.path.join(BASE_DIRECTORY_PATH, str(folder.owner.username), folder.path)):
	for file in folder.children_files:
		if (BASE_DIRECTORY_PATH + str(file.owner.username) + file.path) in children_paths:
			file.delete()
	for folder in folder.children_folders:
		if (BASE_DIRECTORY_PATH + str(folder.owner.username) + folder.path) in children_paths:
			folder.delete()

folder.delete()

# Check whether folder objects still exist

# FOLDER RENAME TEST
folder.rename('renametest')
if folder.name == 'renametest':
	if folder.path == 'renametest':
		folder_rename_test = True
		print 'Folder rename test:  PASSED'
else:
	print 'Folder rename test:  FAILED'

# FOLDER READ TEST
folder.read()

os.listdir(os.path.join(BASE_DIRECTORY_PATH, str(folder.owner.pk), folder.path))

if os.path.isdir(os.path.join(BASE_DIRECTORY_PATH, str(folder.owner.pk), folder.path)):
	folder_creation_test = True
	print 'Folder creation test:  PASSED'
else:
	folder_creation_test = False
	print 'Folder creation test:  FAILED'

# FOLDER DELETE TEST
temp_folder_path = folder.path
temp_folder_ownerpk = str(folder.owner.pk)
folder.delete()
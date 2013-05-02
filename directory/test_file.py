# Tests for the Acme File model
from directory.models import File
from django.contrib.auth.models import User
import os
from settings import BASE_DIRECTORY_PATH

# FILE CREATE TEST
file_creation_test = False
user = User.objects.get(username='iepathos')
file = File.objects.create_file('testfile', user)

#file = File.objects.files()[0]

# FILE RENAME TEST
file.rename('renametest')
if file.name == 'renametest':
	if file.path == 'renametest':
		file_rename_test = True
		print 'File rename test:  PASSED'
else:
	print 'File rename test:  FAILED'


# FILE WRITE TEST
file.write('testing123')

# FILE READ TEST
if file.read() = 'testing123':
	file_read_test = True
	print 'File read test:  PASSED'
else:
	file_read_test = False
	print 'File read test:  FAILED'

if os.path.isfile(os.path.join(BASE_DIRECTORY_PATH, str(file.owner.pk), file.path)):
	file_creation_test = True
	print 'File creation test:  PASSED'
else:
	file_creation_test = False
	print 'File creation test:  FAILED'

# FILE DELETE TEST
temp_file_path = file.path
temp_file_ownerpk = str(file.owner.pk)
file.delete()
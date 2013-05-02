from django.forms import ModelForm

from .models import File, Folder

class FileForm(ModelForm):
	class Meta:
		model = File

class FolderForm(ModelForm):
	class Meta:
		model = Folder
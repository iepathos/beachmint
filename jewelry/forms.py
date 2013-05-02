from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import floppyforms as forms

from .models import Ring, Bracelet, Necklace

class RingForm(forms.ModelForm):

	class Meta:
		model = Ring

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))
		super(RingForm, self).__init__(*args, **kwargs)

class BraceletForm(forms.ModelForm):

	class Meta:
		model = Bracelet

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))
		super(BraceletForm, self).__init__(*args, **kwargs)

class NecklaceForm(forms.ModelForm):

	class Meta:
		model = Necklace

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))
		super(NecklaceForm, self).__init__(*args, **kwargs)
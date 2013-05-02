from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView

from .models import Ring, Bracelet, Necklace

from braces.views import LoginRequiredMixin

from .forms import RingForm, BraceletForm, NecklaceForm
from django.contrib import messages

class JewelryListView(TemplateView):
	template_name = 'jewelry/jewelry_list.html'

	def get_context_data(self, **kwargs):
		context = super(JewelryListView, self).get_context_data(**kwargs)
		context['rings'] = Ring.objects.all()
		context['bracelets'] = Bracelet.objects.all()
		context['necklaces'] = Necklace.objects.all()
		return context


###### Ring

class RingListView(ListView):
	model = Ring

class RingDetailView(DetailView):
	model = Ring

class RingCreateView(LoginRequiredMixin, CreateView):
	model = Ring

	form_class = RingForm

class RingUpdateView(LoginRequiredMixin, UpdateView):
	model = Ring

	form_class = RingForm

###### Bracelet

class BraceletListView(ListView):
	model = Bracelet

class BraceletDetailView(DetailView):
	model = Bracelet

class BraceletCreateView(LoginRequiredMixin, CreateView):
	model = Bracelet

	form_class = BraceletForm
	
class BraceletUpdateView(LoginRequiredMixin, UpdateView):
	model = Bracelet

	form_class = BraceletForm

###### Necklace

class NecklaceListView(ListView):
	model = Necklace

class NecklaceDetailView(DetailView):
	model = Necklace

class NecklaceCreateView(LoginRequiredMixin, CreateView):
	model = Necklace

	form_class = NecklaceForm
	
class NecklaceUpdateView(LoginRequiredMixin, UpdateView):
	model = Necklace

	form_class = NecklaceForm
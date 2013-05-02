# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.utils.translation import ugettext as _

# My BaseModel just provides creation and modified timestamps
from core.models import BaseModel
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

class JewelryManager(models.Manager):

	def by_type(jewelry_type):
		return super(JewelryManager, self).get_queryset().filter(type=jewelry_type)



class Jewelry(BaseModel):
	size = models.FloatField() # I think this is either in mm or inches for jewelry
	weight = models.FloatField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	color = models.CharField(max_length=50)

	objects = JewelryManager()

	class Meta:
		abstract = True


class Ring(Jewelry):

	type = models.CharField(max_length=50, default='Ring', editable=False)

	def wash(self):
		return 'Remove ring from finger to begin washing.'

	def get_absolute_url(self):
		return reverse("ring_detail", kwargs={"pk": self.pk})

class Bracelet(Jewelry):

	type = models.CharField(max_length=50, default='Bracelet', editable=False)

	def wash(self):
		return 'Remove bracelet from wrist to begin washing.'

	def get_absolute_url(self):
		return reverse("bracelet_detail", kwargs={"pk": self.pk})

class Necklace(Jewelry):

	type = models.CharField(max_length=50, default='Necklace', editable=False)

	def wash(self):
		return 'Remove necklace from neck to begin washing.'

	def get_absolute_url(self):
		return reverse("necklace_detail", kwargs={"pk": self.pk})
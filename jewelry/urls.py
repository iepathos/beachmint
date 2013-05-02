from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from jewelry.views import RingListView, RingDetailView, RingCreateView, RingUpdateView

from jewelry.views import BraceletCreateView, BraceletUpdateView, BraceletDetailView, BraceletListView

from jewelry.views import NecklaceCreateView, NecklaceUpdateView, NecklaceDetailView, NecklaceListView

from jewelry.views import JewelryListView

urlpatterns = patterns("",

    url(r'^$', JewelryListView.as_view(), name='jewelry_list',),

    ############### Rings

    url(
        regex=r"^ring/create/$",
        view=RingCreateView.as_view(),
        name="ring_create",
    ),
    url(
        regex=r"^ring/update/(?P<pk>\d+)/$",
        view=RingUpdateView.as_view(),
        name="ring_update",
    ),
    url(
        regex=r"^ring/(?P<pk>\d+)/$",
        view=RingDetailView.as_view(),
        name="ring_detail",
    ),
    url(
        regex=r"^ring/$",
        view=RingListView.as_view(),
        name="ring_list",
    ),

    ############### Bracelets

    url(
        regex=r"^bracelet/create/$",
        view=BraceletCreateView.as_view(),
        name="bracelet_create",
    ),
    url(
        regex=r"^bracelet/update/(?P<pk>\d+)/$",
        view=BraceletUpdateView.as_view(),
        name="bracelet_update",
    ),
    url(
        regex=r"^bracelet/(?P<pk>\d+)/$",
        view=BraceletDetailView.as_view(),
        name="bracelet_detail",
    ),
    url(
        regex=r"^bracelet/$",
        view=BraceletListView.as_view(),
        name="bracelet_list",
    ),

    ############### Necklaces

    url(
        regex=r"^necklace/create/$",
        view=NecklaceCreateView.as_view(),
        name="necklace_create",
    ),
    url(
        regex=r"^necklace/update/(?P<pk>\d+)/$",
        view=NecklaceUpdateView.as_view(),
        name="necklace_update",
    ),
    url(
        regex=r"^necklace/(?P<pk>\d+)/$",
        view=NecklaceDetailView.as_view(),
        name="necklace_detail",
    ),
    url(
        regex=r"^necklace/$",
        view=NecklaceListView.as_view(),
        name="necklace_list",
    ),
)
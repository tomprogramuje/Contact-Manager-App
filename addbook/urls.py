from django.urls import path
from . import views, url_handler

urlpatterns = [
    path("<int:pk>/detail/", views.ContactDetailsView.as_view(), name="contact_detail"),
    path("<int:pk>/edit/", views.ContactEditView.as_view(), name="contact_edit"),
    path("contact_list/", views.ContactListView.as_view(), name="contact_list"),
    path("contact_form/", views.ContactCreateView.as_view(), name="contact_form"),
    path("<int:pk>/delete/", views.ContactDeleteView.as_view(), name="contact_delete"),
    path("contact_search/", views.contact_search, name="contact_search"),
    path("", url_handler.index_handler),
]

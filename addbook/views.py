from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.db.models import Q
from .models import Contact
from .forms import ContactForm

# Create your views here.


class ContactCreateView(generic.edit.CreateView):

    form_class = ContactForm
    template_name = "addbook/contact_form.html"
    success_url = reverse_lazy("contact_list")


class ContactDetailsView(generic.DetailView):

    model = Contact
    template_name = "addbook/contact_detail.html"


class ContactEditView(generic.edit.UpdateView):

    model = Contact
    fields = ["firstname", "lastname", "phone_number", "email"]
    template_name_suffix = "_edit_form"

    def get_success_url(self):
        return reverse("contact_detail", kwargs={"pk": self.object.pk})


class ContactListView(generic.ListView):

    queryset = Contact.objects.order_by("lastname")
    context_object_name = "contact_list"


class ContactDeleteView(generic.edit.DeleteView):

    model = Contact
    success_url = reverse_lazy("contact_list")


def contact_search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        contacts = Contact.objects.filter(
            Q(lastname__contains=searched) |
            Q(firstname__contains=searched) |
            Q(phone_number__contains=searched) |
            Q(email__contains=searched)
        )
        return render(request, "addbook/contact_search.html", {"searched": searched, "contacts": contacts})
    else:
        return render(request, "addbook/contact_search.html", {})

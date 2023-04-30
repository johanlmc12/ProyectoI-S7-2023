from django.contrib import admin

# Register your models here.


from django.contrib.admin.sites import AdminSite
from django.utils.translation import gettext_lazy as _


class CustomAdminSite(AdminSite):
    site_header = _('My Site Admin')

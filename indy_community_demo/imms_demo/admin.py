from django.contrib import admin

from .models import *


admin.site.register(HealthIdentity)
admin.site.register(ImmunizationStatusCertificate)
admin.site.register(SchoolImmunizationConversation)
admin.site.register(RepoImmunizationConversation)
admin.site.register(UserImmunizationConversation)

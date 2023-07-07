from django.contrib import admin
from .models import GeneralInfo, SkillsInfo, StrengthsInfo, EducationInfo, SeminarsInfo, CertificationsInfo, CharReferencesInfo
# Register your models here.

admin.site.register(GeneralInfo)
admin.site.register(SkillsInfo)
admin.site.register(StrengthsInfo)
admin.site.register(EducationInfo)
admin.site.register(SeminarsInfo)
admin.site.register(CertificationsInfo)
admin.site.register(CharReferencesInfo)

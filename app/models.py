from django.db import models

# Create your models here.
class GeneralInfo(models.Model):
    name = models.CharField(max_length=80)
    career_obj = models.CharField(max_length=500)
    contact_no = models.CharField(max_length=11)
    email = models.EmailField()
    github_profile = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class SkillsInfo(models.Model):
    skill = models.CharField(max_length=200)
    person_info = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name='skills')

class StrengthsInfo(models.Model):
    strength = models.CharField(max_length=200)
    person_info = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name='strengths')

class EducationInfo(models.Model):
    school_name = models.CharField(max_length=100)
    date_period = models.CharField(max_length=20)
    person_info = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name='educ')

class SeminarsInfo(models.Model):
    semimar_attended = models.CharField(max_length=200)
    person_info = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name='seminars')

class CertificationsInfo(models.Model):
    certification = models.CharField(max_length=200)
    person_info = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name='certifications')

class CharReferencesInfo(models.Model):
    char_ref_name = models.CharField(max_length=80)
    ref_email = models.EmailField()
    ref_contact_no = models.CharField(max_length=11)
    person_info = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name='char_references')
    


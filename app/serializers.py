from rest_framework import serializers
from .models import GeneralInfo, SkillsInfo, StrengthsInfo, EducationInfo, SeminarsInfo, CertificationsInfo, CharReferencesInfo

class ResumeSerializer(serializers.ModelSerializer):
    class SkillsInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = SkillsInfo
            exclude = ['person_info']
    
    class StrengthsInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = StrengthsInfo
            exclude = ['person_info']
    
    class EducationInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = EducationInfo
            exclude = ['person_info']
    
    class SeminarsInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = SeminarsInfo
            exclude = ['person_info']
    
    class CertificationsInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = CertificationsInfo
            exclude = ['person_info']
    
    class CharReferencesInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = CharReferencesInfo
            exclude = ['person_info']

    skills = SkillsInfoSerializer(many=True)
    strengths = StrengthsInfoSerializer(many=True)
    educ = EducationInfoSerializer(many=True)
    seminars = SeminarsInfoSerializer(many=True)
    certifications = CertificationsInfoSerializer(many=True)
    char_references = CharReferencesInfoSerializer(many=True)
    
    class Meta:
        model = GeneralInfo
        fields = '__all__'
    
    def create(self, validated_data):
        skills_info = validated_data.pop('skills')
        strengths_info = validated_data.pop('strengths')
        educ_info = validated_data.pop('educ')
        seminars_info = validated_data.pop('seminars')
        cert_info = validated_data.pop('certifications')
        char_ref_info = validated_data.pop('char_references')
        gen_info = GeneralInfo.objects.create(**validated_data)
        for skill in skills_info:
            SkillsInfo.objects.create(person_info = gen_info, skill=skill['skill'])
        for str in strengths_info:
            StrengthsInfo.objects.create(person_info = gen_info, strength=str['strength'])
        for ed in educ_info:
            EducationInfo.objects.create(person_info = gen_info, school_name = ed['school_name'], date_period = ed['date_period'])
        for smnr in seminars_info:
            SeminarsInfo.objects.create(person_info = gen_info, semimar_attended = smnr['semimar_attended'])
        for cert in cert_info:
            CertificationsInfo.objects.create(person_info = gen_info, certification = cert['certification'])
        for char_ref in char_ref_info:
            CharReferencesInfo.objects.create(person_info = gen_info, char_ref_name = char_ref['char_ref_name'], ref_email = char_ref['ref_email'], ref_contact_no = char_ref['ref_contact_no'])
        return gen_info
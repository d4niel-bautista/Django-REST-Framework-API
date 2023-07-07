from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GeneralInfo, SkillsInfo, StrengthsInfo, EducationInfo, SeminarsInfo, CertificationsInfo, CharReferencesInfo
from .serializers import ResumeSerializer
# Create your views here.

from rest_framework import generics



# @api_view(['GET'])
# def getResume(req):
#     info = GeneralInfo.objects.all()
#     serializer = ResumeSerializer(info, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def addResume(req):
#     serializer = ResumeSerializer(data=req.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

class ResumeCreateAPIView(generics.ListCreateAPIView):
    
    serializer_class = ResumeSerializer

    def get_queryset(self):

        queryset = GeneralInfo.objects.all()
        skills_info = self.request.query_params.get('person_info')
        strengths_info = self.request.query_params.get('person_info')
        educ_info = self.request.query_params.get('person_info')
        seminars_info = self.request.query_params.get('person_info')
        cert_info = self.request.query_params.get('person_info')
        char_ref = self.request.query_params.get('person_info')
        if skills_info is not None:
            queryset = queryset.filter(person_info=skills_info)
        return queryset

class ResumeRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResumeSerializer
    queryset = GeneralInfo.objects.all()

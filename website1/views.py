from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TeamSerializer,MembersSerializer
from .models import Team, Members

class Teamlist(APIView):
    def get(self,request):
        teamer = Team.objects.all()
        serializer = TeamSerializer(teamer,many=True)
        return Response(serializer.data)


    def post(self):
        pass


class Memberslist(APIView):
    def get(self, request):
        mem = Members.objects.all()
        serial = MembersSerializer(mem, many=True)
        return Response(serial.data)

    def post(self):
        pass

def index(request):

    all_teams=Team.objects.all()
    return render(request,'ITSP/index.html', {'all_teams':all_teams})



def detail(request,team_id):
    try:
        team=Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        raise Http404("Team Does Not Exist")
    return render(request,'ITSP/detail.html',{'team':team})



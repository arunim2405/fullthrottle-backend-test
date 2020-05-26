from django.shortcuts import render
from backend.models import User, ActivityPeriod
from .serializers import UserSerializer,ActivityPeriodSerializer
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from datetime import datetime
# Create your views here.
class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


@api_view(["GET"])
def returnobj(request):
	try:
		rdata=User.objects.all()
		serializer_class = UserSerializer
		djason=UserSerializer(rdata,many=True).data
		for r in djason:
		 	id1=r['id']
		 	adata=ActivityPeriod.objects.filter(ids=id1)
		 	serializer_class = ActivityPeriodSerializer
		 	# for datas in adata:
			#  	datas['start_time'] = datetime.strptime(datas['start_time']).strftime("%b %d %Y %H:%M:%S")
			#  	datas['end_time'] = datetime.strptime(datas['end_time']).strftime("%b %d %Y %H:%M:%S")
		 	djason2=ActivityPeriodSerializer(adata, many=True).data
		 	r['activity_periods'] = djason2
		
		return JsonResponse(djason, safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)	
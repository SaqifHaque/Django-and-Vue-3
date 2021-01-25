from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from . models import Jobs
from . serializers import JobsSerializer


# def frontpage(request):
#     return render(request, 'core/base.html')

class JobsView(generics.RetrieveAPIView):
    queryset = Jobs.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = JobsSerializer(queryset, many=True)
        print(serializer)
        return Response(serializer.data)
        
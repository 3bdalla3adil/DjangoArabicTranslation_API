from django.http                import HttpResponse,HttpResponseRedirect
from django.shortcuts           import render
from django.shortcuts           import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response    import Response
from rest_framework.views       import APIView
from rest_framework             import generics,status

from .models                    import keyword
from .serializers               import KeywordSerializer


class ListKeyword(generics.ListCreateAPIView):
    queryset         = keyword.objects.all()
    serializer_class = KeywordSerializer


    def get( self, request, format=None):
        serializer = KeywordSerializer(self.queryset.all(), many=True)
        return Response(serializer.data)

    def post(self, request,  format=None):
        serializer = KeywordSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
            # return Response(serializer.data, status=status.HTTP_201_CREATED,)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailKeyword(generics.RetrieveUpdateDestroyAPIView):
    queryset         = keyword.objects.all()
    serializer_class = KeywordSerializer

    def get_object(self, pk):
        try:
            return keyword.objects.get(pk=pk)
        except keyword.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        keyword1   = self.get_object(pk)
        serializer = KeywordSerializer(keyword1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        keyword1   = self.get_object(pk)
        serializer = KeywordSerializer(keyword1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        keyword1   = self.get_object(pk)
        keyword1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HomePage(generics.GenericAPIView):
    
    def homy(self):
        home_page_html = "<h1>Welcome to Arabic Text Translation API HomePage</h1><br>"
        r = '<a href="/">APIView Page</a>'
        return HttpResponse(home_page_html+r)

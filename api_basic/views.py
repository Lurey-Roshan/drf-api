from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view   
from .models import Article
from .serializers import ArticleSerializers
from rest_framework.response import Response
from rest_framework import status
#fro generic views we are imporrting followings
from rest_framework import generics
from rest_framework import mixins
#for authintication in rest_framework
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
	serializer_class=ArticleSerializers
	queryset=Article.objects.all()

	lookup_field='id'

	#authentication_classes=[SessionAuthentication, BasicAuthentication]
	authentication_classes=[TokenAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, id=None):
		if id:
			return self.retrieve(request)
		else:

			return self.list(request)
	def post(self, request):
		return self.create(request)
	def put(self, request, id):
		return self.update(request, id=None)

	def delete(self, request, id):
		return self.destroy(request,id)





from rest_framework.views import APIView

class ArticleView(APIView):
	def get(self, request):
		articles=Article.objects.all()
		serializer=ArticleSerializers(articles, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer=ArticleSerializers(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
	def get_object(self, id):
		try:

			return Article.objects.get(id =id)

		except Article.DoesNotExist:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, id):
		article=self.get_object(id)
		serializer=ArticleSerializers(article)
		return Response(serializer.data)

	def put(self, request,id):
		article=self.get_object(id)
		serializer=ArticleSerializers(article,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id):
		article=self.get_object(id)
		article.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

#@csrf_exempt
#else we can do using
@api_view(['GET','POST'])
def article_list(request):
	if request.method=="GET":
		articles=Article.objects.all()
		serializer=ArticleSerializers(articles, many=True)
		#return JsonResponse(serializer.data, safe=False)
		return Response(serializer.data)

	elif request.method=="POST":
		#date=JSONParser().parse(request)
		#serializer=ArticleSerializers(data=data)
		serializer=ArticleSerializers(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def article_detail(request, pk):
	try:
		article=Article.objects.get(pk=pk)
	except Article.DoesNotExist:
		#return HttpResponse(status=404)
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method=="GET":
		serializer=ArticleSerializers(article)
		#return JsonResponse(serializer.data)
		return Response(serializer.data)

	elif request.method=="PUT":
		#data=JSONParser().parse(request)
		#serializer=ArticleSerializers(atricle, data=data)
		serializer=ArticleSerializers(article, data=request.data)

		if serializer.is_valid():
			serializer.save()
			#return JsonResponse(serializer.data)
			return Response(serializer.data)
		#return JsonResponse(serializer.errors,status=400)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	elif request.method == "DELETE":
		article.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

 #1:57
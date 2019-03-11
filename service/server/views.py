# from django.shortcuts import render
# from django.http import HttpResponse
# from server import models
# import json
# import uuid
# from django.core import serializers
# from django.core.serializers.json import DjangoJSONEncoder
#
# # Create your views here.
# def write_server(request):
#     data=json.loads(request.body)
#     data['id']=uuid.uuid4()   #生成一个基于时间的uuid作为主键
#     models.Person.objects.create(**data)
#     res={
#         'success':True
#     }
#     return HttpResponse(json.dumps(res),content_type='application/json')
#
#
# def read_server(request):
#     name=request.GET['name']
#     data=serializers.serialize('python',models.Person.objects.filter(name= name))
#     res={
#         'success':True,
#         'data':data
#     }
#     return HttpResponse(json.dumps(res,cls=DjangoJSONEncoder),content_type='application/json')


#对应APIView
#如果需要其他类型的请求，只需要在Test类里新建post、put等方法，前端发送请求的url是一样的，不同的请求方式会自动匹配到不同的函数
# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
#
# # Create your views here.
# class Test(APIView):
#     def get(self, request):
#         a = request.GET['a']
#         res = {
#             'success': True,
#             'data': 'a'
#         }
#         return Response(res)


#对应ViewSets 不使用**mixins类
# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import viewsets
# from rest_framework.decorators import list_route
# from server.serializers import PersonSerializer
# from server.models import Person
# import json
# import uuid
#
# # Create your views here.
# class PersonViewSet(viewsets.ModelViewSet):

    # @list_route(methods = ['post'])
    # def new_person(self, request):
    #     data = json.loads(request.body)
    #     data['id'] = uuid.uuid1()
    #     Person.objects.create(**data)
    #     res = {
    #         'success': True,
    #         'data': data
    #     }
    #     return Response(res)
    #
    # @list_route(methods = ['get'])
    # def all_person(self, request):
    #     data = PersonSerializer(Person.objects.all(), many = True).data
    #     res = {
    #         'success': True,
    #         'data': data
    #     }
    #     return Response(res)


#对应ViewSets 使用**mixins类
from rest_framework import viewsets
from server.serializers import PersonSerializer
from server.models import Person

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

from server.serializers import BookSerializer
from server.models import Book
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#重写ModelViewSet中的create方法
'''
class RecognitionViewSet(viewsets.ModelViewSet):
    queryset = re_photo.objects.all()        #上传图片界面
    serializer_class = PhotoSerializer
    permission_classes(IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)   #对上传的图片序列化
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        name_re_photo =serializer.data['name']     #提取字段name
        object_worker = worker.objects.filter(name=name_re_photo)  # 从worker中查询是否匹配name_re_photo
        if len(object_worker)!=0:                      #研究是否有匹配的name
            serializer2 = WorkerSerializer(object_worker, many=True)
            serializer2.data[0]['photo']='http://127.0.0.1:8000/api/recognition/'+serializer2.data[0]['photo']
            result = test.getresult(36)     #人脸识别函数，先构造简单函数替代

            return Response({
            "status": status.HTTP_200_OK,
            "message": 'Working right.',
            "tag": 'pass',
            "data": serializer2.data})    #返回worker中匹配的图片地址
        else:
            return Response({
            "status": status.HTTP_200_OK,
            "message": 'Working right.',
            "tag": 'no pass',
            "data": [ ]})
create方法的原始代码如下  地址 http://www.cdrf.co/3.1/rest_framework.viewsets/ModelViewSet.html

def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data) # request.data为上传的信息，经输出实验可知serializer.data是一个字典，可提取出name
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
--------------------- 
作者：ttxs2016 
来源：CSDN 
原文：https://blog.csdn.net/ttxs2016/article/details/79614868 
版权声明：本文为博主原创文章，转载请附上博文链接！

https://www.cnblogs.com/xiaojikuaipao/p/6009882.html
权限、自定义api、filters
https://www.jb51.net/article/142530.htm
django rest framework如何进行model的定义、序列化、增删改查以及搜索、排序等功能
'''





#cbv模式下的class例子
# class CLOGIN(View):
#     # 这个函数(了解作用即可，可不写)作用类似于装饰器，参数*args, **kwargs代表可传进去多个参数
#     def dispatch(self, request, *args, **kwargs):
#         # 重写dispatch方法，相当于执行get/post方法（关键看传来的是那种请求方式，如果是get请求方式，就执行get方法）
#         result = super(CLOGIN,self).dispatch(request, *args, **kwargs)
#         return result
#
#     # 函数名只能是get，一旦有get请求发来，就执行此函数
#     def get(self,request):
#         pass
#
#     # 函数名只能是post，一旦有post请求发来，就执行此函数
#     def post(self,request):
#         pass


#cfb模式下例子
# def login(request):
#     if request.method == 'POST':
#         pass
#     else:
#         pass
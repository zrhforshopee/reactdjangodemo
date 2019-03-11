#基于APIView的方式：更清晰的分隔不同HTTP方法
#如果需要其他类型的请求，只需要在Test类里新建post、put等方法，前端发送请求的url是一样的，不同的请求方式会自动匹配到不同的函数
# from server import views
# from django.conf.urls import url
# urlpatterns = [
#     url('test/', views.Test.as_view())   #CBV:class-views模式，是不常用的url对应views.py中对应的类的模式；
# ]



#使用ViewSets
from django.conf.urls import url, include
from server.views import PersonViewSet
from rest_framework.routers import DefaultRouter

from server.views import BookViewSet

router = DefaultRouter()
#使用Router类自动关联URL
#http://127.0.0.1:8000/支持的默认方法只有GET, POST, HEAD, OPTIONS
#http://127.0.0.1:8000/第一列的具体内容/ Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
router.register(r'person', PersonViewSet, base_name="person")    #CBV:class-views模式，是不常用的url对应views.py中对应的类的模式；
router.register(r'book', BookViewSet, base_name="book")    #CBV:class-views模式，是不常用的url对应views.py中对应的类的模式；

#可以注册不同的url对应不同的类
#rounter写法适用于每一个类中自定义方法
urlpatterns = [
    url('', include(router.urls))
]
# from server import views
# urlpatterns = [
#     url(r'', views.PersonViewSet.as_view({'get': 'list', 'post': 'create'})),
#     url(r"(?P<pk>[正则表达式匹配id])/$", views.PersonViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
#     #CBV:class-views模式，是不常用的url对应views.py中对应的类的模式；
#     #适用于用自带的ModelViewSet中的方法
# ]

# urlpatterns = [
#     url('test/', views.login())
# ]
#FBV:function-views模式，也是常用的url对应views.py中对应的函数；


#调用：
'''http://127.0.0.1:8000/e9b4ea68-1e0a-11e9-bb0c-784f438c4389/ put\get\delete'''
'''http://127.0.0.1:8000/ get获取所有\post'''
'''{
    "id": "e9b4ea68-1e0a-11e9-bb0c-784f438c4389",
    "name": "d",
    "age": 31,
    "time": "2019-01-24T06:22:56.312067Z"
}'''
'''{
    "name": "a",
    "age": 122
}'''
resetframework的写法

# 第一版

    from rest_framework.response import Response
    
    from drf_demo.models import Student
    
    
    class StudentSerializer(serializers.Serializer):
        # source用于展示字段和数据库字段不一致时，source指向数据库实际的字段，变量名为展示的字段
        names = serializers.CharField(source="name")
        sex = serializers.BooleanField()
        age = serializers.IntegerField()
        class_null = serializers.CharField()
    
    
    class StudentView(APIView):
    
        def get(self, request):
    
            # request.GET和request.query_params都可以用于获取get请求的请求参数
            # print(request.GET)
            # print(request.query_params)
    
            students = Student.objects.all()
            # 序列化时使用instance=students，
            # 反序列化时使用data=students
            # many=True用于对多个对象进行序列化,对单个对象进行序列化时其值为False,默认值为False
            serializer = StudentSerializer(instance=students, many=True)
            return Response(serializer.data)
    
        def post(self, request):
            serializer = StudentSerializer(data=request.data, many=False)
            try:
                serializer.is_valid(raise_exception=True)
                stu = Student.objects.create(**serializer.validated_data)
                ser = StudentSerializer(instance=stu, many=False)
                return Response(ser.data)
            except:
                return Response(serializer.errors)
    
    
    class StudentDetailView(APIView):
    
        def get(self, request, nid):
            student = Student.objects.get(pk=nid)
            serializer = StudentSerializer(instance=student, many=False)
            return Response(serializer.data)
        
        def delete(self, request, nid):
            Student.objects.get(pk=nid).delete()
            return Response()
        
        def put(self, request, nid):
            instance = Student.objects.get(pk=nid)
            serializer = StudentSerializer(data=request.data, instance=instance)
            try:
                serializer.is_valid(raise_exception=True)
                Student.objects.filter(pk=nid).update(**serializer.validated_data)
                stu = Student.objects.get(pk=nid)
                ser = StudentSerializer(instance=stu, many=False)
                return Response(ser.data)
            except:
                return Response(serializer.errors)

# 第二版

    from rest_framework.views import APIView
    from rest_framework import serializers
    from rest_framework.response import Response
    
    from drf_demo.models import Student, Publish
    
    
    class PublishSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Publish
            fields = ["name", "email"]
    
    
    class PublishView(APIView):
    
        def get(self, request):
            publishes = Publish.objects.all()
            ps = PublishSerializer(instance=publishes, many=True)
            return Response(ps.data)
    
        def post(self, request):
            serializer = PublishSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
                
                
    class PublishDetailView(APIView):
    
        def get(self, request, nid):
            publish = Publish.objects.get(pk=nid)
            serializer = PublishSerializer(instance=publish, many=False)
            return Response(serializer.data)
    
        def delete(self, request, nid):
            Publish.objects.get(pk=nid).delete()
            return Response()
    
        def put(self, request, nid):
            instance = Publish.objects.get(pk=nid)
            serializer = PublishSerializer(data=request.data, instance=instance)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)

# 第三版

    from rest_framework.views import APIView
    from rest_framework import serializers
    from rest_framework.response import Response
    from rest_framework.generics import GenericAPIView
    
    from drf_demo.models import Student, Publish, Author


​    
    class AuthorSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Author
            fields = ["name", "age"]


​    
    class AuthorView(GenericAPIView):
    
    	queryset = Author.objects.all()
        serializer_class = AuthorSerializer
    
        def get(self, request):
       		# instance=self.get_queryset()可以替换成filter_queryset()或者paginate_queryset()
       		#  当url匹配re_path('author/<?P=pk>(\d)+/', AuthorViewSet.as_view())这种有形参数时，要使用get_object()方法
    
            serializer = self.get_serializer(instance=self.get_queryset(), many=True)
            return Response(serializer.data)
    
        def post(self, request):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid:
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)


​    
    class AuthorDetailView(GenericAPIView):
    
        queryset = Author.objects.all()
        serializer_class = AuthorSerializer
    
        def get(self, request, nid):
            serializer = self.get_serializer(instance=self.get_queryset(), many=False)
            return Response(serializer.data)
    
        def delete(self, request, nid):
            self.get_object().delete()
            return Response()
    
        def put(self, request, nid):
            instance = self.get_object()
            serializer = PublishSerializer(data=request.data, instance=instance)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)

#  第四版

    from rest_framework.views import APIView
    from rest_framework import serializers
    from rest_framework.response import Response
    from rest_framework.generics import GenericAPIView
    from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
        UpdateModelMixin
    
    from drf_demo.models import Student, Publish, Author
    
    class AuthorSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Author
            fields = ["name", "age"]


​    
    class AuthorView(GenericAPIView, ListModelMixin, CreateModelMixin):
    
    	queryset = Author.objects.all()
        serializer_class = AuthorSerializer
    
        def get(self, request):
            return self.list(request)
    
        def post(self, request):
            return self.create(request)


​    
    class AuthorDetailView(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    
        queryset = Author.objects.all()
        serializer_class = AuthorSerializer
    
        def get(self, request, nid):
            return self.retrieve(request)
    
        def delete(self, request, nid):
            return self.destroy(request)
    
        def put(self, request, nid):
            return self.update(request)

# 第五版

    from rest_framework.views import APIView
    from rest_framework import serializers
    from rest_framework.response import Response
    from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
    from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
        UpdateModelMixin
        
    from drf_demo.models import Student, Publish, Author


​    
    class AuthorSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Author
            fields = ["name", "age"]


​     
    class AuthorView(ListCreateAPIView):
    	
    	queryset = Author.objects.all()
    	serializer_class = AuthorSerializer


​    	
    class AuthorDetailView(RetrieveUpdateDestroyAPIView):
    
    	queryset = Author.objects.all()
    	serializer_class = AuthorSerializer

# 第六版

```
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from rest_framework.viewsets import ModelViewSet

from drf_demo.models import Student, Publish, Author


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ["name", "age"]


class AuthorViewSet(ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
```




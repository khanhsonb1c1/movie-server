from rest_framework.serializers import ModelSerializer
from .models import Post


# thằng nào cho phép convert dữ liệu trong DB thành dữ liệu dùng dc
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

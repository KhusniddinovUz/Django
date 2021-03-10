from rest_framework import generics, permissions
from .models import ImageModel
from .serializers import ImageSerializer


class ImageApi(generics.ListAPIView):
    model = ImageModel
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny, ]

    queryset = ImageModel.objects.all()

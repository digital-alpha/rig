from rest_framework import serializers
from UploadMulti.models import Document, Detail

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('file',)

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = "__all__"
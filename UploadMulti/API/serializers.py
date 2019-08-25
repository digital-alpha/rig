from rest_framework import serializers
from UploadMulti.models import Document, Detail,Role

from django.contrib.auth import get_user_model
User = get_user_model()


class DocumentSerializer(serializers.ModelSerializer):
        # Create a custom method field
    uploaded_by = serializers.SerializerMethodField('_user')

    # Use this method for the custom field
    def _user(self, obj):
        return self.context['request'].user.username
    class Meta:
        model = Document
        fields = ('file','id', 'uploaded_at', 'uploaded_by')


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = "__all__"

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


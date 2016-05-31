from rest_framework import serializers
from restcore.models import SavedEmbeds

class EmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedEmbeds


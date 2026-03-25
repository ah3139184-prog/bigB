from rest_framework import serializers
from .models import DataSource, DataRecord,AIQuery,AnalysisResult


class DataSourceSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = DataSource
        fields = "__all__"
        read_only_fields = ["owner", "uploaded_at", "status"]



class DataRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRecord
        fields = "__all__"



class AnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisResult
        fields = "__all__"




class AIQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = AIQuery
        fields = "__all__"
        read_only_fields = ["answer"]
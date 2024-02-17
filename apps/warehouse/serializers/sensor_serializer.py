from rest_framework import serializers
from apps.warehouse.models.sensor_model import Sensor  # Asegúrate de tener el modelo Sensor
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class SensorDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = Sensor
        exclude = ('status', 'modified')

class SensorDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = Sensor
        fields = ('UNSAAC_TESIS_ELECTRONICA', 'data_cloro', 'data_turbidez')  # Ajusta los campos según tu modelo

class SensorBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('UNSAAC_TESIS_ELECTRONICA', 'data_cloro', 'data_turbidez')  # Ajusta los campos según tu modelo

class SensorCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        exclude = ('status', 'modified')

class SensorUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        exclude = ('sensor_id', 'status', 'modified')  # Asume que tu modelo Sensor tiene un campo 'sensor_id'
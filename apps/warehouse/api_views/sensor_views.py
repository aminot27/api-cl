import traceback

from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException, NotFound, ValidationError

from apps.warehouse.models.sensor_model import Sensor  # Asegúrate de tener este modelo
from apps.warehouse.repositories.sensor_repository import SensorRepository  # Asegúrate de tener este repositorio
from apps.warehouse.serializers.sensor_serializer import (  # Asegúrate de tener estos serializadores
    SensorSerializer,
    SensorDynamicResponse,
    SensorCreateRequest,
    SensorUpdateRequest
)
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView

class SensorsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    sensor_repository = SensorRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: SensorSerializer(many=True)})
    def get(self, request):
        try:
            sensors = self.sensor_repository.get_sensors()
            return SuccessResponse(data_=SensorSerializer(sensors, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: SensorDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        sensors = self.sensor_repository.post_sensors(*values, **params)
        if type(sensors) is FieldError:
            raise ValidationError(sensors)
        else:
            return SuccessResponse(
                data_=SensorDynamicResponse(sensors, many=True, fields=values).data).send()

class SensorView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    sensor_repository = SensorRepository()

    @swagger_auto_schema(request_body=SensorCreateRequest, responses={status.HTTP_200_OK: SensorSerializer()})
    def post(self, request):
        create_data = super().get_request_data(SensorCreateRequest(data=request.data))
        try:
            sensor = self.sensor_repository.create_sensor(create_data)
            return SuccessResponse(data_=SensorSerializer(sensor).data).send()
        except:
            tb = traceback.format_exc()
            print(tb)
            raise APIException(detail="Error creating sensor")

class SensorDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    sensor_repository = SensorRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: SensorSerializer()})
    def get(self, request, pk):
        sensor = self.sensor_repository.get_sensor(sensor_id=pk)
        if sensor is None:
            raise NotFound(detail="Sensor not found")
        else:
            return SuccessResponse(data_=SensorSerializer(sensor).data).send()

    @swagger_auto_schema(request_body=SensorUpdateRequest, responses={status.HTTP_200_OK: SensorSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=SensorUpdateRequest(data=request.data))
            sensor = self.sensor_repository.update_sensor(sensor_id=pk, sensor=update_data)
            if sensor is None:
                raise NotFound(detail="Sensor not found")
            else:
                return SuccessResponse(data_=SensorSerializer(sensor).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        sensor = self.sensor_repository.get_sensor(sensor_id=pk)
        deleted = self.sensor_repository.soft_delete_sensor(sensor_id=pk)
        if deleted is None:
            raise NotFound(detail="Sensor not found")
        else:
            return SuccessResponse(data_=SensorSerializer(sensor).data).send()
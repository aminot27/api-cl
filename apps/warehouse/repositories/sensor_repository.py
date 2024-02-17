# Asegúrate de importar tu modelo Sensor correctamente
from apps.warehouse.models.sensor_model import Sensor

class SensorRepository:

    @staticmethod
    def get_sensor(sensor_id):
        # Asume que tienes un método get_one en tu manager de objetos Sensor
        return Sensor.objects.get_one(sensor_id)

    @staticmethod
    def get_sensors(*values, **params):
        # Asume que tienes un método filter en tu manager de objetos Sensor
        return Sensor.objects.filter(*values, **params)

    @staticmethod
    def post_sensors(*values, **params):
        # Asume que tienes un método get_many en tu manager de objetos Sensor, similar a get_academies
        return Sensor.objects.get_many(*values, **params)

    @staticmethod
    def create_sensor(sensor):
        # Asume que tienes un método create_one en tu manager de objetos Sensor
        return Sensor.objects.create_one(**sensor)

    @staticmethod
    def update_sensor(sensor_id, sensor):
        # Asume que tienes un método update_one en tu manager de objetos Sensor
        return Sensor.objects.update_one(obj_primary_key=sensor_id, **sensor)

    @staticmethod
    def log_delete_sensor(sensor_id):
        # Asume que tienes un método log_delete_one en tu manager de objetos Sensor
        return Sensor.objects.log_delete_one(primary_key=sensor_id)

    @staticmethod
    def soft_delete_sensor(sensor_id):
        # Asume que tienes un método soft_delete_one en tu manager de objetos Sensor
        return Sensor.objects.soft_delete_one(primary_key=sensor_id)
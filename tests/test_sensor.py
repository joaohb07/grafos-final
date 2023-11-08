# test_sensor.py
import sys
import os
from classes.Sensor import Sensor

# Adicione o caminho do módulo à variável sys.path
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, module_path)


def test_sensor_initialization():
    sensor = Sensor("sensor1", "Sensor", 3, 4)
    assert sensor.node == "sensor1"
    assert sensor.node_type == "Sensor"
    assert sensor.x == 3
    assert sensor.y == 4

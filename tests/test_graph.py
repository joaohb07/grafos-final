import math
import pytest
from classes.Grafo import Graph
from classes.Sensor import Sensor


@pytest.fixture
def sample_graph():
    graph = Graph()
    sensors = [
        Sensor("A", "Sensor", 0, 0),
        Sensor("B", "Sensor", 1, 0),
        Sensor("C", "Sensor", 0, 1),
    ]
    for sensor in sensors:
        graph.add_sensor(sensor)
    graph.build_graph()
    return graph


def test_add_sensor():
    graph = Graph()
    sensor = Sensor("A", "Sensor", 0, 0)
    graph.add_sensor(sensor)
    assert len(graph.nodes) == 1


def test_calculate_distance():
    sensor1 = Sensor("A", "Sensor", 0, 0)
    sensor2 = Sensor("B", "Sensor", 3, 4)
    graph = Graph()
    distance = graph.calculate_distance(sensor1, sensor2)
    assert math.isclose(distance, 5.0, rel_tol=1e-9)


def test_build_graph(sample_graph):
    assert len(sample_graph.edges) == 3


def test_kruskal(sample_graph):
    mst, total_cost = sample_graph.kruskal()
    assert len(mst) == 2
    assert math.isclose(total_cost, 2.0, rel_tol=1e-9)


def test_prim(sample_graph):
    mst, total_cost = sample_graph.prim()
    assert len(mst) == 2
    assert math.isclose(total_cost, 2.0, rel_tol=1e-9)

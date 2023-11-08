from unittest.mock import Mock
import matplotlib.pyplot as plt
from helpers.Helpers import Helpers


def test_plot_graph(monkeypatch):
    def mock_show():
        pass

    monkeypatch.setattr(plt, 'show', mock_show)

    graph = Mock()
    graph.nodes = [Mock(x=1, y=2, node='A'), Mock(x=3, y=4, node='B')]
    graph.edges = [(graph.nodes[0], graph.nodes[1])]

    Helpers.plot_graph(graph, title='Test Graph')


def test_plot_mst(monkeypatch):
    def mock_show():
        pass

    monkeypatch.setattr(plt, 'show', mock_show)

    graph = Mock()
    graph.nodes = [Mock(x=1, y=2, node='A'), Mock(x=3, y=4, node='B')]
    graph.edges = [(graph.nodes[0], graph.nodes[1])]

    mst = graph.edges

    Helpers.plot_mst(graph, mst, title='Test MST')

import csv
from classes.Grafo import Graph
from classes.Sensor import Sensor
from helpers.Helpers import Helpers


def main():
    graph = Graph()

    with open('./data/sensores34.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header

        for row in csv_reader:
            node, node_type, x, y = row
            sensor = Sensor(node, node_type, float(x), float(y))
            graph.add_sensor(sensor)

    graph.build_graph()
    Helpers.plot_graph(graph, "Grafo Original")

    mst_kruskal, cost_kruskal = graph.kruskal()
    Helpers.print_final_mst("Kruskal", mst_kruskal, cost_kruskal)
    Helpers.plot_mst(graph, mst_kruskal, "Minimum Spanning Tree (Kruskal)")

    mst_prim, cost_prim = graph.prim()
    Helpers.print_final_mst("Prim", mst_prim, cost_prim)
    Helpers.plot_mst(graph, mst_prim, "Minimum Spanning Tree (Prim)")


if __name__ == "__main__":
    main()

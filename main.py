import csv
from classes.Grafo import Graph
from classes.Sensor import Sensor
from helpers.Helpers import Helpers


def main():
    graph = Graph()

    with open('./data/sensores45.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header

        for row in csv_reader:
            node, node_type, x, y = row
            sensor = Sensor(node, node_type, float(x), float(y))
            graph.add_sensor(sensor)

    graph.build_graph()
    Helpers.plot_graph(graph, "Grafo Original")

    mst_kruskal, cost_kruskal = graph.kruskal()
    print("\nMST Final Kruskal e Grafo:")
    for edge in mst_kruskal:
        print(f"Aresta: {edge[0].node} - {edge[1].node}, Distance: {edge[2]:.2f}")
    Helpers.plot_mst(graph, mst_kruskal, "Minimum Spanning Tree (Kruskal)")
    print(f"\nCusto Total (Kruskal): {cost_kruskal:.2f}\n")

    mst_prim, cost_prim = graph.prim()
    print("\nMST Final Prim e Grafo:")
    for edge in mst_prim:
        print(f"Aresta: {edge[0].node} - {edge[1].node}, Distance: {edge[2]:.2f}")
    Helpers.plot_mst(graph, mst_prim, "Minimum Spanning Tree (Prim)")
    print(f"\nCusto Total (Prim): {cost_prim:.2f}\n")


if __name__ == "__main__":
    main()

import math
from helpers.Helpers import Helpers


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_sensor(self, sensor):
        self.nodes.append(sensor)

    def calculate_distance(self, sensor1, sensor2):
        return math.sqrt(
            (sensor1.x - sensor2.x) ** 2 + (sensor1.y - sensor2.y) ** 2
        )

    def build_graph(self):
        for i in range(len(self.nodes)):
            for j in range(i + 1, len(self.nodes)):
                distance = self.calculate_distance(
                    self.nodes[i], self.nodes[j]
                )
                self.edges.append((self.nodes[i], self.nodes[j], distance))

    def kruskal(self):
        print("\nPasso a Passo do Algoritmo de Kruskal:")
        self.edges.sort(key=lambda edge: edge[2])
        parent = {}
        mst = []
        total_cost = 0

        for node in self.nodes:
            parent[node.node] = node.node

        for edge in self.edges:
            node1, node2, distance = edge
            if parent[node1.node] != parent[node2.node]:
                mst.append((node1, node2, distance))
                total_cost += distance
                old_parent = parent[node1.node]
                new_parent = parent[node2.node]
                for node in self.nodes:
                    if parent[node.node] == old_parent:
                        parent[node.node] = new_parent

                # Print the step-by-step process
                Helpers.print_mst_step_by_step(
                    node1,
                    node2,
                    distance,
                    total_cost
                )

        return mst, total_cost

    def prim(self):
        print("\nPasso a Passo do Algoritmo de Prim:")
        mst = []
        total_cost = 0

        start_node = self.nodes[0]
        unvisited_nodes = set(self.nodes)
        visited_nodes = set([start_node])

        while unvisited_nodes:
            nearest_edge = None
            for node in visited_nodes:
                for edge in self.edges:
                    if node in edge[:2] and (
                        edge[0] in unvisited_nodes
                        or edge[1] in unvisited_nodes
                    ):
                        if nearest_edge is None or edge[2] < nearest_edge[2]:
                            nearest_edge = edge

            if nearest_edge:
                mst.append(nearest_edge)
                total_cost += nearest_edge[2]
                if nearest_edge[0] in unvisited_nodes:
                    unvisited_nodes.remove(nearest_edge[0])
                if nearest_edge[1] in unvisited_nodes:
                    unvisited_nodes.remove(nearest_edge[1])

                visited_nodes.add(nearest_edge[0])
                visited_nodes.add(nearest_edge[1])

                # Print the step-by-step process
                Helpers.print_mst_step_by_step(
                    nearest_edge[0],
                    nearest_edge[1],
                    nearest_edge[2],
                    total_cost
                )
            else:
                break

        return mst, total_cost

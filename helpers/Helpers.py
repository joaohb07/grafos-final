import matplotlib.pyplot as plt


class Helpers:
    def plot_graph(graph, title="Graph"):
        plt.figure(figsize=(11, 9))
        for sensor in graph.nodes:
            plt.scatter(sensor.x, sensor.y, label=sensor.node)

        for edge in graph.edges:
            x1, y1 = edge[0].x, edge[0].y
            x2, y2 = edge[1].x, edge[1].y
            plt.plot([x1, x2], [y1, y2], 'k-', lw=0.5)

        plt.legend(loc="upper left", bbox_to_anchor=(1, 1), borderaxespad=0)
        plt.title(title)
        plt.show()

    def plot_mst(graph, mst, title="Minimum Spanning Tree"):
        plt.figure(figsize=(11, 9))
        for sensor in graph.nodes:
            plt.scatter(sensor.x, sensor.y, label=sensor.node)

        for edge in mst:
            x1, y1 = edge[0].x, edge[0].y
            x2, y2 = edge[1].x, edge[1].y
            plt.plot([x1, x2], [y1, y2], 'r-', lw=2)

        plt.legend(loc="upper left", bbox_to_anchor=(1, 1), borderaxespad=0)
        plt.title(title)
        plt.show()
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

    def print_mst_step_by_step(node1, node2, distance, total_cost):
        print("Adicionando Nó: {} - {}, ".format(node1.node, node2.node),
              end='')
        print("Distância: {:.2f}, ".format(distance), end='')
        print("Custo Total: {:.2f}".format(total_cost))

    def print_final_mst(algorithm, mst, cost):
        print(f"\nMST Final {algorithm} e Grafo:")
        for edge in mst:
            print("Aresta: {} - {}, Distancia: {:.2f}".format(
                edge[0].node,
                edge[1].node,
                edge[2]
            ))
        print(f"\nCusto Total ({algorithm}): {cost:.2f}\n")

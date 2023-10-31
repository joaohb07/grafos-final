# Trabalho Final de Grafos
----

Este projeto propõe abordar o desafio da otimização das redes de sensores sem fio, com o objetivo de encontrar a Minimum Spanning Tree (MST) que conecta todos os sensores à estação central de forma eficiente. Este problema desempenha um papel fundamental na construção de infraestruturas de rede eficazes.
A proposta envolve uma rede de sensores sem fio distribuídos geograficamente, cada um dos quais deve ser conectado à estação central por meio de cabos. A questão fundamental é encontrar a configuração de conexões que minimizem o comprimento total dos cabos, reduzindo assim custos e impactos ambientais.

Este problema pode ser formalizado como a busca da Minimum Spanning Tree (MST) em um grafo, onde:

- Cada sensor é representado como um nó no grafo.
- As distâncias entre sensores adjacentes representam o custo (comprimento do cabo) da conexão.
- O objetivo é encontrar uma árvore que conecte todos os sensores à estação central de forma que o custo total seja minimizado.

A solução para este problema tem aplicações práticas em várias áreas, como a economia de recursos em infraestruturas de redes, a minimização da pegada de carbono e a otimização de redes de sensores sem fio em áreas remotas.

Para resolver o problema da MST em redes de sensores sem fio, propomos as seguintes etapas, depois estimadas no cronograma:

- Coleta de Dados: A coleta de dados inclui a obtenção das coordenadas geográficas de cada sensor e da estação central. Isso pode ser realizado por meio de sistemas de posicionamento global (GPS), sistemas de georreferenciamento ou outros métodos de localização.
Modelagem do Grafo: A construção de um grafo, em que os sensores são representados como nós e as distâncias entre eles são as arestas, cria uma representação matemática do problema. Isso permite a aplicação de algoritmos de otimização.

- Algoritmo MST: Implementação de um algoritmo para encontrar a Minimum Spanning Tree no grafo. Algoritmos bem estabelecidos, como o algoritmo de Kruskal ou o algoritmo de Prim, são amplamente utilizados para resolver esse problema. A escolha do algoritmo depende das características específicas da rede.
Implementação e Testes: Desenvolvimento de um software que aplica o algoritmo MST à rede de sensores e avaliação dos resultados com base no custo total do cabo. Os testes podem ser conduzidos em ambientes simulados e reais para verificar a eficácia da solução proposta.

Espera-se que este projeto resulte em uma solução eficaz para a otimização de redes de sensores sem fio, proporcionando uma série de benefícios, incluindo:

- Uma implementação funcional do algoritmo MST, adaptada às necessidades específicas da rede de sensores em questão.

- Uma análise detalhada das soluções propostas e da economia de recursos alcançada em comparação com abordagens não otimizadas.

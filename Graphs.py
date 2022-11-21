def add_vertex(v):
    global Graph
    global Vertex_No
    Vertex_No += 1
    Graph[v] = []

def add_edge(v1,v2,cost):
    global Graph
    temp = [v2,cost]
    Graph[v1].append(temp)

def print_graph():
    global Graph
    for vertex in Graph:
        for edges in Graph[vertex]:
            print(vertex," attaches to ", edges[0], " weight: ", edges[1])

def ask_user():
    global Graph
    vertex = int(input("Input your new vertex or vertex to edit"))
    if vertex not in Graph:
        add_vertex(vertex)
    edge = input("Input a connected vertex, type end to cancel")
    while edge != "end":
        weight = int(input("What is the weight?"))
        add_edge(vertex,int(edge),weight)
        edge = input("Input a connected vertex, type end to cancel")
    print_graph()

Graph = {}
Vertex_No = 0

for i in range(1,5):
    add_vertex(i)

add_edge(1,2,5)
add_edge(1,4,3)
add_edge(2,1,5)
add_edge(2,3,6)
add_edge(3,2,6)
add_edge(3,4,1)
add_edge(4,1,3)
add_edge(4,3,1)

print_graph()

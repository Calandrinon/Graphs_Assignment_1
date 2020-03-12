from graph import DoubleDictGraph

"""
    TODO:
    - The graph shall be modifiable: it shall be possible to add and remove an edge,
    and to add and remove a vertex. Think about what should happen with the properties
    of existing edges and with the identification of remaining vertices. You may use
    an abstract Vertex_id instead of an int in order to identify vertices; in this case,
    provide a way of iterating the vertices of the graph.

    - The graph shall be copyable, that is, it should be possible to make an exact
    copy of a graph, so that the original can be then modified independently of its
    copy. Think about the desirable behaviour of an Edge_property attached to the
    original graph, when a copy is made.

    - Read the graph from a text file (as an external function); see the format below.

    - Write the graph from a text file (as an external function); see the format below.

    - Create a random graph with specified number of vertices and of edges
    (as an external function).
"""

def test_get_vertices():
    graph = DoubleDictGraph(30)
    graph.add_edge(0, 0, 1)
    graph.add_edge(0, 1, 7)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 1, -1)
    graph.add_edge(1, 3, 8)
    graph.add_edge(2, 3, 5)

    dict = {}
    for i in range(30):
        dict[i] = []
    dict[0] = [0, 1]
    dict[1] = [2, 3]
    dict[2] = [1, 3]

    assert(dict.keys() == graph.get_vertices())
    print("Vertex set getter test passed!")


def test_is_edge():
    graph = DoubleDictGraph(30)
    graph.add_edge(1, 2, 7)
    assert(graph.is_edge(1, 2) == True)
    assert(graph.is_edge(2, 3) == False)
    print("Edge existence check test passed!")


def test_add_edge():
    graph = DoubleDictGraph(30)
    graph.add_edge(4, 3, 15)
    assert(graph.is_edge(4, 3) == True)
    print("Edge addition test passed!")


def test_get_outbound_neighbours():
    graph = DoubleDictGraph(30)
    graph.add_edge(0, 2, 5)
    assert(graph.get_outbound_neighbours_of_vertex_X(0) == [2])
    print("Outbound neighbours of a node test passed!")


def test_get_inbound_neighbours():
    graph = DoubleDictGraph(30)
    graph.add_edge(0, 2, 5)
    assert(graph.get_inbound_neighbours_of_vertex_X(2) == [0])
    print("Outbound neighbours of a node test passed!")


def test_get_number_of_vertices():
    graph = DoubleDictGraph(30)
    assert(graph.get_number_of_vertices() == 30)
    print("Number of vertices getter test passed!")


def test_get_in_and_out_degree():
    graph = DoubleDictGraph(30)
    graph.add_edge(0, 0, 1)
    graph.add_edge(0, 1, 7)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 1, -1)
    graph.add_edge(1, 3, 8)
    graph.add_edge(2, 3, 5)
    assert(graph.get_in_and_out_degree(1) == (2, 2))
    print("In and out degree of a node test passed!")


def test_parse_outbound_edges():
    graph = DoubleDictGraph(30)
    graph.add_edge(0, 0, 1)
    graph.add_edge(0, 1, 7)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 1, -1)
    graph.add_edge(1, 3, 8)
    graph.add_edge(2, 3, 5)
    assert(graph.parse_outbound_edges_of_vertex_x(0) == [0, 1])
    print("Outbound edges of a node parsing test passed!")


def test_parse_inbound_edges():
    graph = DoubleDictGraph(30)
    graph.add_edge(0, 0, 1)
    graph.add_edge(0, 1, 7)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 1, -1)
    graph.add_edge(1, 3, 8)
    graph.add_edge(2, 3, 5)
    assert(graph.parse_inbound_edges_of_vertex_x(1) == [0, 2])
    print("Inbound edges of a node parsing test passed!")


def test_retrieve_edge_cost():
    graph = DoubleDictGraph(30)
    graph.add_edge(0, 0, 1)
    graph.add_edge(0, 1, 7)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 1, -1)
    graph.add_edge(1, 3, 8)
    graph.add_edge(2, 3, 5)
    assert(graph.retrieve_edge_cost(1, 3) == 8)
    print("Edge cost retrieval test passed!")


def test_modify_edge_cost():
    graph = DoubleDictGraph(30)
    graph.add_edge(0, 0, 1)
    graph.add_edge(0, 1, 7)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 1, -1)
    graph.add_edge(1, 3, 8)
    graph.add_edge(2, 3, 5)
    graph.modify_edge_cost(1, 3, 18)
    assert(graph.retrieve_edge_cost(1, 3) == 18)
    print("Edge cost modification test passed!")


def test_remove_edge():
    graph = DoubleDictGraph(30)
    graph.add_edge(0, 0, 1)
    graph.add_edge(0, 1, 7)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 1, -1)
    graph.add_edge(1, 3, 8)
    graph.add_edge(2, 3, 5)
    assert(graph.is_edge(0, 1) == True)

    graph.remove_edge(0, 1)

    assert(graph.is_edge(0, 1) == False)
    print("Edge removal test passed!")


def test_add_vertex():
    graph = DoubleDictGraph(1)
    graph.add_vertex(156)

    assert(graph.get_number_of_vertices() == 2)
    print("Vertex addition test passed!")


def test_remove_vertex():
    graph = DoubleDictGraph(30)
    graph.add_edge(0, 0, 1)
    graph.add_edge(0, 1, 7)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 1, -1)
    graph.add_edge(1, 3, 8)
    graph.add_edge(2, 3, 5)

    graph.remove_vertex(1)

    assert(graph.is_edge(0, 1) == False)
    assert(graph.is_edge(2, 1) == False)
    assert(graph.is_edge(1, 2) == False)
    assert(graph.is_edge(1, 3) == False)

    print("Vertex removal test passed!")


def test_copy_graph():
    graph = DoubleDictGraph(2)
    graph.add_edge(0, 1, 0)

    copy_of_the_graph = graph.copy()
    copy_of_the_graph.remove_vertex(0)
    copy_of_the_graph.remove_vertex(1)

    assert(copy_of_the_graph.get_number_of_vertices() == 0)
    assert(graph.get_number_of_vertices() == 2)

    print("Graph copy test passed!")


def main():
    test_get_vertices()
    test_is_edge()
    test_add_edge()
    test_get_outbound_neighbours()
    test_get_inbound_neighbours()
    test_get_number_of_vertices()
    test_get_in_and_out_degree()
    test_parse_outbound_edges()
    test_parse_inbound_edges()
    test_retrieve_edge_cost()
    test_modify_edge_cost()
    test_remove_edge()
    test_add_vertex()
    test_remove_vertex()
    test_copy_graph()

main()

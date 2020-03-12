import copy

class DoubleDictGraph:

    def __init__(self, number_of_nodes):
        self._dictOut = {}
        self._dictIn = {}
        self._dictCosts = {}

        for i in range(number_of_nodes):
            self._dictOut[i] = []
            self._dictIn[i] = []


    def get_vertices(self):
        """
            Returns an iterable containing all the vertices
        """
        return self._dictOut.keys()


    def get_number_of_vertices(self):
        """
            Returns the number of vertices in the graph
        """
        return len(self.get_vertices())


    def get_outbound_neighbours_of_vertex_X(self, x):
        """
            Returns a list containing the outbound neighbours of x
        """
        return self._dictOut[x]


    def get_inbound_neighbours_of_vertex_X(self, x):
        """
            Returns a list containing the inbound neighbours of x
        """
        return self._dictIn[x]


    def is_edge(self, x, y):
        """
            Returns True if there is an edge from x to y, False otherwise
        """
        try:
            return y in self._dictOut[x]
        except KeyError:
            return False


    def add_edge(self, x, y, cost):
        """
            Adds an edge from x to y with the cost "cost".
            Precondition: there is no edge from x to y
        """
        if self.is_edge(x, y):
            print("There is already an edge from {} to {}!\n".format(x, y))
            return

        self._dictOut[x].append(y)
        self._dictIn[y].append(x)
        self._dictCosts[(x, y)] = cost


    def remove_edge(self, x, y):
        """
            Removes the edge from x to y.
            Precondition: there is an edge from x to y.
        """

        if not self.is_edge(x, y):
            print("There is no edge between x and y!")
            return

        for node_index in range(0, len(self._dictOut[x])):
            if self._dictOut[x][node_index] == y:
                del self._dictOut[x][node_index]
                break

        for node_index in range(0, len(self._dictIn[y])):
            if self._dictIn[y][node_index] == x:
                del self._dictIn[y][node_index]
                break

        del self._dictCosts[(x, y)]


    def get_in_and_out_degree(self, vertex_number):
        """
            Gets the in degree and out degree of a vertex and returns it in
            a tuple.
        """
        return (len(self._dictIn[vertex_number]), len(self._dictOut[vertex_number]))


    def get_iterator_for_outbound_edges_of_vertex_x(self, vertex_number):
        """
            Returns an iterator for the outbound edges of vertex "vertex_number".
        """
        return iter(self._dictOut[vertex_number])


    def get_iterator_for_inbound_edges_of_vertex_x(self, vertex_number):
        """
            Returns an iterator for the outbound edges of vertex "vertex_number".
        """
        return iter(self._dictIn[vertex_number])


    def parse_outbound_edges_of_vertex_x(self, vertex_x):
        iterator = self.get_iterator_for_outbound_edges_of_vertex_x(vertex_x)
        outbound_edges_endpoints = []

        try:
            while True:
                outbound_edges_endpoints.append(next(iterator))
        except StopIteration:
            pass

        return outbound_edges_endpoints


    def parse_inbound_edges_of_vertex_x(self, vertex_x):
        iterator = self.get_iterator_for_inbound_edges_of_vertex_x(vertex_x)
        inbound_edges_startpoints = []

        try:
            while True:
                inbound_edges_startpoints.append(next(iterator))
        except StopIteration:
            pass

        return inbound_edges_startpoints


    def retrieve_edge_cost(self, vertex_x, vertex_y):
        return self._dictCosts[(vertex_x, vertex_y)]


    def modify_edge_cost(self, vertex_x, vertex_y, new_cost):
        self._dictCosts[(vertex_x, vertex_y)] = new_cost


    def add_vertex(self, vertex_x):
        self._dictOut[vertex_x] = []
        self._dictIn[vertex_x] = []


    def remove_vertex(self, vertex_x):
        # Removing inbound edges of vertex x from the neighbouring vertices
        for node_index in range(0, len(self._dictIn[vertex_x])):
            for node_index_2 in range(0, len(self._dictOut[self._dictIn[vertex_x][node_index]])):
                if self._dictOut[self._dictIn[vertex_x][node_index]][node_index_2] == vertex_x:
                    removed_edge = (self._dictIn[vertex_x][node_index], vertex_x)
                    del self._dictCosts[removed_edge]
                    del self._dictOut[self._dictIn[vertex_x][node_index]][node_index_2]
                    break

        # Removing outbound edges of vertex x from the neighbouring vertices
        for node_index in range(0, len(self._dictOut[vertex_x])):
            for node_index_2 in range(0, len(self._dictIn[self._dictOut[vertex_x][node_index]])):
                if self._dictIn[self._dictOut[vertex_x][node_index]][node_index_2] == vertex_x:
                    removed_edge = (vertex_x, self._dictOut[vertex_x][node_index])
                    del self._dictCosts[removed_edge]
                    del self._dictIn[self._dictOut[vertex_x][node_index]][node_index_2]
                    break

        del self._dictOut[vertex_x]
        del self._dictIn[vertex_x]


    def copy(self):
        copy_of_the_graph = copy.deepcopy(self)
        return copy_of_the_graph

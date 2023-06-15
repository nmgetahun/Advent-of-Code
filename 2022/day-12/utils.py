import math

ADJ_LOCS = [         (0, +1),
            (-1,  0),        (+1, 0),
                     (0, -1)         ]


class Vertex:
    def __init__(self, x, y, elevation, start = False, end = False):
        self.x = x
        self.y = y
        self.elevation = elevation
        self.start = start
        self.end = end
        self.adjacent = set()
        self.f_cost = math.inf
        self.g_cost = math.inf
        self.h_cost = None
        self.predecessor = None


    def add_edge(self, edge):
        self.adjacent |= {edge}


class Graph:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.cells = [[0 for _ in range(width)] for _ in range(length)]
        self.vertices = set()
        self.a_vertices = []


    def add_vertex(self, vertex):
        #print(vertex.x, vertex.y, chr(vertex.elevation))
        #print(len(self.cells[0]), len(self.cells))
        self.cells[vertex.y][vertex.x] = vertex
        self.vertices |= {vertex}
        if vertex.elevation == ord('a'):
            self.a_vertices.append(vertex)


    def _get_adj(self, vertex):
        loc = (vertex.x, vertex.y)
        adj = []
        for dr in ADJ_LOCS:
            x = loc[0] + dr[0]
            y = loc[1] + dr[1]
            if 0 <= x < self.width and 0 <= y < self.length:
                if self.cells[y][x].elevation - vertex.elevation <= 1:
                    adj.append((x, y))

        return adj


    def validate_vertices(self):
        for row in self.cells:
            for vertex in row:
                for adj_x, adj_y in self._get_adj(vertex):
                    vertex.add_edge(self.cells[adj_y][adj_x])


    def reset_costs(self):
        for vertex in self.vertices:
            vertex.f_cost = math.inf
            vertex.g_cost = math.inf
            vertex.h_cost = None
            vertex.predecessor = None


class MinHeap:
    @staticmethod
    def parent_index(i):
        """
        Calculate index of parent in heap given child index. Returns None if
        given index is root.

        Parameters:
            i : int : index of child

        Returns:
            int or None: index of parent if it exists
        """
        if i == 0:
            return None
        return (i - 1) // 2

    @staticmethod
    def left_child_index(i):
        """
        Calculate index of left child in heap given parent index.

        Parameters:
            i : int : index of parent

        Returns:
            int : index of child
        """
        return 2 * i + 1

    @staticmethod
    def right_child_index(i):
        """
        Calculate index of right child in heap given parent index.

        Parameters:
            i : int : index of parent

        Returns:
            int : index of child
        """
        return 2 * i + 2

    def __init__(self, max_capacity=999):
        """
        Constructor

        Parameters: 
            max_capacity : int (optional) : maximum capacity of minheap; 
                                            defaults to 999.
        """
        self.data = [None] * max_capacity
        self.index_of_item = {}
        self.next = 0

    def size(self):
        """
        Retrieve size of heap (number of elements in heap).

        Returns:
            int : number of elements in heap
        """
        return self.next

    def height(self):
        """
        Retrieve height of heap.

        Returns:
            int : max height from root to lowest child
        """
        return math.floor(math.log(self.next, 2)) + 1

    def is_empty(self):
        """
        Checks if heap is empty (has no elements)

        Returns:
            boolean : whether or not heap is empty
        """
        return self.next == 0

    def reset(self):
        """
        Resets heap to start at root.
        """
        self.next = 0
        self.index_of_item = {}

    def min(self):
        """
        Retrieves minimum element in heap if it exists.

        Returns:
            any or None : minimum element in heap if heap is not empty;
                          None otherwise
        """
        if self.is_empty():
            return None
        return self.data[0]

    def _swap(self, p, q):
        """
        Swaps two elements in heap.

        Parameters:
            p : any : first item in heap to be swapped
            q : any : second item in heap to be swapped
        """
        assert p < self.next and q < self.next
        tmp = self.data[p]
        tmq = self.data[q]
        self.data[p] = self.data[q]
        self.index_of_item[tmp[1]] = q
        self.data[q] = tmp
        self.index_of_item[tmq[1]] = p

    def _sift_up(self, pos):
        """
        Sift up an element in heap if its priority is less than that of its
        parent.

        Parameters:
            pos : int : index of element to be sifted up
        """
        if pos == 0:
            return
        pi = MinHeap.parent_index(pos)
        if self.data[pos][0] < self.data[pi][0]:
            self._swap(pos, pi)
            self._sift_up(pi)

    def _sift_down(self, pos):
        """
        Sift down an element in heap if its priority is greater than that of
        either of its children.

        Parameters:
            pos : int : index of element to be sifted down
        """
        curr = self.data[pos][0]
        li = MinHeap.left_child_index(pos)
        ri = MinHeap.right_child_index(pos)

        if li >= self.next:
            return

        lc = self.data[li][0]
        if li < self.next and ri >= self.next:
            if lc < curr:
                self._swap(pos, li)
                self._sift_down(li)
        else:
            rc = self.data[ri][0]
            m = min([curr, lc, rc])
            if rc == m:
                self._swap(pos, ri)
                self._sift_down(ri)
            elif lc == m:
                self._swap(pos, li)
                self._sift_down(li)

    def remove_min(self):
        """
        Removes and returns root (minimum) element from heap, then corrects heap
        to maintain MinHeap property (complete tree + all children <= parents).

        Returns:
            any : minimum element in heap
        """
        if self.is_empty():
            return None
        min_item = self.data[0]
        del self.index_of_item[min_item[1]]
        if self.next > 0:
            self.data[0] = self.data[self.next - 1]
            self.next -= 1
            self._sift_down(0)
            if self.next == 1:
                key = list(self.index_of_item.keys())[0]
                self.index_of_item[key] = 0
        return min_item

    def insert(self, priority, item):
        """
        Inserts a new element into minheap and sifts up if necessary to maintain
        valid MinHeap.

        Parameters:
            priority : int : priority of item
            item : any : item to be stored in heap
        """
        self.data[self.next] = (priority, item)
        self.index_of_item[item] = self.next
        self.next += 1
        self._sift_up(self.next - 1)

    def _verify(self, pos):
        """
        Recursively checks if MinHeap is valid (complete tree + all children <=
        parents).

        Parameters:
            pos : int : index to check for validity

        Returns:
            boolean : whether or not heap is valid
        """
        if pos >= self.next:
            return True
        curr = self.data[pos][0]
        li = MinHeap.left_child_index(pos)
        ri = MinHeap.right_child_index(pos)
        if ri < self.next:
            return (
                curr <= self.data[ri][0]
                and curr <= self.data[li][0]
                and self._verify(ri)
                and self._verify(li)
            )
        if li < self.next:
            return curr <= self.data[li][0] and self._verify(li)
        return True

    def verify(self):
        """
        Checks if MinHeap is valid (complete tree + all children <= parents).

        Returns:
            boolean : whether or not heap is valid
        """
        return self._verify(0)

    def show(self):
        """
        Prints readable representation of MinHeap.
        """
        if self.is_empty():
            print("[empty]")
            return
        linebreak = 1
        row_count = 0
        for i in range(self.next):
            print(self.data[i], end=" ")
            row_count += 1
            if row_count == linebreak or i == self.next - 1:
                print()
                linebreak *= 2
                row_count = 0

    def change_priority(self, item, new_prio):
        """
        Changes priority of item in heap then corrects to maintain MinHeap
        validity. Throws ValueError exception if item not already in heap.

        Parameters:
            item : any : item in heap
            new_prio : int : new priority of item

        Raises:
            ValueError : if item not currently an element in heap
        """
        if item not in self.index_of_item:
            raise ValueError("Cannot update priority of a non-existent item")

        index = self.index_of_item[item]
        self.data[index] = (new_prio, item)

        pi = index if index == 0 else MinHeap.parent_index(index)
        if self.data[pi][0] > new_prio:
            self._sift_up(index)
        else:
            self._sift_down(index)
import sys

class MinHeap:

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = []

    def __len__(self) -> int:
        """
        Returns length of the data
        :return: length of the data
        """
        return len(self.data)

    def empty(self) -> bool:
        """
        Returns if the heap is empty
        :return: true if empty
        """
        return len(self.data) <= 0

    def top(self):
        """
        Returns the top element of the heap
        :return: top element
        """
        if self.empty():
            return None
        return self.data[0]

    def get_left_child_index(self, index: int) -> int:
        """
        Return index of left child
        :param index: index of parent
        :return: index of left child
        """
        if len(self) < 2:
            return None
        
        child_index = 2 * index + 1
        
        if len(self) <= child_index:
            return None
        
        return child_index

    def get_right_child_index(self, index: int) -> int:
        """
        Return index of right child
        :param index: index of parent
        :return: index of right child
        """
        if len(self) < 3:
            return None
        
        child_index = 2 * index + 2
        
        if len(self) <= child_index:
            return None
        
        return child_index

    def get_parent_index(self, index: int) -> int:
        """
        Return index of parent
        :param index: index of child
        """
        if index % 2 == 0: 
            parent_index = (index - 2) // 2 # Right Child
        else:
            parent_index = (index - 1) // 2 # Left Child
            
        if len(self) <= parent_index or parent_index < 0:
            return None
        
        return parent_index
            

    def get_min_child_index(self, index: int) -> int:
        """
        Return index of min child
        :param index: index we are finding the child of
        :return: index of the min child
        """
        left = self.get_left_child_index(index)
        right = self.get_right_child_index(index)
        
        if left is None:
    
            if right is None:
                return None
            
            return right
        
        elif right is None:
            return left
        
        
        if self.data[left] >= self.data[right]:
            return right
        
        return left

    def percolate_up(self, index: int) -> None:
        """
        Percolates up the heap:
        :param index: index to percolate up from
        :return: None
        """
        parent = self.get_parent_index(index)
        if index > 0 and self.data[index] <= self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            self.percolate_up(parent)
    
    def percolate_down(self, index: int) -> None:
        """
        Percolates down the heap:
        :param index: index to percolate down from
        :return: None
        """
        min_child = self.get_min_child_index(index)
        if min_child is not None and self.data[min_child] < self.data[index]:
            self.data[min_child], self.data[index] = self.data[index], self.data[min_child]
            self.percolate_down(min_child)

    def push(self, val) -> None:
        """
        Push new value onto the heap
        :param val: value being pushed to the heap
        :return: None
        """
        self.data.append(val)
        self.percolate_up(len(self.data) - 1)

    def pop(self) :
        """
        Pop top value from the heap
        :return: value popped from the heap
        """
        if not self.empty():
            out = self.data[0]
            
            self.data[0] , self.data[-1] = self.data[-1], self.data[0]
            self.data.pop()
            self.percolate_down(0)
            
            return out   
        
class MaxHeap:

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = MinHeap()

    def empty(self) -> bool:
        """
        Returns if the heap is empty
        :return: true if empty
        """
        return len(self.data) <= 0

    def top(self) -> int:
        """
        Returns the top element of the heap
        :return: top element
        """
        if self.empty():
            return None
        return self.data.top() * -1

    def push(self, key: int) -> None:
        """
        Push new key onto the heap
        :param key: key being pushed to the heap
        :return: None
        """
        self.data.push(key * -1)

    def pop(self) -> int:
        """
        Pop top key from the heap
        :return: key popped from the heap
        """
        return self.data.pop() * -1

sys.stdin.readline()

stack = []

max_nums = MaxHeap()

in_stack = {}

for line in sys.stdin.readlines():
    line =  line.split(" ")
    
    action = int(line[0])
    
    match action:
        case 1:
            value = int(line[1])
            
            stack.append(value)
            max_nums.push(value)
            
            if value not in in_stack:
                in_stack[value] = 1
            else:
                in_stack[value] += 1
                                
        case 2:
            in_stack[stack.pop()] -= 1
            
        case 3:
            
            while 1:
                if in_stack[max_nums.top()] == 0:
                    max_nums.pop()
                else:
                    print (max_nums.top())
                    break
                
                    
            
        
            
            



        
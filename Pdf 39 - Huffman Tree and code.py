import heapq
from collections import defaultdict

# Node class to store characters, frequencies, and children for the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define less than operator to be used in priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree and generate codes
def huffman_codes(characters, frequencies):
    # Step 1: Build the priority queue (min-heap) of nodes
    heap = [Node(char, freq) for char, freq in zip(characters, frequencies)]
    heapq.heapify(heap)
    
    # Step 2: Build the Huffman Tree
    while len(heap) > 1:
        # Extract the two nodes with the smallest frequencies
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create a new internal node with the combined frequency
        internal_node = Node(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right
        
        # Add the new internal node back to the heap
        heapq.heappush(heap, internal_node)
    
    # The remaining node is the root of the Huffman Tree
    root = heap[0]
    
    # Step 3: Traverse the Huffman Tree to generate the codes
    huffman_code_map = {}
    
    def traverse(node, code):
        if node is None:
            return
        # If it's a leaf node, store the code for the character
        if node.char is not None:
            huffman_code_map[node.char] = code
        traverse(node.left, code + '0')
        traverse(node.right, code + '1')
    
    traverse(root, "")
    
    # Step 4: Return the list of Huffman codes for each character
    return [(char, huffman_code_map[char]) for char in characters]

# Test Case 1
n1 = 4
characters1 = ['a', 'b', 'c', 'd']
frequencies1 = [5, 9, 12, 13]
output1 = huffman_codes(characters1, frequencies1)
print(f"Test Case 1 Output: {output1}")

# Test Case 2
n2 = 6
characters2 = ['f', 'e', 'd', 'c', 'b', 'a']
frequencies2 = [5, 9, 12, 13, 16, 45]
output2 = huffman_codes(characters2, frequencies2)
print(f"Test Case 2 Output: {output2}")
      

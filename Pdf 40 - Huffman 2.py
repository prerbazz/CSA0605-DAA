import heapq

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

# Function to build the Huffman Tree
def build_huffman_tree(characters, frequencies):
    heap = [Node(char, freq) for char, freq in zip(characters, frequencies)]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        internal_node = Node(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right
        
        heapq.heappush(heap, internal_node)
    
    return heap[0]  # Root of the Huffman Tree

# Function to decode the Huffman encoded string
def decode_huffman(encoded_string, root):
    decoded_message = []
    current_node = root
    
    for bit in encoded_string:
        # Traverse the tree based on the bits (0 for left, 1 for right)
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        # If it's a leaf node, append the character to the decoded message
        if current_node.left is None and current_node.right is None:
            decoded_message.append(current_node.char)
            current_node = root  # Go back to the root for the next character
    
    return ''.join(decoded_message)

# Test Case 1
n1 = 4
characters1 = ['a', 'b', 'c', 'd']
frequencies1 = [5, 9, 12, 13]
encoded_string1 = '1101100111110'
root1 = build_huffman_tree(characters1, frequencies1)
output1 = decode_huffman(encoded_string1, root1)
print(f"Test Case 1 Output: {output1}")

# Test Case 2
n2 = 6
characters2 = ['f', 'e', 'd', 'c', 'b', 'a']
frequencies2 = [5, 9, 12, 13, 16, 45]
encoded_string2 = '110011011100101111001011'
root2 = build_huffman_tree(characters2, frequencies2)
output2 = decode_huffman(encoded_string2, root2)
print(f"Test Case 2 Output: {output2}")

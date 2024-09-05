class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(nums):
    def buildTreeHelper(start, end):
        if start > end:
            return None
        
        # Find the index of the maximum value in the current range
        max_index = start
        for i in range(start, end + 1):
            if nums[i] > nums[max_index]:
                max_index = i
        
        # Create the root node with the maximum value
        root = TreeNode(nums[max_index])
        
        # Recursively build the left and right subtrees
        root.left = buildTreeHelper(start, max_index - 1)
        root.right = buildTreeHelper(max_index + 1, end)
        
        return root
    
    return buildTreeHelper(0, len(nums) - 1)

# Helper function to print the tree in-order
def printTree(root):
    if root is None:
        return
    printTree(root.left)
    print(root.val, end=' ')
    printTree(root.right)

# Example usage
nums = [3, 2, 1, 6, 0, 5]
root = buildTree(nums)

print("In-order traversal of the tree:")
printTree(root)
print()

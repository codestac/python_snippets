# check if the binary tree is symmetric

def tree_sum(root):
    if root is NOde:
        return 0
    
    else:
        left = true_sum(root.left)
        right = tree_sum(root.right)
        
        return root.val + left + right #this is depth first search
    
    
def are_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
	else:
		return are_symmetric(root1.left, root2.right)
				and are_symmetric(root1.right, root2.left)
    
def is_symmetric(root):
    if root is None:
        return True
    return are_symmetric(root.left, root.right)

# time complexity is O(n) as it has to traverse thru each node on the tree
# space complex. is O(log n) required by a balanced binary tree



# gas station wher eyou start from a station and reach back to teh station without running out of gas

def can_traverse(gas, cost, start):
    n = len(gas)
    remaining = 0
    i = start 
    started = False
    
    while i!= start or not started:
        started = True
        remaining += gas[i] - cost[i]
        
        if remaining < 0:
            return  False
        
        
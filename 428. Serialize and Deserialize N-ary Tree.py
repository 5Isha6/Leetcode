#428. Serialize and Deserialize N-ary Tree
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        
        ser = []
        def preord(node):
            if not node:
                return
            ser.append(str(node.val))
            for i in node.children:
                preord(i)
            ser.append('#')
        
        preord(root)
        # print(' '.join(ser))
        return ' '.join(ser)
            
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        
        q = collections.deque(data.split())
        print(q)
        def helper():
            if not q:
                return None
            node = Node(int(q.popleft()), [])
            while q[0] != '#':
                node.children.append(helper())
            q.popleft()
            return node
        return helper()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

from tkinter import *

win = None

class Node():
    def __init__(self, value, left=None, right=None, depth=None, position=None, father=None):
        self.value = value
        self.left = left
        self.right = right
        self.depth = depth
        self.position = position
        self.father = father
        
class Fifo():
    def __init__(self):
        self.queue = []
    
    def __len__(self):
        return len(self.queue)

    def put(self, element):
        self.queue.append(element)
    
    def get(self):
        return self.queue.pop(0)

def draw_node(canvas, node, color, bg_color, height, position, depthIndex, widthIndex):
    if position == "left":
        # Edge Drawing
        if node.left != None:
            canvas.create_line((widthIndex.get(node.father)-depthIndex.get(node.depth), height), (widthIndex.get(node.father)-depthIndex.get(node.depth)-depthIndex.get(node.depth)/2, height+100), fill="black", width=2) # Left Edge
        if node.right != None:
            canvas.create_line((widthIndex.get(node.father)-depthIndex.get(node.depth), height), (widthIndex.get(node.father)-depthIndex.get(node.depth)+depthIndex.get(node.depth)/2, height+100), fill="black", width=2) # Right Edge

        # Node Drawing
        canvas.create_oval ((widthIndex.get(node.father)-depthIndex.get(node.depth)-15, height-15), (widthIndex.get(node.father)-depthIndex.get(node.depth)+15, height+15), fill=bg_color, outline="black", width=2)
        canvas.create_text (widthIndex.get(node.father)-depthIndex.get(node.depth), height, text=node.value, fill=color, anchor="center", justify="center")
        
        widthIndex[node.value] = widthIndex.get(node.father)-depthIndex.get(node.depth)
    elif position == "right":
        # Edge Drawing
        if node.left != None:
            canvas.create_line((widthIndex.get(node.father)+depthIndex.get(node.depth), height), (widthIndex.get(node.father)+depthIndex.get(node.depth)-depthIndex.get(node.depth)/2, height+100), fill="black", width=2) # Left Edge
        if node.right != None:
            canvas.create_line((widthIndex.get(node.father)+depthIndex.get(node.depth), height), (widthIndex.get(node.father)+depthIndex.get(node.depth)+depthIndex.get(node.depth)/2, height+100), fill="black", width=2) # Right Edge

        # Node Drawing
        canvas.create_oval ((widthIndex.get(node.father)+depthIndex.get(node.depth)-15, height-15), (widthIndex.get(node.father)+depthIndex.get(node.depth)+15, height+15), fill=bg_color, outline="black", width=2)
        canvas.create_text (widthIndex.get(node.father)+depthIndex.get(node.depth), height, text=node.value, fill=color, anchor="center", justify="center")
        
        widthIndex[node.value] = widthIndex.get(node.father)+depthIndex.get(node.depth)
    else:
        # Edge Drawing
        if node.left != None:
            canvas.create_line((depthIndex.get(node.depth), height), (depthIndex.get(node.depth)/2, height+100), fill="black", width=2) # Left Edge
        if node.right != None:
          canvas.create_line((depthIndex.get(node.depth), height), (depthIndex.get(node.depth)/2+depthIndex.get(node.depth), height+100), fill="black", width=2)# Right Edge

        # Root Drawing
        canvas.create_oval ((depthIndex.get(node.depth)-15, height-15), (depthIndex.get(node.depth)+15, height+15), fill=bg_color, outline="black", width=2)
        canvas.create_text (depthIndex.get(node.depth), height, text=node.value, fill=color, anchor="center", justify="center")
        widthIndex[node.value] = depthIndex.get(node.depth)
        #print(widthIndex[node.value])

# bfs = Breadth-first seach
def bfs(tree, fontColor="black", color="white"):
    q = Fifo()
    q.put(tree)

    depthIndex = {0:450}
    widthIndex = {}
    
    win = Tk()
    win.title("TreeDrawing")
    canvas = Canvas(win, width=900, height=900, bg="white")
    canvas.pack()
    height = 100
    while len(q) != 0:
        current = q.get()
        if current.father != None: 
            depthIndex[current.depth] = depthIndex.get(current.depth-1)/2

        draw_node(canvas, current, fontColor, color, height*(current.depth+1), current.position, depthIndex, widthIndex)

        if current.depth != None: print("----- Node's Depth : ",current.depth, " -----")
        print(current.value)

        if current.left != None:
            q.put(current.left)
        if current.right != None:
            q.put(current.right)
    #print(depthIndex)
    win.mainloop()

def treeAppend(tree, element, depth=0, position=None, father=None):
    if tree == None:
        if position == None:
            tree = Node(value=element, depth=depth)
        else:
            tree = Node(value=element, depth=depth, position=position, father=father)
    elif tree.value >= element:
        tree.leaf = False
        tree.left = treeAppend(tree.left, element, depth+1, "left", tree.value)
    else:
        tree.leaf = False
        tree.right = treeAppend(tree.right, element, depth+1, "right", tree.value)
    return tree

# arbre = Node(1, 
#             Node(2,
#                 Node(3, 
#                     Node(4, depth=3, position="left", father=3, leaf=True), 
#                     Node(5, depth=3, position="right", father=3, leaf=True), depth=2, position="left", father=2), 
#                 Node(6, depth=2, position="right", father=2, leaf=True), depth=1, position="left", father=1), 
#             Node(7, depth=1, position="right", father=1, leaf=True), depth=0)

# arbre2 = Node(1,
#               Node(2,
#                    Node(4, position="left", father=2, depth=2, leaf=True),
#                    Node(5, position="right", father=2, depth=2, leaf=True), position="left", father=1, depth=1),
#               Node(3,
#                    Node(6, position="left", father=3, depth=2, leaf=True),
#                    Node(7, position="right", father=3, depth=2, leaf=True), position="right", father=1, depth=1), depth=0)

arbre3 = None
arbre3 = treeAppend(arbre3, 8)
bfs(arbre3)
arbre3 = treeAppend(arbre3, 3)
bfs(arbre3)
arbre3 = treeAppend(arbre3, 10)
bfs(arbre3)
arbre3 = treeAppend(arbre3, 1)
bfs(arbre3)
arbre3 = treeAppend(arbre3, 14)
bfs(arbre3)
arbre3 = treeAppend(arbre3, 6)
bfs(arbre3)
arbre3 = treeAppend(arbre3, 4)
bfs(arbre3)
arbre3 = treeAppend(arbre3, 7)
bfs(arbre3)
arbre3 = treeAppend(arbre3, 13)
bfs(arbre3)

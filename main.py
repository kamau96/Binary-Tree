class Node:
  def __init__(self,data):
    self.left=None
    self.right=None
    self.data=data
def inorder(temp):
  if (not temp):
    return
  inorder(temp.left) 
  print(temp.key,end = " ")
  inorder(temp.right) 

def insert(temp, key):
  if not temp:
    root= Node(key)
    return 
  queue=[]
  queue.append(temp)
  while (len(queue)):
    temp=queue[0]
    queue.pop(0)
    if (not temp.left):
      temp.left=Node(key)
      break
    else:
      queue.append(temp.left)
    if (not temp.right):
      temp.right=Node(key)
      break
    else:
      queue.append(temp.right)

def deleteDeepest(root,d_node):
  queue=[]
  queue.append(root)
  while len(queue):
    temp=queue.pop(0)
    if temp is d_node:
      temp=None
      return
    if temp.right:
      if temp.right is d_node:
        temp.right=None
      else:
        queue.append(temp.right)
    if temp.left:
      if temp.left is d_node:
        temp.left=None
      else:
        queue.append(temp.left)
def deletion(root,key):
  if root==None:
    return None
  if root.left==None and root.right==None:
    if root.data==key:
      return None
    else:
      return root
  key_node=None
  queue=[]
  queue.append(root)
  while len(queue):
    temp=queue.pop(0)
    if temp.data==key:
      key_node=temp
    if temp.left:
      queue.append(temp.left)
    if temp.right:
      queue.append(temp.right)
  if key_node:
    x=temp.data
    deleteDeepest(root,temp)
    key_node.data=x
  return root
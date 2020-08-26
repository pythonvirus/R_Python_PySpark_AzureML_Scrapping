#Global Variables
PoliceRoot=None
counter=0

class DriverHash:

    def __init__(self):
        """
		Updating the Default constructor. 
        initializes DriverHash Class Object which points to NULL
        
		"""
        self.driverhash = None

    def initializeHash(self):
        """
        initializes Hash Table of size(size) which points to NULL
        Args:
            size:Size of the Hash Table
        Returns:
            Hash Table object created with specified size
        """
        self.driverhash = [[] for _ in range(10)]
    

def insertHash(driverhash, lic):
    """
    This function inserts the license number(lic) to the hash table(driverhash).
    It inserts a license number if its not already present. If its already present
    then it updates the violation count for that license number
    Args:
        driverhash: HashTable
        lic: License number of violator
    Debugs:
        Print Message if the license has been successfully Inserted/updated or not
    """
    if (driverhash.driverhash is None):
        driverhash.initializeHash()

    # Calculate hashkey of the license key
    hash_key = int(lic) % len(driverhash.driverhash)
    # initialize Key exists to False
    key_exists = False

    # Extract the bucket based on hash key
    bucket = driverhash.driverhash[hash_key]

    # Iterate over bucket to check for license
    for i, kv in enumerate(bucket):
        key, value = kv
        # break if key exists
        if lic == key:
            key_exists = True
            break
    # Update violation count if license(key) exists else insert license number
    if key_exists:
        bucket[i] = ((lic, value + 1))
        #print("Licence Key:", lic,bucket[i], " has been successfully updated")
    else:
        bucket.append((lic, 1))
        driverhash.driverhash[hash_key] = bucket
        #print("Licence Key:", lic,hash_key,bucket, " has been successfully inserted")


def printViolators(driverhash):
    """
    This function prints the serious violators by looking through all hash table entries
    and printing the license numbers of the drivers who have more than 5 violations
    onto the file violators.txt
    Args:
        driverhash: HashTable
    Returns:
        Creates violators.txt file with Licence no. and violation details
    If driverhash is none then file will have just below output
    "--------------Violators-------------"    
    """
    output = open("violators.txt","w")
    output.write("--------------Violators-------------\n")
    if driverhash.driverhash != None:
       for item in driverhash.driverhash:
           if len(item) > 0:
              for data in item:
                  lic, violation = data[0], data[1]
                  if violation >= 5:
                      output.write(str(lic)+", "+str(violation)+"\n")
    output.close()


def destroyHash(driverhash):
    """
    This function destroys all entries in the hash table
    Args:
        driverhash: HashTable
    """
    # destroys and reinitializes hash table
    driverhash.driverhash = None
    print("Hash Table has been cleaned!");
	
# Node class 
# It has three properties policeId, fineAmt and bookingCount
class PoliceNode:
    def __init__(self, policeId, fineAmt):
        self.policeId = policeId
        self.fineAmt = fineAmt
        self.bookingCount = 1
        
        # stores the left child
        self.left = None
        
        # stores the right child
        self.right = None


def insertByPoliceId(policeRoot, policeId, fineAmt):
    """This function inserts an entry <policeId, amount> into the police tree ordered by police id. 
    If the Police id is already found in the tree, then this function adds up to the existing amount to get the total amount collected by him. 
    This function returns the root node of updated tree.

    Args:
        policeRoot (PoliceNode): Root node of the police tree
        policeId (int): id of the police 
        fineAmt (float): Fine amount collected by police

    Returns:
        PoliceNode: root node of the updated police tree ordered by policeId
    Debugs:
        print the root node content.

    Examples:
        >>> policeRoot = None
        >>> root = insertByPoliceId(root,10,10)

    """
    # check if police id and fine amt are not null. 
    if (policeId is not None) & (fineAmt is not None):
        
        # check if root of tree is not null
        if(policeRoot is None):
            policeRoot = PoliceNode(policeId,fineAmt)
            #print("Adding Root Node",policeRoot.policeId,policeRoot.fineAmt,policeRoot.bookingCount)
        else:
            # if not null, then call function _insertByPoliceId to insert the PoliceNode in tree
            _insertByPoliceId(PoliceNode(policeId,fineAmt), policeRoot)
    
    return policeRoot


def _insertByPoliceId(node, treeNode):
    """This function is called inside the insertByPoliceId to handle the recursive call.
       This helps in inserting the PoliceNode and creating the BST based on the policeId.
       It insert nodes based on three cases:
       Case 1. If inserting node policeId is less than tree root node policeId, then it goes to left child of root node 
       Case 2. If inserting node policeId is greater than tree root node policeId, then it goes to right child of root node
       Case 3. If inserting node policeId is equal to tree root node policeId, then it updates the fineAmt of tree root node
    Args:
        node (PoliceNode): police tree node which is to be inserted
        treeNode (PoliceNode): tree node which it is to be traversed

    Debugs:
        print statements to see which node added to left and right.
        Print statement to show updated value if node.
        

    Examples:
        >>> _insertByPoliceId(PoliceNode(policeId,fineAmt), policeRoot)

    """    
    
    # If inserting node policeId is less than tree root node policeId
    if(node.policeId < treeNode.policeId):
        if(treeNode.left is not None):
            _insertByPoliceId(node, treeNode.left)
        else:
            treeNode.left = node
            #print("Adding to left....",node.policeId,"<----",treeNode.policeId)
            
    # If inserting node policeId is greater than tree root node policeId
    if(node.policeId > treeNode.policeId):
        if(treeNode.right is not None):
            _insertByPoliceId(node, treeNode.right)
        else:
            treeNode.right = node
            #print("Adding to right....",treeNode.policeId,"---->",node.policeId,)
            
    # If inserting node policeId is equal to tree root node policeId
    if(node.policeId == treeNode.policeId):
        treeNode.fineAmt = treeNode.fineAmt + node.fineAmt
        treeNode.bookingCount=treeNode.bookingCount+1
        #print("Updating Node",treeNode.policeId,treeNode.fineAmt,treeNode.bookingCount)

def printPoliceTree(policeRoot):
    """This function is meant for debugging purposes. This function prints the contents of the PoliceTree in-order.
    It calls the function _printPoliceTree internally by passing the root node of tree.
    Args:
        policeRoot (PoliceNode): Root node of the police tree

    Returns:
        print the contents of Police tree in-order else print "Tree is empty"

    Examples:
        >>> printPoliceTree(policeRoot)

    """    
    
    if(policeRoot != None):
        _printPoliceTree(policeRoot)
    else:
        print('Tree is empty')
        
        
def _printPoliceTree(node):
    """This function is called inside the printPoliceTree function to handle the recursive call.
    It traverses the tree by passing left and right child of root node recursively and prints the PoliceNode
    contents if node is not null. 
    It prints the tree inorder traversal
    Args:
        policeRoot (PoliceNode): node of the police tree

    Returns:
        print the contents of Police tree in-order.
    Examples:
        >>> printPoliceTree(policeRoot)

    """    

    if(node != None):
        _printPoliceTree(node.left)
        print('police ID {} fineAmt {} BookingCount {}'.format(node.policeId,node.fineAmt,node.bookingCount))
        _printPoliceTree(node.right)
		
def reorderPoliceTree(policeRoot):
    """This function reorders the Binary Tree on the basis of total BookingCount, instead of police id. 
    This function calls the function _reorderByBookingCount internally to handle the recursive call if policeRoot is not none.
    Args:
        policeRoot (PoliceNode): Root node of the police tree

    Returns:
    
    Examples:
        >>> root = None
            root = insertByPoliceId(root,10,10)
            root = insertByPoliceId(root,2,100)
            new_tree = reorderByFineAmount(root)
            printPoliceTree(new_tree)

    """    
    _tree = None
    # call recursive to traverse police tree
    if(policeRoot != None):
        return _reorderByBookingCount(policeRoot,_tree)
    else:
        print('Tree is empty')
		


def _reorderByBookingCount(node,_tree):
    """This function is called from reorderPoliceTree. It recursively traverses the policeRoot node tree and
       calls the function insertByBookingCount for each node of tree. 
    Args:
        node (PoliceNode): Node of the police tree

    Returns:
        PoliceNode: root node of new tree ordered by fineAmt 

    Examples:
        >>> _tree = None
            root = None
            root = insertByPoliceId(root,10,10)
            root = insertByPoliceId(root,2,100)
            _tree = _reorderByBookingCount(root,_tree)
            printPoliceTree(_tree)
    """    
    
    # check if node is null that is stopping condition of Recursion.
    if(node != None):
        
        # call insertByBookingCount when node is visited
        _tree = insertByBookingCount(_tree,node.policeId,node.fineAmt,node.bookingCount)
        
        # call left child recursively
        _tree = _reorderByBookingCount(node.left,_tree)
    
        # call right child recursively
        _tree = _reorderByBookingCount(node.right,_tree)
        #Deleting records from old Police tree
        destroyPoliceTree(node)
        #Reset the Global Variable
        global PoliceRoot
        PoliceRoot=None
    
    # return root node of updated tree
    return _tree
	
def insertByBookingCount(policeRoot, policeId, fineAmt,bookingCount):
    """This function is called from _reorderByBookingCount. It calls the function _insertByBookingCount which helps
    in inserting the PoliceNode by BookingCount. It calls the function _insertByBookingCount by passing tree root. 
    Args:
        policeRoot (PoliceNode): Node of the police tree
        policeId (int): id of the police 
        bookingCount (int): Booking count by police

    Debugs:
        PoliceNode: root node of the updated police tree ordered by bookingCount

    Examples:
        >>> root = None
        >>> root = insertByBookingCount(root,10,300)
        >>> root = insertByBookingCount(root,20,100)
        >>> printPoliceTree(root)

    """    
    # create new tree ordered by BookingCount
    # check for the policeid and BookingCount
    if (policeId is not None) & (fineAmt is not None):
        node = PoliceNode(policeId,fineAmt)
        node.bookingCount= bookingCount
        
        # initialize root
        if(policeRoot is None):
            policeRoot = node
           # print("Adding Root Node",policeRoot.policeId,policeRoot.fineAmt,policeRoot.bookingCount)
        else:
            # call insert recursively to find insert position of node
            _insertByBookingCount(node, policeRoot)
                   

    return policeRoot

def _insertByBookingCount(node, treeNode):
    """This function is called inside the insertByBookingCount to handle the recursive call.
       This helps in inserting the PoliceNode and creating the BST based on the BookingCount.
       It insert nodes based on three cases:
        a. If inserting node BookingCount is less than or equal to tree root node BookingCount, then it goes to left child of root node 
        b. If inserting node BookingCount is greater than tree root node BookingCount, then it goes to right child of root node
    Args:
        node (PoliceNode): police tree node which is to be inserted
        treeNode (PoliceNode): tree node which it is to be traversed

    Debugs:
        print statement to see which node is added to left and right by booking count.

    Examples:
        >>> policeRoot = PoliceNode(11,100)
        >>> policeRoot =_insertByPoliceId(PoliceNode(10,1000), policeRoot)
        >>> printPoliceTree(policeRoot)

    """    
    
    # if fineAmt is less or equal to tree node fine amt
    if(node.bookingCount <= treeNode.bookingCount):
        # traverse left child and insert node
        if(treeNode.left is not None):
            _insertByBookingCount(node, treeNode.left)
        else:
            treeNode.left = node
            #print("Adding to left....",node.policeId,"!",node.bookingCount,"<----",treeNode.policeId,"!",treeNode.bookingCount)

    # if fineAmt is greater than tree node fine amt                    
    if(node.bookingCount > treeNode.bookingCount):
        # traverse right child and insert node
        if(treeNode.right is not None):
            _insertByBookingCount(node, treeNode.right)
        else:
            treeNode.right = node
            #print("Adding to right....",treeNode.policeId,"!",treeNode.bookingCount,"---->",node.policeId,"!",node.bookingCount)

def printPolicemen (policeRoot):
    '''
    This function prints the list of police ids which have not met the target of at least 10 bookings.
    The output is pushed to a file called police.txt. The output will be in the format
    -------------- Police list -------------
    Police id, no of bookings
    
    if policeRoot is Null then we will get below output in file.
    -------------- Police list -------------
    '''
    with open('police.txt', 'w') as file:
        file.write('-------------- Police list -------------\n')
    _printPolicemen(policeRoot)

def _printPolicemen(node):
    '''
    _printPolicemen:
    Helper function for printPolicemen function
    '''
    if(node != None):
        _printPolicemen(node.left)
        if node.bookingCount < 10:
            #print('police ID {}, BookingCount {}'.format(node.policeId, node.bookingCount))
            with open('police.txt', 'a') as file:
                file.write('{}, {}\n'.format(node.policeId, node.bookingCount))
        _printPolicemen(node.right)

def printTopTen(policeRoot):
    '''
    This function prints the list of top 10 police ids based on total number of bookings.
    The output is pushed to a file called police.txt. The output will be in the format
    -------------- Police Top 10 -------------
    Police id, no of bookings, total fine amount
    
    if policeRoot is Null then we will get below output in file along with old available content.
     -------------- Police Top 10 -------------
    '''
    with open('police.txt', 'a') as file:
        file.write('-------------- Police Top 10 -------------\n')
    global counter
    counter = 0
    _printTopTen(policeRoot)


def _printTopTen(node):
    '''
    _printTopTen
    Helper function for printTopTen Function
    We are traversing tree in format of Right root left
    '''
    global counter
    if (node != None) and counter < 10:
        _printTopTen(node.right)
        #print(counter, node.policeId, node.bookingCount, node.fineAmt)
        with open('police.txt', 'a') as file:
            file.write('{}, {}, {}\n'.format(node.policeId, node.bookingCount, node.fineAmt))
            counter = counter + 1
        _printTopTen(node.left)

def destroyPoliceTree(policeRoot):
    policeRoot.left = None
    policeRoot.right = None
    policeRoot.policeId = None
    policeRoot.fineAmt = None
    policeRoot.bookingCount= None
   

#Below code has been used to validate the functions
'''
if __name__ == '__main__':
    #import os
    path="E:\\Sachin\\Learning\\1.M.Tech\\1stSemester\\4.DataStructure and Algorithm\\Assginment1\\"
    #Intialize Hash Table & Tree
    myhash = DriverHash()
    #root = None
    for line in open(path+"inputPS11.txt").readlines():
        lic = int(line.split("/")[1])
        policeid = int(line.split("/")[0])
        fineamount = int(line.split("/")[2])
        insertHash(myhash,lic)
        PoliceRoot = insertByPoliceId(PoliceRoot,policeid,fineamount)
    #Print Violators
    printViolators(myhash)    
    #printBonusPolicemen(root)
    
    ## print hash
    print(myhash.driverhash) #need to handal none
    
    ## print Police Tree
    printPoliceTree(PoliceRoot)
    
    ## print police tree ordered by Booking count
    root=reorderPoliceTree(PoliceRoot)
    printPoliceTree(root)
    
    
    #Printpoliceman
    printPolicemen(root)
    
    #Print top10
    printTopTen(root)
    
    ## destroy police tree
    destroyPoliceTree(root)
    
    #print destroyed police tree
    printPoliceTree(PoliceRoot)
    print(PoliceRoot)
'''
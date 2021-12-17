import numpy as np
def getABC(A_String):
    rows=A_String.split("\n") # split string in evry new line
    A_mat=[] # empty list
    #print('this rows',rows) #this rows ['1 1 -1 0', '0 -1 0 1', '-1 0 1 -1']
    for i in rows: # looping on every string in list row
        columns=i.split(" ") # list of first string in list rows
        columns=[eval(item) for item in columns] # make it eval
        A_mat.append(columns) # adding it to A list
    A=np.array(A_mat) #make it Matrix
    #barnches_num=A.shape[1] # useless line
    new_row= [-1*sum(A[:,i]) for i  in range(A.shape[1])] # making new row to complete the matrix
    isFullMat=(1 or -1) not in new_row # check if full or not
    if(not isFullMat): # check if not full  to add the new row
        A_mat.append(new_row) # add new list to list
        A=np.array(A_mat) # make it matrix
    nodes=A.shape[0] # get the number of the node (number of rows)
    links_num=A.shape[1]-nodes+1 # number of links number of branches

    if(nodes==A.shape[1]-links_num): # check the AT is it square or not (rows == columns )
        A_Tree=A[:,:-1*(A.shape[1]-links_num)] # getting A tree columns only (A - link columns)
        A_Link=A[:,-1*links_num:] # getting A link columns only (A - tree columns)

    else: # A tree not square
        A_Tree=A[:-1,:-1*(A.shape[1]-links_num)] # getting A tree without the last row
        A_Link=A[:-1,-1*links_num:] # getting A link without the last row
    C_Link=np.dot(np.linalg.inv(A_Tree),A_Link) #CL =AT^-1 . AL
    Cut_set=np.concatenate((np.identity(C_Link.shape[0]),C_Link),1)# calculate Cutset CL + I
    B_Tree=-1*C_Link.T #BT = -CL trans
    Tie_set=np.concatenate((B_Tree,np.identity(B_Tree.shape[0])),1) # calculate Teiset CL + I
    
    return A,Tie_set,Cut_set
def get_JB_VB(B,ZB,EB,IB):
    zmat = list(ZB.split())#ZB edit line AS I/P
    Zb_diag = []
    for item in zmat:
        Zb_diag.append(eval(item))
    ZB_matrix = np.diag(Zb_diag)
    #print(ZB_matrix)
    bzb_bt=np.dot(B,np.dot(ZB_matrix,np.transpose(B)))
    #print(bzb_bt)
    eb_matrix=EB.split()#editline as I/P
    EB_matrix =[]
    for item in eb_matrix:
      EB_matrix.append(eval(item))
    #print(EB_matrix)
    B_EB=np.dot(B,EB_matrix) # B mat * EB MAT
    #print(B_EB)
    IL=np.dot(np.linalg.inv(bzb_bt),B_EB) # IL MAT
    #print(IL)
    JB=np.dot(np.transpose(B),IL)# JB MATrix every current in circuit
    #print(JB)
    iblist=IB.split()
    IB_MAT=[]
    for item in iblist:
      IB_MAT.append(eval(item))
    VB=[]
    jbpulsib=JB+IB_MAT
    #print(jbpulsib)
    VB=(np.dot(ZB_matrix,jbpulsib))-EB_matrix
    #print(VB)
    return JB,VB
a='''1 1 -1 0
0 -1 0 1
-1 0 1 -1'''
A,B,C=getABC(a)
print("tie set:\n",B)
print("Cut set:\n",C)
print("A:\n",A)
JB,VB=get_JB_VB(ZB='5 10 5 5',B=B,EB='0 0 10 0',IB='0 0 0 0')

print("I:\n",JB)
print("V\n",VB)


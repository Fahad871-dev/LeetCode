class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)     #rows
        m=len(matrix[0])    #columns
        total=n*m           #total elements in matrix
        c=0                 #count
        ans=[]             #ans is a list in which element return
        colstart=0        #column start from 0
        rowstart=0          #row start from 0
        colend=m-1          #column end
        rowend=n-1           #row end 

        while c<total:
            #1st upper row left to right =colstart->colend
            for i in range(colstart,colend+1):
                ans.append(matrix[rowstart][i])
                c+=1
            rowstart+=1
            if c==total:
                break


            #right column from up to down:  colend, rowstart->rowend+1
            for i in range(rowstart,rowend+1):
                ans.append(matrix[i][colend])
                c+=1
            colend-=1     
            if c==total:
                break

            #lastrow rowend=colend to colstart
            for i in range(colend,colstart-1,-1):
                ans.append(matrix[rowend][i])
                c+=1
            rowend-=1
            if c==total:
                break

            #startcolumn leftside ,colstart=rowend to row start-1
            for i in range(rowend,rowstart-1,-1):
                ans.append(matrix[i][colstart])
                c+=1
            colstart+=1
            
        return ans                



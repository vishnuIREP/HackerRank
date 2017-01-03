def absolute_permute(holder,k,visit):
   if k == 0:
       return holder
   length=len(holder)
   if length%2 != 0:
       return -1
   else:
       i=0
       while i < length:
         if(visit[i] == False):
           if(i+k<length):
               temp=holder[i]
               holder[i]=holder[i+k]
               holder[i+k]=temp
               visit[i]=True
               visit[i+k]=True
           else:
               return -1
         i = i+1
   return holder


if __name__ == "__main__":
    iter = raw_input()
    for i in range(0,int(iter)):
        n,k = raw_input().split()
        holder=[]
        visit =[]
        for i in range(0,int(n)):
            holder.append(i+1)
            visit.append(False)
        result = absolute_permute(holder,int(k),visit)
        print str(result).replace(",","").replace("[","").replace("]","")
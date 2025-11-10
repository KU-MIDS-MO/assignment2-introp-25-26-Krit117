def swap_ends(L, k):
   if k <= 0 or len(L)== 0 or k > len(L) // 2:
       return (L.copy(),0 )
   L2= L.copy()
   L2[:k], L2[-k:] = L2[-k:], L2[:k]
   return (L2, k)

   
   
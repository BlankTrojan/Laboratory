def rvrs(s):
   if len(s)==0:
       return ' '
   else:
       return rvrs(s[1:])+s[0]
s="12345"
print(rvrs(s))

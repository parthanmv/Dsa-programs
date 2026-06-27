s="A man, a plan, a canal: Panama"
s=s.lower()
l=0
r=len(s)-1
def alphnum(s):
    return (ord('A') <= ord(s) <=ord('Z')or
           ord('a') <= ord(s) <=ord('a') or
           ord('a') <= ord(s) <=ord('z'))
while l < r:    
  while l<r and not alphnum(s[l]):
    l+=1
  while r > l and not alphnum(s[r]):
    r-=1
  if s[l]!=s[r]:
      print("false")
  l,r=l+1,r-1    
print("true")
function palindrome(s)
{
   let left=0
   let right=s.lenghth
   while(s[left]<s[right])
   {
    if(s[left] !== s[right])
    {
        return false
    }
    left+=1
    right-=1
   }
}
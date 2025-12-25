class Solution:
    def defangIPaddr(self, address: str) -> str:
        #return address.replace(".","[.]") or
        ans=""
        for i in address:
            if i!=".":
                ans+=i
            else:
                ans+="[.]"
        return ans

        
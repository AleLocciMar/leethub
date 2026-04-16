class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = ""
        p = 0
        q = len(nums)-1
        turne = False
        while(not turne):
           turne = True
           while(p < len(nums) and nums[p] != ""):
               p+=1
           while(q >= 0 and nums[q] == ""):
               q-=1
           if p >= q:
               turne = True
           elif nums[p] == "" and nums[q] != "":
                nums[p] = nums[q]
                nums[q] = ""
                turne = False
          # else:
          #     p = 0
          #     q = len(nums)-1
          #elif nums[p] == val:
        i = 0
        j = 0
        aux = []

        for i in range(len(nums)):
            if not nums[i] == "":
                aux.append(nums[i])
            else:
                break
        return len(aux)
        
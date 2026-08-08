class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = -1
        clean = "".join(char for char in s.lower() if char.isalnum())
        for i in range(len(clean)//2):
            if clean[front] != clean[back]:
                print(clean[front], clean[back])
                return False
            front +=1
            back -= 1
        return True
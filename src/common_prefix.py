class CommonPrefix:
    """
    Solution for https://leetcode.com/problems/longest-common-prefix/
    """

    def find_prefix(self, my_list):
        """Determine longest common prefix in given array."""
        #handle empty lists
        if len(my_list)== 0: 
            return ""
        
        #locate smallest string in array
        substring = min(my_list,key=len)

        #remove smallest string from array
        my_list.remove(substring)

        return self.compare(my_list, substring)

    
    def compare(self, my_list, substring):
        """Recursively compare substring to elements of array."""
        #base case for recursion
        if substring == "": return ""

        counter = 0
        for string in my_list:
            if substring == string[:len(substring)]:
                counter+=1
        
        if counter == len(my_list):
            return substring
        else:
            return self.compare(my_list, substring[:-1])
    
        

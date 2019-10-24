class CommonPrefix:
    """
    Solution for https://leetcode.com/problems/longest-common-prefix/
    """

    def solution1(self, my_list):
        """Basic solution using iteration."""   
        #handle empty lists
        if len(my_list) == 0: return ""
        
        #set prefix to first string in list, remove
        prefix = my_list[0]
        my_list.remove(prefix)

        for my_string in my_list:
            while my_string.find(prefix[:len(prefix)]): 
                prefix = prefix[:-1]
                if prefix == "": return ""   
        
        return prefix


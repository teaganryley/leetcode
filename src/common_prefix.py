from .helpers import trie_node

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

    def solution2(self, my_list):
        """
        Maps list of words to prefix tree (trie) structure, then traverses structure to find longest
        common prefix. 
        """
        
        # instantiate root of trie
        root = trie_node.TrieNode("root")

        for word in my_list:
            trie_node.insert(root, word)
        
        return trie_node.find_lcp(root, len(my_list))


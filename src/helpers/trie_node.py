class TrieNode():
    """
    Simple prefix tree (trie) implementation.
    """
    
    def __init__(self, value: str):
        self.value = value
        self.children = []
        #gives multiplicity of current character
        self.counter = 1


def insert(root, word: str):
    """
    Maps word to trie structure.
    """
    
    current = root
    
    for char in word:
        
        found_in_child = False
        
        for child in current.children:
            if child.value == char:
                child.counter += 1
                current = child
                found_in_child = True
                break
        
        if not found_in_child:
            new_node = TrieNode(char)
            current.children.append(new_node)
            current = new_node


def find_lcp(root, list_length: int):
    """
    Locates the longest common prefix in a trie.
    """
    
    lcp = ""
    current = root
    common_char_exists = True 

    while common_char_exists:    
        common_char_exists = False
        for child in current.children:
            if child.counter == list_length:
                lcp += child.value
                current = child
                common_char_exists = True
                break
    return lcp

    
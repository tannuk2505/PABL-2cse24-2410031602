from collections import defaultdict

def groupAnagrams(strs):
    # Use defaultdict so we don't have to check if a key exists
    anagram_map = defaultdict(list)
    
    for s in strs:
        # Sort the string to create a uniform key
        # sorted("eat") -> ['a', 'e', 't']
        # "".join(['a', 'e', 't']) -> "aet"
        sorted_key = "".join(sorted(s))
        
        # Append the original string to the list for this key
        anagram_map[sorted_key].append(s)
        
    # Return only the grouped lists
    return list(anagram_map.values())

# Example:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
class Tree:
    def __init__(self, char, freq):
        self.data = (char, freq)
        self.left = None
        self.right = None

    def __str__(self):
        return "[" + str(self.data) + ",[" + str(self.left) + "," + str(self.right) + "]" + "]"


def merge_trees(tree1,tree2): # tree1 , tree2 list of trees
    tree3 = []
    p1 = 0
    p2 = 0
    looping = 1
    while looping == 1:
        if (p1 < len(tree1) and p2 < len(tree2)):
            if (tree1[p1].data[1] > tree2[p2].data[1]):
                tree3.append(tree2[p2])
                p2 += 1
            else:
                tree3.append(tree1[p1])
                p1 += 1
        if p1 < len(tree1) and p2 >= len(tree2):
            tree3.append(tree1[p1])
            p1+=1
        if p1 >= len(tree1) and p2 < len(tree2):
            tree3.append(tree2[p2])
            p2+=1
        if p1 >= len(tree1) and p2 >= len(tree2):
            looping = 0
    return tree3 # return list of trees
def sort(tree):
    # merge sort
    if len(tree) <= 1:
        return tree
    index_mid = int(len(tree) // 2)
    left1 = tree[0: index_mid]
    l1 = sort(left1)
    right1 = tree[index_mid: len(tree)]
    l2 = sort(right1)
    return merge_trees(l1, l2)
l = ['C', 'A', 'S', 'A', 'B', 'L', 'N', 'C', 'A']
def format_tree(l):
    dict1 = {}
    tree = [] # list of trees
    for i in range(len(l)):
        if l[i] in dict1:
            dict1[l[i]] += 1
        else :
            dict1[l[i]]=1
    for i in dict1.keys():
        node = Tree(i, dict1[i])
        tree.append(node)
    return tree



def add_nodes(l):
    tree = format_tree(l)
    sorted_tree = sort(tree)
    tree_final = []
    for node in sorted_tree:

        tree_final.append(node)
    return tree_final


def huffmanTree(L):
    sorted_tree= add_nodes(L)
    if (len(sorted_tree)<2):
        return sorted_tree
    while (len(sorted_tree)>1):
        new_node = Tree(None,sorted_tree[0].data[1]+sorted_tree[1].data[1])
        temp= sorted_tree[0]
        temp2=sorted_tree[1]
        sorted_tree[0]= new_node
        sorted_tree[0].left=temp
        sorted_tree[0].right=temp2
        sorted_tree.remove(sorted_tree[ 1])


        index=0
        for j in range(1,len(sorted_tree)):
            if (sorted_tree[j].data[1]<sorted_tree[index].data[1]):

                sorted_tree[index],sorted_tree[j]=sorted_tree[j],sorted_tree[index]
                index = j


    return sorted_tree

T = huffmanTree(l)
for node in T :
    print(node)




# q3
def dict_huffman(T,code,dict):
    if T[0].data[0] != None :
        dict[T[0].data[0]] = code or '0'
        return dict

    subtree_left= T[0].left
    subtree_right = T[0].right
    if subtree_left.data[0] is  None:

        dict_huffman([subtree_left],code+'0',dict)
    else :
        dict[subtree_left.data[0]]= code+'0'

    if subtree_right.data[0] is  None:

        dict_huffman([subtree_right],code+'1',dict)
    else:
        ## n'essaie pas d'ajouter dans string car strings sont immutable and ca cree une nouvelle string
        dict[subtree_right.data[0]] = code + '1'

    return dict


dict1=dict_huffman(T,'',{})
for i in dict1 :
    print(i,"====",dict1[i])

def compress(S,dict):
    result = ""
    for i in S:
        result+=dict[i]
    return result
print(compress("CACA",dict1))
def generate_prefix(s):
    result =[]
    for i in range(1,len(s)+1):
        result.append(s[:i])
    return result
print(generate_prefix("aaabsddkkdzudzikz"))

def decompress(dict, string):
    result = ""
    reverse_dict = {v: k for k, v in dict.items()}

    var = 0
    while var < len(string):
        matched = False
        for i in generate_prefix(string[var:]):

            if i in reverse_dict:
                result += reverse_dict[i]
                var += len(i)
                matched = True
                break
        if not matched:
            raise ValueError(f"No matching prefix found at position {var}")
    return result

## EXAMPLE :


text = "Huffman coding is a popular algorithm used for lossless data compression. It was developed by David A. Huffman while he was a Ph.D. student at MIT and was published in 1952. The primary goal of Huffman coding is to compress data efficiently by assigning shorter codes to more frequent symbols or characters and longer codes to less frequent ones"
list_of_characters= []
for i in text :
    list_of_characters.append(i)
tree = huffmanTree(list_of_characters)
dict2 = dict_huffman(tree,"",{})
print(dict2)
compress_result = compress(text,dict2)
print(compress_result)
print(decompress(dict2,compress_result))

import math


def toBinary(a):
    binary_str = ""
    for i in a:
        binary_char = bin(ord(i))[2:]

        binary_char = "0" * (7 - len(binary_char)) + binary_char
        binary_str += binary_char
    return binary_str


print(toBinary("Huffman coding is a popular algorithm used for lossless data compression. It was developed by David A. Huffman while he was a Ph.D. student at MIT and was published in 1952. The primary goal of Huffman coding is to compress data efficiently by assigning shorter codes to more frequent symbols or characters and longer codes to less frequent ones"))
print("size of ascii code is too long than hauffman code")

import string
import random
all_characters = string.ascii_lowercase
list1 = [[] for _ in range(100)]
print(len(list1))
for i in list1:
    for j in range(100):
        i.append(random.choice(all_characters))

L1 = [] # storing huffman codes of nested lists of list1

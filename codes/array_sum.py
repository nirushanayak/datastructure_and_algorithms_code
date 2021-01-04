
from collections import defaultdict 
import copy

def fourNumberSum(array, targetSum):
    result = []
    hashMap = defaultdict(list)
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            
'''
Created on 2017-9-3
@author: NiroLN
'''

class leet001_sum2(object):
    '''
    classdocs
    '''
#     def __init__(self, params):
#         '''
#         Constructor
#         '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """    
        dic = {}
    
        for i , num in enumerate(nums):
            if target - num in dic:
                return (i, dic[target- num])
            else:
                dic[num] = i
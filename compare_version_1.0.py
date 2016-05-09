'''
Leetcode #165

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

'''
# Count execution time
import timeit

# class from leetcode
class Solution(object):
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2): 
    	splitem = zip(version1.split('.'), version2.split('.'))
    	for x, y in splitem:
    		if int(x) > int(y):
    			return 1
    		elif int(x) < int(y):
    			return -1
    	return 0

# Create a instance that can access compareVersion function
compare = Solution()

# Ask user to enter version numbers
v1 = raw_input("Please enter first version number:")
v2 = raw_input("Please enter second version number:")

start_time = timeit.default_timer()
# Show the result
print 'Here is the comparision result:', compare.compareVersion(v1 , v2)

elapsed = timeit.default_timer() - start_time
print elapsed
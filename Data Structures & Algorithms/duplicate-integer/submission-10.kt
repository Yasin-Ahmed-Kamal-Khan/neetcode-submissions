class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {
        val numSet = mutableSetOf<Int>()
        nums.forEach { num ->
            if (num in numSet) {
                return true
            }
            numSet.add(num)
        }
        return false
    }
}

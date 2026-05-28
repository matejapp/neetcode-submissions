public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        Dictionary<int, int> nums = new Dictionary<int, int>();

        for (int i = 0; i < numbers.Length; i++) {
            int needed = target - numbers[i];

            if (nums.ContainsKey(needed)) {
                return new int[] { nums[needed]+
                1, i+1 };
            }

            nums[numbers[i]] = i;
        }

        return new int[] { };
    }
}
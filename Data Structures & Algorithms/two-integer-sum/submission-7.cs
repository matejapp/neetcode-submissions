public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> num_dict = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++) {

            int needed = target - nums[i];

            if (num_dict.ContainsKey(needed)) {
                return new int[] { num_dict[needed], i };
            }

            num_dict[nums[i]] = i;
        }

        return new int[] {};
    }
}

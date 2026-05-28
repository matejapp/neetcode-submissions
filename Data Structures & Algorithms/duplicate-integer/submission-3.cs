public class Solution {
    public bool hasDuplicate(int[] nums) {
        var no_duplicates = new HashSet<int>();
        foreach(int n in nums){
            no_duplicates.Add(n);
        };

        return no_duplicates.Count() != nums.Length;
    }
}
public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var res = new List<int>();
        var dict = new Dictionary<int,int>();


        for(int i = 0; i < nums.Length; i++){
            dict[i] = nums[i];
        }

        int index = 0;
        foreach(int n in nums){
            var prod = dict.Where(kvp => kvp.Key != index)
            .Select(kvp => kvp.Value)
            .Aggregate(1,(p,kvp) => p*=kvp);
            res.Add(prod);
            index++;
        }

        return res.ToArray();
    }
}

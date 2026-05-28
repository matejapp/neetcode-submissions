public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        
        var dict = new Dictionary<int,int>();
        foreach(int n in nums){
            if(dict.ContainsKey(n)){
                dict[n]++;
            }else{
                dict[n] = 1;
            }
        }

        var res = new List<int>();
        for(int i = 0;i<k;i++){
            var max = dict.Aggregate((l,r) => l.Value > r.Value ? l:r).Key;
            dict.Remove(max);
            res.Add(max);
        }

        return res.ToArray();
}}

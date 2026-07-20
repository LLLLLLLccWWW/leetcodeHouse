public class Solution {
    public IList<IList<int>> LargeGroupPositions(string s) {
        var result = new List<IList<int>>();
        int start = 0;
        int n = s.Length;

        for(int i = 0;i < n ; i++){
            if (i == n-1 || s[i] != s[i+1]){
                int length = i - start + 1;

                if(length >= 3){
                    result.Add(new List<int> {start,i});
                }

                start = i + 1;

            }
        }
        return result;
    }
}

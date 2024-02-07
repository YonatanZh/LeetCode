class Solution {
    public int removeElement(int[] nums, int val) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] == val) {
                
                int j = findNextNoneVal(nums, val, i , n);
                if (j != -1) {
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }
        for (int i = n-1; i > -1; i--) { 
            if (nums[i] != val) {return i+1;}
        }
        return 0;
    }
    private int findNextNoneVal (int [] nums, int val, int start, int finish) {
        for (int i = start; i < finish; i ++) {
            if (nums[i] != val){
                return i;
            }
        }
        return -1;
    }
}

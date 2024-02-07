class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 1;
        int curr = nums[0];
        boolean flag = false;
        for (int i = 1; i < nums.length; i++) {
            if (!flag && curr == nums[i]) {
                nums[index] = nums[i];
                index++;
                flag = true;
            } else if (flag && nums[i] != curr) {
                curr = nums[i];
                nums[index] = nums[i];
                index++;
                flag = false;
            } else if (!flag && nums[i] != curr) {
                curr = nums[i];
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }

}
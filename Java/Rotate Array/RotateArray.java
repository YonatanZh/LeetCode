class Solution {
    public static void rotate(int[] nums, int k) {
        int len = nums.length;
        // k = k % len;

        reverseArray(nums, 0, len - k % len);
        reverseArray(nums, len - k % len, len);
        reverseArray(nums, 0, len);
    }

    private static void reverseArray(int[] nums, int start, int end)
    {
        for (int i = start; i < (start + end) / 2; i++) {
            int temp = nums[i];
            nums[i] = nums[start + end - i - 1];
            nums[start + end - i - 1] = temp;
        }
    }
}
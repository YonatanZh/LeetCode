class Solution {
    public int candy(int[] ratings) {
        int [] candy = new int[ratings.length];

        Arrays.fill(candy, 1);

        for (int i = 1; i < ratings.length; i++) {
            if (ratings[i-1] < ratings[i]) {
                candy[i] = candy[i-1] + 1;
            }
        }
        for (int i = ratings.length - 2; i >= 0; i--) {
            if (ratings[i+1] < ratings[i]) {
                candy[i] = Math.max(candy[i], candy[i+1] + 1);
            }
        }

        int sum = 0;

        for (int j : candy) {
            sum = sum + j;
        }

        return sum;
    }
}
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap<Integer, Integer>();
        for(int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>( (a, b) -> 
            -Integer.compare(freq.get(a), freq.get(b)));

        for(int num : freq.keySet()) {
            maxHeap.add(num);
        }

        int [] kItems = new int[k];
        for(int i = 0; i < k; i++) {
            kItems[i] = maxHeap.poll();
        }
        return kItems;
    }
}

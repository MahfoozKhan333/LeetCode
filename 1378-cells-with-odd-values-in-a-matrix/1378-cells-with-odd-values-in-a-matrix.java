class Solution {
    public int oddCells(int a, int b, int[][] indices) {
        int[] rows = new int[a];
        int[] cols = new int[b];
        for (int[] index : indices) {
            rows[index[0]]++;
            cols[index[1]]++;
        }
        int count = 0;
        for (int i=0; i<a; i++) {
            for (int j=0; j<b; j++) {
                if ((rows[i] + cols[j]) % 2 != 0) {
                    count++;
                }
            }
        } 
        return count;
    }
}

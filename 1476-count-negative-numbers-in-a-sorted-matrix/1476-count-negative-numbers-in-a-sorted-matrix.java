public class Solution {
    public int countNegatives(int[][] grid) {
        int a = grid.length;
        int b = grid[0].length;
        int row = 0, col = b - 1;
        int count = 0;

        while (row < a && col >= 0) {
            if (grid[row][col] < 0) {
                count += a - row;
                col--;
            } else {
                row++;
            }
        }

        return count;
    }
}
// brute force approach
// public class Solution {
//     public int countNegatives(int[][] grid) {
//         int count = 0;
//         for (int[] row : grid) {
//             for (int num : row) {
//                 if (num < 0) count++;
//             }
//         }
//         return count;
//     }
// }

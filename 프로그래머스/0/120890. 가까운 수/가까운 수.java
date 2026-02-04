import java.util.Arrays;

class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int min = Math.abs(array[0] - n);

        for (int x : array) {
            int temp = Math.abs(x - n);

            if (temp < min) {
                min = temp;
            }
        }

        Arrays.sort(array);
        for (int x : array) {
            if (Math.abs(x - n) == min) {
                answer = x;
                break;
            } else if( Math.abs(n-x) == min) {
                answer = x;
                break;
            }
        }
        return answer;
    }
}
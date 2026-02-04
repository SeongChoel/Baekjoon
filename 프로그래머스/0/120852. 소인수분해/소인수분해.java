import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(int n) {
        List<Integer> list = new ArrayList<>();

        for (int i = 2; i <= n+1; i++) {
            while (n % i == 0) {
                if (!list.contains(i)) {
                    list.add(i);
                }
                n = n / i;
            }
        }
        int[] answer = new int[list.size()];
        int index = 0;
        for (int x : list) {
            answer[index++] = x;
        }
        return answer;
    }
}
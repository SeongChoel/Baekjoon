import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        List<Integer> result = new ArrayList<>();
        for (int[] q : queries) {
            List<Integer> list = new ArrayList<>();
            int s = q[0];
            int e = q[1];
            int k = q[2];

            for (int i = s; i <= e; i++) {
                if (arr[i] > k) {
                    list.add(arr[i]);
                }
            }
            Collections.sort(list);

            if (list.isEmpty()) {
                result.add(-1);
            } else {
                result.add(list.get(0));
            }

        }
        return result.stream()
                .mapToInt(x -> x)
                .toArray();
    }
}

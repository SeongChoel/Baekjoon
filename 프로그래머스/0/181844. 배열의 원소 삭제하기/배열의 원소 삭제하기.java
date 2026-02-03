import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> list = new ArrayList<>();

        for(int x: arr) {
            int flag = 0;
            for(int y: delete_list) {
                if (x==y) {
                    flag++;
                }
            }
            if (flag==0) {
                list.add(x);
            }
        }
        int[] answer = new int[list.size()];

        int i=0;
        for (int x : list) {
            answer[i] = x;
            i++;
        }
        return answer;
    }
}

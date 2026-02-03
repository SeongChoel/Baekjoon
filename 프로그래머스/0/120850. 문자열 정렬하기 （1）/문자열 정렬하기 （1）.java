import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(String my_string) {
        List<Integer> list = new ArrayList<>();

        for (char x : my_string.toCharArray()) {
            if (x>='a'&& x<='z') {
                continue;
            } else {
                list.add(x-'0');
            }
        }

        int[] answer = new int[list.size()];
        int i = 0;
        for (int x : list) {
            answer[i] = x;
            i++;
        }

        Arrays.sort(answer);



        return answer;
    }
}
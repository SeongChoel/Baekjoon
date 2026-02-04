import java.util.Arrays;

class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];
        int[] temp = new int[emergency.length];

        int index = 0;
        for(int x: emergency) {
            temp[index++] = x;
        }

        Arrays.sort(temp);
        int rank = 1;
        for(int i=temp.length-1; i>=0; i--) {
            for(int j=0; j<emergency.length; j++) {
                if(temp[i] == emergency[j]) {
                    answer[j] = rank++;
                }
            }
        }
        return answer;
    }
}
import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        String result = my_string.toLowerCase();
        char[] arr = new char[my_string.length()];
        int i =0;

        for(char x: result.toCharArray()) {
            arr[i] = x;
            i++;
        }

        Arrays.sort(arr);
        String answer = "";
        for(char x: arr) {
            answer += x;
        }

        return answer;
    }
}

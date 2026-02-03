class Solution {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";

        char[] arr = new char[my_string.length()];

        int i= 0;
        for(char x : my_string.toCharArray()) {
            arr[i] = x;
            i++;
        }

        char temp = arr[num1];
        arr[num1] = arr[num2];
        arr[num2] = temp;

        for (char x: arr) {
            answer +=x;
        }
        return answer;
    }
}
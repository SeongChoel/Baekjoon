class Solution {
    public String solution(String my_string) {
        String answer = "";

        for (char x : my_string.toCharArray()) {
            if(answer.indexOf(x)==-1) {
                answer+=x;
            }
        }

        return answer;
    }
}
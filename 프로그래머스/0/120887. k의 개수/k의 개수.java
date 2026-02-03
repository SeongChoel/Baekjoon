class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        String target = String.valueOf(k);


        for (int x = i; x <= j; x++) {
            String s = String.valueOf(x);

            for (int idx = 0; idx < s.length(); idx++) {
                if (s.charAt(idx) == target.charAt(0)) {
                    answer++;
                }
            }
        }
        return answer;
    }
}
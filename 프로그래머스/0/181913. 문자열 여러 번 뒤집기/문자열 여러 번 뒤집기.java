class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuilder sb = new StringBuilder(my_string);


        for (int q[] : queries) {
            int s = q[0];
            int e = q[1];

            while (s < e) {
                char temp = sb.charAt(s);
                sb.setCharAt(s,sb.charAt(e));
                sb.setCharAt(e,temp);
                s++;
                e--;
            }

        }

        return sb.toString();
    }
}
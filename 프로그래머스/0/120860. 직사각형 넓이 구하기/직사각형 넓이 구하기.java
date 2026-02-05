class Solution {
    public int solution(int[][] dots) {
        int answer = 0;

        int min_x = 256;
        int max_x = -256;

        int min_y = 256;
        int max_y = -256;

        for (int[] d : dots) {

            int dx = d[0];
            int dy = d[1];

            min_x =Math.min(dx,min_x);
            max_x =Math.max(dx,max_x);

            min_y = Math.min(dy,min_y);
            max_y = Math.max(dy,max_y);

        }
        answer = (max_x-min_x) * (max_y-min_y);


        return answer;
    }
}

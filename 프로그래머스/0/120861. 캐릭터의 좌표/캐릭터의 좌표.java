class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = new int[board.length];

        int min_x = board[0] / 2;
        int min_y = board[1] / 2;

        for (String input : keyinput) {
            if (input.equals("left") && answer[0] > -min_x)
                answer[0] -= 1;
            else if (input.equals("right") && (answer[0]) < min_x)
                answer[0] += 1;
            else if (input.equals("up") && (answer[1]) < min_y)
                answer[1] += 1;
            else if (input.equals("down") && (answer[1]) > -min_y)
                answer[1] -= 1;
        }

        return answer;
    }
}

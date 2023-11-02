package BaekJoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Java_1010 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            String[] stringArray = br.readLine().split(" ");
            int N = Integer.parseInt(stringArray[0]);
            int M = Integer.parseInt(stringArray[1]);
            int result = solution(N, M);
            System.out.println(result);
        }
    }

    private static int solution(int N, int M) {
        int result = 1;
        for(int i = M; i > N; i--) {
            result *= i;
            result /= (M-i+1);
        }
        return result;
    }
    
}
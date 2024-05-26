import java.util.*;
import java.io.*;

public class Main {
    
    private static int X;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        X = Integer.parseInt(br.readLine());
        
        int answer = 0;
        int N = 64;
        
        while(0 < X) {
            if(N <= X) {
                answer++;
                X -= N;
            }
            N /= 2;
        }
        
        System.out.println(answer);
    }
    
}

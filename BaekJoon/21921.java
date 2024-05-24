import java.io.*;
import java.util.*;

public class Main {
	
	private static int N, X, answer, target, count;
	private static int[] visitors;
	
    public static void main(String[] args) throws IOException {
    	
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        
        target = 0;
        
        st = new StringTokenizer(br.readLine());
        
        visitors = new int[N];
        for(int n = 0; n < N; n++) {
        	int visitor = Integer.parseInt(st.nextToken());
        	visitors[n] = visitor;
        	
        	if(n < X) target+= visitor;
        	
        }
        
        answer = target;
        count = 1;
        
        for(int n = X; n < N; n++) {
        	target = target - visitors[n-X] + visitors[n];
        	
        	if(answer < target ) {
        		answer = target;
        		count = 1;
        	}
        	else if(answer == target) {
        		count++;
        	}
        }
    	
        if(answer == 0) {
        	System.out.println("SAD");
        }
        
        else {
        	System.out.println(answer);
            System.out.println(count);
        }
        
    }

}

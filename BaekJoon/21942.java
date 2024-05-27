import java.io.*;
import java.util.*;

public class Main {

    private static int N, M;

    private static Road[] roads;

    private static int[] parent;

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        parent = new int[N+1];
        roads = new Road[M];

        for(int n=0; n < N+1; n++) {
            parent[n] = n;
        }

        int a, b, c;
        long cost = 0L;

        for(int m = 0; m < M; m++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            roads[m] = new Road(a, b, c);
            cost += c;
        }

        // ================================================

        Arrays.sort(roads);

        for(Road road : roads) {
            if(find(road.a) == find(road.b)) continue;
            cost -= road.c;
            union(road.a, road.b);
        }

        for(int n = 1; n < N+1; n++) {
            if(find(n) == 1) continue;
            System.out.println(-1);
            return;
        }

        System.out.println(cost);

    }

    private static int find(int x) {
        if(x != parent[x]) parent[x] = find(parent[x]);
        return parent[x];
    }

    private static void union(int x, int y) {
        x = find(x);
        y = find(y);
        parent[Math.max(x, y)] = Math.min(x, y);
    }

    static class Road implements Comparable<Road> {
        int a, b, c;
        public Road(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }
        @Override
        public int compareTo(Road other) {
            return this.c - other.c;
        }

        @Override
        public String toString() {
            return "a : " + a + ", b: " + b + ", c: " + c + " ";
        }
    }

}

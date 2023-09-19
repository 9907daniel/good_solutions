import java.util.*;
import java.io.*;

public class Solution{
    // 정적 변수를 여기다가 설정해준다
    static int[] limit;
    static boolean[][] visited;
    static Set<Integer> answer;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st= new StringTokenizer(br.readLine());

        limit = new int[3];
        visited = new boolean[201][201];

        for(int i=0; i<3; i++){
            limit[i] = Integer.parseInt(st.nextToken());
        }

        answer = new TreeSet<>();
		dfs(0,0,limit[2]);
    }

    static void dfs(int x, int y, int z){
        if(visited[x][z]) return;

        if (a==0){
            answer.add(c);
        }
    }
}
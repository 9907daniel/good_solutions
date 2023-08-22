class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int number3 = numer1*denom2+numer2*denom1;
        int denom3 = denom1*denom2;
        
        int current_max = 1;
        for(int a=1;a<=denom3;a++){
            if (denom3%a == 0 && number3%a == 0){
                current_max = a;
            }
        }
        
        int[] answer = {(number3/current_max), (denom3/current_max)};
    
        return answer;    
    }
}
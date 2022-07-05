public class arrays{

    static int sum (int x,int y){
        int z = x+y;
        return z;
        }


    public static void main(String[] args){
        int c=sum(98,45);
        System.out.println(c);
        System.out.println(sum(10,90,87,35));
        }



    static int sum(int ...arr){
        int result =0;
        for(int z:arr){
            result=result+z;
        }
        return result;

    }
 
}
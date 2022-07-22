import java.util.Scanner;


public class conditionals {
  
  public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    // ------------------------leap year--------------------------------------
    
    
    System.out.println("enter year");
    int yr=sc.nextInt();

    if(yr%4==0){
      if(yr%100==0){
        if(yr%400==0){
          System.out.println("leap year");
        }
        else{
          System.out.println("not leap year");
        }
      }
      else{
        System.out.println("leap year");
      }
    }
    else{
      System.out.println("not a leap year");
    }


    // System.out.println("enter website name");
    // String name=sc.nextLine();
    // int c=name.indexOf(".");
    // System.out.println(c);
    // String domain=name.substring(c+1);
    // System.out.println(domain);
    // if (domain=="com"){
    //   System.out.println("commercial website");
    // }
    // else if (domain=="org"){
    //   System.out.println("organization website");
    // }
    // else{
    //   System.out.println("indian website");
    // }




    sc.close();
  }


  

  


}

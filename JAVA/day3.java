import java.util.Scanner;
public class day3 {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);


    //------------------------------Odd or Even------------------------------------------
    System.out.println("Which number do you want to check? ");
    int check_num = sc.nextInt();
    if (check_num % 2 == 0) {
      System.out.println("Even");    
    }
    else{
      System.out.println("odd");
    }
    // --------------------------------Leap Year--------------------------

    System.out.println("Which year you want to check");
    int year = sc.nextInt();
    if (year % 4 == 0) {
      if( year % 100 == 0){
        if( year % 400 == 0) {
          System.out.println("leap year");
        }
        else{
          System.out.println("not a leap");
        }
      }
      else{
        System.out.println("leap year");
      }
    } 
    else{
      System.out.println("not a leap year");
    }
    // ---------------------------------Pizza Order------------------------------------
    System.out.println("Welcome to Python Pizza Deliveries!");
    System.out.println("What size pizza do you want? S, M, or L ");
    String size = sc.nextLine();
    System.out.println("Do you want pepperoni? Y or N ");
    String add_pepperoni = sc.nextLine();
    System.out.println("Do you want extra cheese? Y or N ");
    String extra_cheese = sc.nextLine();
    int bill=0;
    if( size.equalsIgnoreCase("S")){
      bill=15;
      if( add_pepperoni.equalsIgnoreCase("Y")){
        bill+=2;
      }

    } 
    else if(size.equalsIgnoreCase("M")){
      bill=20;
      if( add_pepperoni.equalsIgnoreCase("Y")){
        bill+=3;
      }
      

    } 
    else{
      bill=25;
      if( add_pepperoni.equalsIgnoreCase("Y")){
        bill+=3;
      }    
    }
    if(extra_cheese.equalsIgnoreCase("Y")){
      bill+=1;
    }
    System.out.printf("Your final bill is: %d$",bill);
    




    sc.close();
  }

}
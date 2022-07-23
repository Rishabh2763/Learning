import java.util.Scanner;

public class day2 {
  public static void main(String[] args) {
    Scanner sc= new Scanner(System.in);




    System.out.println("Enter Your Name");
    String name=sc.next();
    System.out.println("Your name has "+ name.length() + " characters");



// ----------------------------F strings--------------------------------------------

    int score= 10;
    int large_num=100000;
    double height=1.8;
    boolean iswinning= true;

    System.out.printf("Your score is %d and height is %.2f and winning is %b",score,height,iswinning);
    System.out.println();
    System.out.printf("10 spaces before %10d",score);
    System.out.println();
    System.out.printf("10 spaces after %-10d (reference)",score);
    System.out.println();
    System.out.printf("number with commas %,d ",large_num);
    System.out.println();
    String sr = String.format("Your score is %d and height is %.2f and winning is %b",score,height,iswinning,score,height,iswinning);
    System.out.println(sr);

  // -----------------------------tip calculator/---------------------------------------

    System.out.println("Welcome to the tip calculator");
    System.out.println("what was the the total bill ");
    float bill = sc.nextFloat();
    System.out.println("what percentage tip would you like to give ");
    int tip = sc.nextInt();
    System.out.println("how many people to split the bill");
    int n =sc.nextInt();

    float total_pay= (bill + (bill * tip)/100);
    System.out.println(total_pay);
    float each_pay = (total_pay/n);
    System.out.printf("each person should pay %.2f$", each_pay);







  sc.close();


  }
}

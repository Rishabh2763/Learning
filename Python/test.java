import java.util.Scanner;
public class test {
  public static void main(String[] args) {
    
    Scanner sc = new Scanner(System.in);    
    String name1 = sc.nextLine();
    String name2 = sc.nextLine();
    String name3 = name1 + name2;
    System.out.println(name3);
    
    sc.close();
  }
  
}

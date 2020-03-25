

import java.util.Scanner;

public class NumOfChar {

 public static void main(String[] args) {
  int i=0,j=0;
  Scanner sc=new Scanner(System.in);
  String str=sc.nextLine();
  char ch=sc.next().charAt(0);
  for(i=0;i<str.length();i++)
  {
   if(Character.toLowerCase(str.charAt(i))==Character.toLowerCase(ch))
   {
    j++;
   }
  }
  System.out.println(j);
  
 }

}
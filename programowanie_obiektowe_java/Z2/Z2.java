import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Stack;

public class Z2 {
    public static <t> void wypiszCoDrugi(Iterable<t> argument) {
        int wajcha=0;
        int wajcha_jednorazowa=1;
        for(t element: argument){
            if(wajcha==0){
                if(wajcha_jednorazowa!=1) System.out.print(", ");
                else wajcha_jednorazowa=0;
                System.out.print(element);
                wajcha=1;
            }
            else {
                wajcha=0;
            }
        }
    }
    public static void main(String[] args) {
        ArrayList<Integer> lista_testowa=new  ArrayList<Integer>();
        lista_testowa.add(7);
        lista_testowa.add(7);
        lista_testowa.add(8);
        lista_testowa.add(3);
        lista_testowa.add(8);
        lista_testowa.add(5);
        wypiszCoDrugi(lista_testowa);
        System.out.print("\n");
        Stack<Integer> stack_testowa=new  Stack<Integer>();
        stack_testowa.add(7);
        stack_testowa.add(8);
        stack_testowa.add(3);
        stack_testowa.add(5);
        wypiszCoDrugi(stack_testowa);
        PriorityQueue<Integer> kolejka=new  PriorityQueue<Integer>();
        kolejka.add(7);
        kolejka.add(8);
        kolejka.add(3);
        kolejka.add(5);
        System.out.print("\n");
        wypiszCoDrugi(kolejka);

    }
}

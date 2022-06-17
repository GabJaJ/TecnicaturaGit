
package Ejerciocio6;

import java.util.Scanner;

public class Ejercicio6 {
    public static void main (String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite la cantidad de dinero de Guillermo: ");
        guillermo = Float.parseFloat(entrada.nextLine());
        
        luis= guillermo / 2;
        juan = (lius + guillermo)/ 2;
        total = luis + guillermo + juan;
        System.out.println("\nEl dinero de Luis es: U$D"+luis);
        System.out.println("\nEl dinero de Juan es: U$D"+juan);
        System.out.println("\nEl total de dinero entre todos es: U$D"+total);
    }
    
}

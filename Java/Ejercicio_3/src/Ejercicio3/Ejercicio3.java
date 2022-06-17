
package Ejercicio3;

import java.util.Scanner;


public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.printIn("Digite el alto del rectangulo: ");
        int alto = Integer.parseInt(entrada.nextLine());
        System.out.printIn("Digite el ancho del rectangulo: ");
        int ancho = Integer.parseInt(entrada.nextLine());
        int area = alto * ancho;
        int perimetro = (alto + ancho) *2;
        System.out.printIn("Area: "+ area);
        System.out.printIn("Perimetro: "+ perimetro);
    }
    
    
}

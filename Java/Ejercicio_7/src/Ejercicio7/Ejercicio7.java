
package Ejercicio7;

import java.util.Scanner;

public class Ejercicio7 {
    public static void main (String[] args) {
        Scanner entrada = new Scanner(System.in);
        final int salario = 1000;
        int comision = 150, venta;
        float salarioMensual, ventaCarro, porcVenta, totalPrecio;
        
        System.out.println("Digite la cantidad de carros vendidos: ");
        venta = Integer.parseInt(entrada,nextLine());
        System.out.println("Digite el presio de un carro: ");
        ventaCarro = Float.parseFloat(entrada,nextline());
        
        comision *= venta;
        totalPrecio = ventaCarro * venta;
        porVenta = totalPrecio * 0,05f;
        salarioMensual = salario + comision + porVenta;
        
        System.out.println("\nEl salario mensual es: "+salarioMensual);
    }
    
    
}


package com.mycompany.semana1clase2;

public class ejericio2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        double raiz = Math.sqrt(10);
        double potencia = Math.pow(10,2);
        
        System.out.println("El resultado de la raiz de 10 es :  " + raiz);
        System.out.println("La potencia es :  " + potencia);
     // Condicionales
     
     int num1 = 30;
     int num2 = 36;
     
     if (num1 >= num2) {
   
         if (num1 ==num2) {
             System.out.println("Los numeros son iguales");
         } else {
             System.out.println("El numero " + num1 + " es mayor que " + num2);
         
         }
     } else {
         System.out.println("El numero " + num1 + " es menor que " + num2);
     }
    }
    
}

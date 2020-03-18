#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <windows.h>
#include <time.h>


int main(){

float capital = 10000000;
int pproduccion = 5;
printf("\n\t\tCompra de inmuebles para ampliar la empresa\n\t\t");
    printf("\nA continuacion se presentan los inmuebles disponibles:\n");

char zona[4][15] = {"Norte","Sur","Oriente","Centro"};
int precio[4] = {1000000,2000000,1500000,3000000};
char transito [4][15] = {"Bajo","Medio","Medio","Alto"};
int gastos_mensuales[4] = {100000,150000,200000,300000};
int produccion[4] = {2,4,3,6};

    int i=1,op,inmuebles;
inmuebles1: {
    for( i=1 ; i<=4 ; i++){

        printf("\nInmueble %i\n",i);
        printf("Ubicacion: %s\n",zona[i-1]);
        printf("Precio del inmueble: %i\n",precio[i-1]);
        printf("El transito de personas por la zona es: %s\n",transito[i-1]);
        printf("Los gastos mensuales del inmuebles seran de: %i\n",gastos_mensuales[i-1]);
        printf("El aumento de produccion con la compra del nuevo inmueble es del %i porciento\n\n\n",produccion[i-1]);
    }
    printf("Desea comprar un nuevo inmueble?  1) Si  2)  No\n");
    scanf("%d",&op);
    system("cls");

        if(op==1){
            printf("Que inmueble desea comprar?\n");
            scanf("%d",&inmuebles);

            if(inmuebles == 1 || inmuebles == 2 || inmuebles == 3 || inmuebles == 4){
            printf("El capital que se descontara de los activos es: %i\n",precio[inmuebles-1]);
            printf("Los gastos mensuales seran de: %i\n",gastos_mensuales[inmuebles-1]);
            printf("El aumento de produccion con la compra del nuevo inmueble es del %i porciento",produccion[inmuebles-1]);

            capital = capital - precio[inmuebles-1] - gastos_mensuales[inmuebles-1];
            pproduccion = pproduccion + produccion[inmuebles-1];
            printf("\nEl capital final de la compra del inmueble menos los gastos del primer mes es de: %f\n",capital);
            printf("El porcentaje de produccion aumento a %i porciento\n",pproduccion);}

             printf("Desea comprar otro inmueble?");
            scanf("%d",&op);
            system("cls");
            goto inmuebles1;
            if (op == 1){
            goto inmuebles1;}
            }//Llave del if

}
} // Llave del caso

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <windows.h>
#include <time.h>


int main(){
int capital= 10000000;
int op,rporcentaje,acciones_p=100;
int rdinero,dinero_recibido,i=0;
int socios[10],dinerorec[10];


printf("\n\tEn esta seccion recibiras propuestas de diversos socios interesados en comprar acciones de tu empresa\n");
srand(time(NULL));
printf("\nDesea generar una propuesta de inversion?: 1) SI 2) NO\n");
scanf("%d",&op);
inversiones: {
if (op==1){
    printf("\nLa propuesta es la siguiente: \n");
    rdinero=1+rand()%(40-1);
    rporcentaje=1+rand()%(20);
    printf("Este socio desea invertir el %i por ciento del capital que tienes \n ",rdinero);
    printf("Por el %i porciento de tu empresa\n",rporcentaje);
    printf("Te interesa esta propuesta? 1) SI   2) NO\n");

    scanf("%d",&op);

    if(op==1){
        dinero_recibido = (capital*rdinero)/100;
        printf("La cantidad que recibiras por el socio es: %d\n",dinero_recibido);
        dinerorec[i] = dinero_recibido;
        capital = capital + dinero_recibido;
        printf("El capital final es: %i\n",capital);
        socios[i] = rporcentaje;
        printf("Las acciones del socio son: %i\n",socios[i]);
        printf("Las acciones quedan divididas asi: \n");
        acciones_p = acciones_p - socios[i];
        printf("Tus acciones son: %i\n",acciones_p);
        i++;
    }
    }

 printf("Desea generar otra propuesta?\n");
 scanf("%d",&op);
  system("cls");
 if(op == 1){
    goto inversiones;
 }

}
}

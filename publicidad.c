#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <windows.h>
#include <time.h>

int main(){
float dinero_in;
int op;
float aumento_pro,produccion=0;

printf("\t\tEn esta seccion podras invertir en publicidad para aumentar la produccion\n");
publicidadm: {
printf("\tQue desea hacer: \n\n");
printf("1. Invertir en publicidad\n");
printf("2. Modificar dinero invertido en publicidad\n");
scanf("%d",&op);

switch(op){

case 1:
printf("\t**Ingrese la cantidad de dinero que desee invertir para que se haga una cotizacion del aumento de produccion: ");
scanf("%f",&dinero_in);

aumento_pro = (dinero_in)/50000;

printf("Con la cantidad de dinero que quiere invertir, el aumento de produccion es de: %f\n\n",aumento_pro);
printf("Desea invertir esa cantidad ? presione 1 \n Desea modificar la cantidad ? presione 2\n");
scanf("%d",&op);

if (op == 2){
    printf("Ingrese la nueva cantidad que desea invertir:\n ");
    scanf("%f",&dinero_in);
    aumento_pro = (dinero_in)/50000;
    printf("Con la cantidad de dinero que quiere invertir, el aumento de produccion es de: %f\n\n",aumento_pro);
    printf("Desea invertir esa cantidad ? presione 1 \n");
    scanf("%d",&op);
    if (op != 1){
            dinero_in = 0;
            system("cls");
            goto publicidadm;
    }
}
if (op==1){
   produccion = produccion + aumento_pro;
   printf("La produccion aumentara %f\n",aumento_pro);
   printf("El total de produccion es: %f\n",produccion);

   printf("Desea realizar otra opcion? : \n");
scanf("%d",&op);}

if (op == 1){
    system("cls");
    goto publicidadm;
}


return aumento_pro,produccion;
break;

case 2:

printf("En esta seccion se puede modificar las cantidades invertidas en publicidad\n");
if (dinero_in <= 0  ){
    printf("Primero tienes que invertir dinero\n");
}else if(dinero_in > 0 ){
printf("Cantidad invertida en publicidad %f\n",dinero_in);
printf("Aumento de produccion %d\n",aumento_pro);
printf("Desea modificar la cantidad invertida en publicidad?\n");
scanf("%d",&op);}

 printf("Desea realizar otra opcion? :\n ");
scanf("%d",&op);

if (op == 1){
    goto publicidadm;
    system("cls");
}
return aumento_pro,produccion;
break;




default:
printf("opcion invalida\n");
system("cls");
goto publicidadm;

break;
}

}



}

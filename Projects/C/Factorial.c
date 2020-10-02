
#include <stdio.h>
int main()
{
   int i, f=1, num;
 
   printf("\nPlease enter a number: ");
   scanf("%d",&num);
   for(i=1;i<=num;i++){
      f=f*i;
    }
   printf("\n");
   printf("The result of factorial (%d!) is %d\n", num, f);
   return 0;
}

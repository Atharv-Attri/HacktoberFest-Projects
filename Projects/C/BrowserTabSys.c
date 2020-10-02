#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX1 100
#define MAX2 100
typedef struct 
{
  char site[MAX1][MAX2];
  char history[MAX1][MAX2];
  char bookmark[MAX1][MAX2];
  int top;
  int top1;
  int top2;
}stack;

void push(stack *s, int ch)
{  char ele[MAX1];
  printf("Enter search text :\n");
  scanf("%s",ele);
  s->top++;
  //Had s->top1++ here, that created void space
  strcpy(s->site[s->top],ele);
  if(ch!=2)
  {      s->top1++;
         strcpy(s->history[s->top1],ele);
     }
}
void pop(stack *s)
{   char ele[MAX1];
  //char *ele =(char* )malloc(100*sizeof(char));
  //ele = s->site[s->top];
  if(s->top==-1)
  {
    printf("\nNo Recent Tabs!!!Add one. \n");
  }
  else
    {
      strcpy(ele,s->site[s->top]);
      printf("\n - %s\n",ele);
      s->top--;
    }
}
void display(stack *s)
{  
  int i;
  if(s->top==-1)
  {printf("No Recent Tabs!!! \n");
  return;}
  {for(i=s->top;i>=0;i--)
  printf("%s\n",s->site[i]);}
}

void past(stack *s)
{  
  int i;
  if(s->top1==-1)
  {printf("No history!!! \n");
  return;}
  {
    for(i=s->top1;i>=0;i--) 
         {  
            printf("%s\n",s->history[i]);
         
         }
   }
}

 void bookmark(stack *s)  
 { int n, i;
   char ele[MAX1];
   past(s);
   if(s->top1!=-1)
     {
   printf("\nBottom to top i.e.\n n \n . \n . \n . \n 1 \n 0");
   printf("\nSelect a tab to bookmark:\n");
   scanf("%d", &n );
   if(n>=0 && n<=s->top1)
  {
     s->top2++;
   strcpy(s->bookmark[s->top2], s->history[n]);
   }
   else
   {
     printf("\nInvalid Tab!!! \n");
   }
   
      }
 
  
} 

void book(stack *s)
{  int i;
  if(s->top2==-1)
  {
    printf("\nNo bookmarks!!! \n");
    return;
  }
  else
    {
       {for(i=s->top2;i>=0;i--)
    printf("%s\n",s->bookmark[i]);}
    }
}
  




int main()
{   stack s;
    s.top = -1;
    s.top1 = - 1;
    s. top2=-1;
  int ch;
  printf("BROWSER TAB SYSTEM \n");
  while(1)
  {
    printf("Enter \n 1:Add a tab \n 2:Incognito tab \n 3:Back\n 4:Add to Bookmarks\n 5:Recent Tabs\n 6:View Bookmarks \n 7:View History \n 8:Exit\n");
    scanf("%d",&ch);
    //printf("************\n");
    if(ch==8)
    break;
    switch(ch)
    {
      case 1:    push(&s,ch);
                       break;
                     
      case 2 :  push(&s,ch);
                      break;             
          
      case 3 :  pop(&s);
                      break;    
    
      case 4 : bookmark(&s);
                     break;
          
      case 5 : display(&s);
                     break;      
      case 6 : book(&s);
                     break;               
          
      case 7 : past(&s) ;
                     break;     
                     
      default : printf("\nInvalid choice\n");  
    }
  }
  return 0;
}

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
char arr[]={"ABCDEFGHIJKLMNOPQRSTUVWXYZ    "};
int pos1[20];
int pos2[20];
int main()
{
	int num, guess, tries = 0,option;
	srand(time(0)); //seed random number generator
	num = rand() % 100 + 1; // random number between 1 and 100
	cout<<"1.Guess my number game 2. find the word game";
	cin>>option;
	switch(option)
	{case 1: int i,no,j,z;
		textattr(1<<4|14);
		clrscr();
		cprintf("Asume A Word!\n\n\rStep 1:\n\r=======\n\rTabel 1:\n\n\r");
		textattr(1<<4|12);
		for(i=0;i<5;i++)
			cprintf("%d ",i+1);
		textattr(7<<4);
		for(i=0;i<30;i++)
		 {
			 if(i%5==0)
			 printf("\n");
 			cprintf("%c ",arr[i]);
 		}
		textattr(1<<4|14);
		gotoxy(1,15);
		cprintf("\n\n\rEnter Total Number of letters in word:");
		cscanf("%d",&no);
		cprintf("                                            ");
		for(i=0;i<no;i++)
		{
			gotoxy(1,15);
			cprintf("\n\n\rEnter Letter %d Coloumn number:",i+1);
			scanf("%d",&pos1[i]);
			pos1[i]-=1;
		}
		clrscr();
		cprintf("Step 2:\n\rTabel 2:\n\r");
		textattr(1<<4|12);
		for(i=0;i<6;i++)
			cprintf("%d ",i+1);
		textattr(7<<4);
		for(i=0;i<no;i++)
		 {
			 printf("\n");
 			for(j=pos1[i];j<30;j+=5)
   			 cprintf("%c ",arr[j]);
		 }
		textattr(1<<4|14);
		for(i=0;i<no;i++)
		{
			gotoxy(1,15);
			cprintf("\n\n\rEnter the  %d Letter's Coloumn number:",i+1);
			scanf("%d",&pos2[i]);
			pos2[i]-=1;
		}
		clrscr();
		gotoxy(30,13);
		cprintf("We Got U! ");
		gotoxy(30,15);
		cprintf("SURPRISED!");
		textcolor(WHITE+BLINK);
		gotoxy(30,14);
		for(i=0;i<no;i++)
		{
			cprintf("%c",arr[pos2[i]*5+pos1[i]]);
		}
		textcolor(YELLOW+BLINK);
		cprintf("\n\n\n\n\n\n\n\n\rPress Esc To Exit...");
		while(getch()!=27);
	break;

	 
	 
	case 2:

	do
	{
		cout << "Enter a guess between 1 and 100 : ";
		cin >> guess;
		tries++;

		if (guess > num)
		{	cout << "Too high!\n\n";
		 	if(num<50)
				cout<<"try to guess under 50";
		}
		else if (guess < num)
		{		cout << "Too low!\n\n";
		 		if(num>50)
					cout<<"try to guess above 50";
		}
		else if(guess==num-1 || guess == num+1)
				cout<<"you are soo close";
		else if(guess>100)
			cout<<"are you high, enter any number between 1 and 100";
		
		else
			cout << "\nCorrect! You got it in " << tries << " guesses!\n";
	} while (guess != num);
	 
	 default: cout<"enter options 1 and 2 only";

	return 0;
}

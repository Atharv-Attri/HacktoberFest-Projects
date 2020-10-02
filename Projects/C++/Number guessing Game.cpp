#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
	int num, guess, tries = 0;
	srand(time(0)); //seed random number generator
	num = rand() % 100 + 1; // random number between 1 and 100
	cout << "Guess My Number Game\n\n";

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

	return 0;
}

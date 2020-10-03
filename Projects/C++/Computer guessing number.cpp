/* Computer guesses user number in range (1, 2000000) in 32 tries  
The idea of this game is binary search. 
Here is an example of it : https://www.geeksforgeeks.org/binary-search/ .
*/

#include <iostream>
#include <algorithm>

int main()
{
    int num;
    system("clear");
    std::string color = "\033[1;33m";
    std::cout << color;
    std::cout << "Rules:\n1.If the guess is bigger than your number, write smaller, if it is equal, write equal, otherwise bigger.\n";
    int guesses = 32;
    bool won = false;
    int l = 1, r = 2000000;
    while(l <= r && guesses > 0 && !won)
    {
        int guess = l + (r - l) / 2;
        std::cout << "Computer guess is " << guess << ".\n";
        std::flush(std::cout);
        std::string user;
        std::getline(std::cin, user);
        std::for_each(user.begin(), user.end(), [](char &c){return tolower(c);});
        if(user == "equal")
        {
            std::cout << "The number was " << guess << ".\n";
            won = true;
        }
        else if(user == "smaller")
        {
            r = guess - 1;
        }
        else {
            l = guess + 1;
        }
        guesses--;
        if(!won)
        std::cout << "The computer has " << guesses << " guesses left.\n"; 
    }
    if(won)
    {
        std::cout << "Computer knew it.\n";
    }
    else
    {
        std::cout << "Somehow, I was mistaken.\n";
    }
    return 0;
}
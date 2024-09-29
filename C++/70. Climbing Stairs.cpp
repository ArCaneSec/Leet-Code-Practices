#include <iostream>

int calc(int n)
{
    if (n < 4)
    {
        return n;
    }

    int n_minus_one = 2;
    int n_minus_two = 1; 

    for(int i = 3; i < n; i++)
    {
        int temp = n_minus_one;
        n_minus_one += n_minus_two;
        n_minus_two = temp;
    }

    return n_minus_one + n_minus_two;
}


int main()
{
    std::cout << calc(45);
}
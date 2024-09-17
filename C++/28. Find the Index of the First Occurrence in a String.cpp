#include <iostream>
#include <cstring>

class Solution
{
public:
    int strStr(std::string haystack, std::string needle)
    {
        int n_size = needle.size();
        int h_size = haystack.size();

        if (n_size > h_size)
        {
            return -1;
        }

        int ans{};
        int j{};
        for (int i = 0; i < h_size; i++)
        {
            if (haystack[i] == needle[j])
            {
                if (j == 0) 
                {
                    ans = i;
                }
                j++;

                if (j >= n_size)
                {
                    return ans;
                }
            }
            else
            {
                if (j > 0)
                {
                    i = ans;
                }
                ans = -1;
                j = 0;
            }
        }

        if (n_size == j)
        {
            return ans;
        }
        return -1;
    }
};

int main()
{
    auto s{Solution{}};
    std::cout << s.strStr("mississippi", "sippia") << std::endl;
    
    return 0;
}
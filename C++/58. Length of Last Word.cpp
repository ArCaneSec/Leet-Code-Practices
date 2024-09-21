#include <iostream>

class Solution
{
public:
    int lengthOfLastWord(std::string s)
    {
        int ans{};
        bool begins = false;
        for (int i = std::size(s) - 1; i >= 0; i--)
        {
            switch (s[i])
            {
                case ' ':
                    if (!begins) continue;
                    else return ans;
                    break;
                default:
                    if (!begins) begins = true;
                    ans ++;
            }
        }

        return ans;
    }
};

int main()
{
    auto ans = Solution().lengthOfLastWord("g");
    std::cout << ans << std::endl;

    return 0;
}
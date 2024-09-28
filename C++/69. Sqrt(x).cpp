class Solution {
public:
    int mySqrt(int x) {
        if (x < 2)
        {
            return x;
        }
        
        long start = 1;
        long mid{};
        long end = x;
        long square{};
        
        while(end >= start)
        {
            mid = (start + end) / 2;

            square = mid * mid;
            if (square == x)
            {
                return mid;
            }
            else if (square > x)
            {
                end = mid - 1;
            }
            else
            {
                start = mid + 1;
            }
        }
        return end;
    }
};
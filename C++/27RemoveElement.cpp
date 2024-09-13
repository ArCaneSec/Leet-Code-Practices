#include <iostream>
#include <vector>

int removeElement(std::vector<int> &nums, int val)
{
	int ans = 0;
	int j = std::size(nums) - 1;

	for (int index = 0; index <= j; index++)
	{
		if (nums[index] == val)
		{
			nums[index] = nums[j];
			nums[j] = -1;
			j--; index --;
		}
		else
		{
			ans++;
		}
	}

	return ans;
}

int main()
{
	std::vector<int> arr = {0,1,2,2,3,0,4,2};
	std::cout << removeElement(arr, 2) << std::endl;
	for (int elem : arr)
	{
		std::cout << elem;
	}

	return 0;
}
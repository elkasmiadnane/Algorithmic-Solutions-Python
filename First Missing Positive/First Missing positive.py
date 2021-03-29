from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:

        container = []
        counter = True



        while (counter == True):

            for item in range(1 , 300):

                if nums.__contains__(item):
                    container.append(item)

                else:
                    counter = False
                    container.append(item)
                    break


        return container[-1]

if __name__ == '__main__':
    solution = Solution()

    # Unit Tests

    assert (solution.firstMissingPositive([0,2]) == 1)
    assert (solution.firstMissingPositive([-302, 0,1,2,3, -100 ]) == 4)
    assert (solution.firstMissingPositive([-302, 400 ]) == 1)

    print(' End of Tasks ')
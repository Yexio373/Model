def find_factor(nums: int) -> str:
    #find_factor Custom functions
    #nums     Pass a positive integer argument
             #Returns all the factors of a positive integer as a string
    factors = []
    for i in range(1, nums+1):
        if nums % i == 0:
            factors.append(i)
    return factors
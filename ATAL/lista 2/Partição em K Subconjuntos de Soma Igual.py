def main():
    n, k = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))

    total = sum(nums)

    if total % k != 0:
        print("false")
        return

    alvo = total // k

    nums.sort(reverse=True)

    if nums[0] > alvo:
        print("false")
        return
    
    sum_gp = [0] * k
    
    def bt(i):
        if i >= len(nums):
            return True

        num = nums[i]
        
        for j in range(k):
            if sum_gp[j] + num > alvo:
                continue
            
            sum_gp[j] += num
            
            if bt(i + 1):
                return True
            
            sum_gp[j] -= num
            
            if sum_gp[j] == 0:
                break
        
        return False
    
    print("true" if bt(0) else "false")
            

if __name__ == "__main__":
    main()

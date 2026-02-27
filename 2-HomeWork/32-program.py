def combinationSum(candidates, target):
    result = []
    
    def backtrack(remaining, stack, start_index):
        if remaining == 0:
            result.append(list(stack))
            return
        
        if remaining < 0:
            return
        
        for i in range(start_index, len(candidates)):
            stack.append(candidates[i])
            
            backtrack(remaining - candidates[i], stack, i)
            
            stack.pop()

    backtrack(target, [], 0)
    return result

candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
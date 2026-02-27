def combinationSum2(candidates, target):
    candidates.sort()  # Essential for skipping duplicates
    result = []
    
    def backtrack(remaining, stack, start_index):
        if remaining == 0:
            result.append(list(stack))
            return
        if remaining < 0:
            return
        
        for i in range(start_index, len(candidates)):
            if i > start_index and candidates[i] == candidates[i-1]:
                continue
                
            stack.append(candidates[i])
            backtrack(remaining - candidates[i], stack, i + 1)
            stack.pop()

    backtrack(target, [], 0)
    return result

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))
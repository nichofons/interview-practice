func twoSum(nums []int, target int) []int {
    // Key: the number, Value: its index in the slice
    seen := make(map[int]int)
    
    for i, num := range nums {
        complement := target - num
        
        // Check if the required complement already exists in our map
        if index, found := seen[complement]; found {
            return []int{index, i}
        }
        
        // Store the current number and its index
        seen[num] = i
    }
    
    // Return nil or empty slice if no solution is found (per constraints, a solution always exists)
    return nil
}

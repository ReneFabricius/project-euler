
def problem148(n):
    c = 1
    remaining_rows = n - 1
    
    def countNondivisible(prev_length, prev_count):
        nonlocal c
        nonlocal remaining_rows
        
        levels_count = int(remaining_rows / prev_length)
        
        if levels_count >= 6:
            c += 27*prev_count
            current_count = 28*prev_count
            remaining_rows -= 6*prev_length
            
            starting_apexes_count = countNondivisible(7*prev_length, current_count)
            
            levels_count = int(remaining_rows / prev_length)
            
            if levels_count >= 1:
                c += int(starting_apexes_count*(1 + levels_count)*prev_count*levels_count/2)
                remaining_rows -= levels_count*prev_length
            
            return starting_apexes_count*(levels_count + 1)
        
        c += int((4 + levels_count - 1)*prev_count*levels_count/2)
        remaining_rows -= levels_count*prev_length
        
        return 2 + levels_count
    
    countNondivisible(1, 1)
    
    return c
            

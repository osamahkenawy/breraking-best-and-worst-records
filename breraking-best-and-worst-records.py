def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]
    
    max_count = 0
    min_count = 0
    
    
    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1
    
    return max_count, min_count

   #  [10, 5, 20, 20, 4, 5, 2, 25, 1]


    # Iteration Table:
    # | Iteration | Current Score | max_score | min_score | max_count | min_count | Action                           
    # |-----------|---------------|-----------|-----------|-----------|-----------|----------------------------------
    # | 1         | 5             | 10        | 5         | 0         | 1         | New min record set               
    # | 2         | 20            | 20        | 5         | 1         | 1         | New max record set               
    # | 3         | 20            | 20        | 5         | 1         | 1         | No change                        
    # | 4         | 4             | 20        | 4         | 1         | 2         | New min record set               
    # | 5         | 5             | 20        | 4         | 1         | 2         | No change                        
    # | 6         | 2             | 20        | 2         | 1         | 3         | New min record set               
    # | 7         | 25            | 25        | 2         | 2         | 3         | New max record set               
    # | 8         | 1             | 25        | 1         | 2         | 4         | New min record set               




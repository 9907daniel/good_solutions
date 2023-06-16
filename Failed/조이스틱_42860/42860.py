def solution(name):
    # alphabet = ["a","b","c","d","e","f","g","h","i","j",
    #              "k", "l","m","n","o","p","q", "r","s","t","u","v","w","x","y","z"]
    # print(ord("A")) = 65
    
    new_name = [a for a in name]
    
    # iterate를 하면서 넘어갈때 옆으로 갈까, 뒤로 갈까를 고려
    # if next one is closer to the left / right
    

    # current = 0
    # for b,a in enumerate(new_name):
    
    
    
    
    check = 0
    for a in new_name:
        if a != "A":
            check +=1 
    
    count = 0
    previous = 0
    consecutive_a = 0
    a = 0
    
    
    if check == 1:
        a= 0
        for a in range(1):
            positive_count = 1
            for c in range(previous+1,len(new_name)):
                if new_name[c] != "A":
                    positive = c
                    break
                positive_count += 1
            negative_count = 1
            for d in range(len(new_name)-1,-1,-1):
                if new_name[d] != "A":
                    negative = d
                    break
                negative_count += 1

            if positive_count > negative_count+previous:
                count += negative_count+previous
                previous = negative
            else:
                count += positive_count
                previous = positive
    
            if ord(new_name[previous])-ord("A") > 13:
                count += abs(ord("Z")-ord(new_name[previous])+1)

            else:
                count += abs(ord("A")-ord(new_name[previous]))
        a += 1
    
    
    # current
    
    while a <= check-1:        
        if a != 0:
            positive_count = 1
            for c in range(previous+1,len(new_name)):
                if new_name[c] != "A":
                    positive = c
                    break
                positive_count += 1
            negative_count = 1
            for d in range(len(new_name)-1,-1,-1):
                if new_name[d] != "A":
                    negative = d
                    break
                negative_count += 1

            if positive_count > negative_count+previous:
                count += negative_count+previous
                previous = negative
            else:
                count += positive_count
                previous = positive
    
        if ord(new_name[previous])-ord("A") > 13:
            count += abs(ord("Z")-ord(new_name[previous])+1)
            # print(abs(ord("Z")-ord(new_name[previous])+1))
        else:

            count += abs(ord("A")-ord(new_name[previous]))
            print(abs(ord("A")-ord(new_name[previous])))
        a += 1
    
    return count





        
        
#         if a == "A":
#             consecutive_a += 1
#             continue
                
#         if b-previous > len(new_name)-b:
#             count += len(new_name)-b
#         else:
#             count += b-previous
        
    
        
#         consecutive_a = 0
#         previous = b
        
        
                
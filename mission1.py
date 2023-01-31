#function to get input
def get_input(num):
    arr = list(map(int,input().split()))
    result =[]
    if len(arr) > num:
        print("Limit execeeded")
        return
    else:
        return sum_of_squares(arr)
     

#function to calcuate
def sum_of_squares(arr):        
    if arr and arr[0] >= 1:
        return arr[0]**2 + sum_of_squares(arr[1:])
    elif arr and arr[0] < 1:
        return sum_of_squares(arr[1:])
    else:
        return 0

def print_arr(arr):
    if len(arr) == 0:
        return
    else:
        print(arr[0])
        print_arr(arr[1:])
    

def main():
    test_cases = int(input())
    if test_cases >= 1 and test_cases <= 100:
        result = []
        try:
            for i in range(0,test_cases):
                num = int(input())
                result.append(get_input(num))
        except:
            print("Enter a valid number")
            
        print_arr(result)            
    else:   
        print("Input should be from 1 to 100")
        
        
if __name__ == "__main__":
    main()

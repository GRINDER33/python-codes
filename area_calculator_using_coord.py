import math
A_coord = eval(input("Enter the first vertex: "))
B_coord = eval(input("Enter the second vertex: "))
C_coord = eval(input("Enter the third vertex: "))
D_coord = eval(input("Enter the fourth vertex: "))


try:
    area1 = 1/2*(
        A_coord[0]*(B_coord[1] - C_coord[1]) + 
        B_coord[0]*(C_coord[1] - A_coord[1]) + 
        C_coord[0]*(A_coord[1] - B_coord[1])
                )
    
    area2 = 1/2*(
        A_coord[0]*(C_coord[1] - D_coord[1]) + 
        C_coord[0]*(D_coord[1] - A_coord[1]) + 
        D_coord[0]*(A_coord[1] - C_coord[1]))
    
    area = area1 + area2
    area = math.fabs(area)
except Exception:
    print('error')
print(f'Area:{area}')



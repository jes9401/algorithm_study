#4번
import copy

def g(w,h,grid,temp,dx,dy,n):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            num = grid[i][j]
            isTrue = True
            for mode in range(len(dx)):
                if i+dx[mode]>(h-1) or j+dy[mode]>(w-1):
                    isTrue = False
                    break
                if grid[i+dx[mode]][j+dy[mode]] == num:
                    pass
                else:
                    isTrue = False
                    break
            if isTrue:
                temp.extend([n])
    return temp


def solution(grid):
    answer=[]
    grid2 = copy.deepcopy(grid)
    for i in range(len(grid2)):
        grid2[i] = grid2[i][::-1]
    grid3 = list(map(list,zip(*grid)))
    grid3 = grid3[::-1]
    w = len(grid[0])
    h = len(grid)
    w3 = len(grid3[0])
    h3 = len(grid3)
    temp = []
    if w<2 or h<2:
        answer = [1,w*h]
    else:
        n = 2
        while (n*2-1)<=w:
            dx = []
            dy = []
            for i in range(n):
                for j in range(n):
                    dx.append(i)
                    dy.append(j+i)
            temp = g(w,h,grid,temp,dx,dy,n)
            temp = g(w,h,grid2,temp,dx,dy,n)
            temp = g(w3,h3,grid3,temp,dx,dy,n)
            n+=1
    if len(temp)==0:
        answer = [1,w*h]
    else:
        answer = [max(temp),temp.count(max(temp))]
    return answer

print(solution([[2,1,1,3,5,1],[1,1,3,3,5,5],[8,3,3,3,1,5],[3,3,3,4,4,4],[3,3,4,4,4,4],[1,4,4,4,4,4]]))
print(solution([[10,20,30],[40,50,60],[70,80,90]]))
print(solution([[1,1,1,1],[1,1,1,1]]))

# java 짜증난다.. 변환해서 풀어보자..
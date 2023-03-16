def towerofhanoi(n,from_rod,to_rod,aux_rod):
    if n==1:
        print("move disk 1 from_rod",from_rod,"to rod",to_rod)
        return
    towerofhanoi(n-1,from_rod,aux_rod,to_rod)
    print("move disk",n,"from rod",from_rod,"to rod",to_rod)
    towerofhanoi(n-1,aux_rod,to_rod,from_rod)
disks=int(input('enter number of disks:'))
towerofhanoi(disks,'A','B','C')

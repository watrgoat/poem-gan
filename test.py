from multiprocessing import Pool
def f(x):
    return(x*x)
if __name__ == '__main__':
    p = Pool(10) # Spawning 10 processes
    ans = p.map(f, [1,2,3,4,5,6,7,8,9])
    p.terminate() # Destroying the 10 processes
    print(ans)
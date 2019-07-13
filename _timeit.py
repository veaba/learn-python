# todo 
from timeit import Timer
Timer('t=a;a=b;b=t','a=1,b=2,c=3').timeit()
Timer('a,b=b,a','a=1,b=2,c=3').timeit()

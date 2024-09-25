
import time as t 
from test  import add

#def testFn():
 #   pass

startTime = t.time()
#add(5,3)
endTime = t.time()
runTimeInSec = endTime - startTime
print(f"\n time to execute function is {runTimeInSec/60} min")

result = add(5, 3)
print(result)


    

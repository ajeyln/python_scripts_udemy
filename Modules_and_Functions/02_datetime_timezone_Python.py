import time
from time import time as my_timer
import random
input("Press enter to start")

wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")
end_time = my_timer()

print("Started at"+time.starftime("&X",time.localtime(start_time)))
print("Ended at"+time.starftime("&X",time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))

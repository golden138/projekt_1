import tqdm
import time
import random

# użycie tqdm pasek postempu 
for i in tqdm.tqdm(range(100)):
    time.sleep(random.random())
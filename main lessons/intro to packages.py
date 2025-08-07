import emoji
from tqdm import tqdm
from time import sleep


print(emoji.emojize("shayan is :red_heart:"))

for i in tqdm(range(1000)):
    sleep(0.1)


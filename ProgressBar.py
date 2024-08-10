from tqdm import trange
from time import sleep

bar = trange(100, desc="Hacking started...", leave=True)
for idx in bar:
    bar.set_description(f"Hacking {idx}% completed...", refresh=True)
    sleep(0.0666)
print("Hacking complete!")
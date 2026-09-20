import time
for i in range(101):
    print(f"\rProgress: {i}%", end="", flush=True)
    time.sleep(0.1)
print()

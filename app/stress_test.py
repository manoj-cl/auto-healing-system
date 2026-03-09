import time

data = []

print("Starting stress test...")

while True:
    # CPU load
    for i in range(10**7):
        _ = i * i

    # Memory load
    data.append("X" * 10_000_000)

    print("CPU and memory load generated")
    time.sleep(1)
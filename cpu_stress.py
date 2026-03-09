import multiprocessing

def burn_cpu():
    while True:
        pass

if __name__ == "__main__":
    cores = multiprocessing.cpu_count()
    processes = []

    for _ in range(cores):
        p = multiprocessing.Process(target=burn_cpu)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
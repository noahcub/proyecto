import threading

class MiHilo(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print(f"Soy el hilo {self.num}")


print("Soy el hilo principal")
for i in range(10):
    hilo = MiHilo(i)
    hilo.start()
    hilo.join()
import threading
def coder(k,x):
    print(f'coder ID::{k}{x}')
threads =[]
for k in range(4):
    for x in range(4):
        t=threading.Thread(target=coder,args=(k,x))
        threads.append(t)
        t.start()


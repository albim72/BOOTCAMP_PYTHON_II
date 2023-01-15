from time import  sleep

class CountDown:
    def __init__(self,step):
        self.step = step

    def __next__(self):
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        return self

if __name__ == '__main__':
    print("Odliczanie: ")
    for element in CountDown(10):
        print(f'*{element}')
        sleep(0.2)

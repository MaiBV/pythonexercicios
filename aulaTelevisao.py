class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1


if __name__ == '__main__':
    televisao = Televisao()
    print(f'Televisão está ligada: {televisao.ligada}')
    televisao.power()
    print(f'Televisão está ligada: {televisao.ligada}')
    televisao.power()
    print(f'Televisão está ligada: {televisao.ligada}')
    print(f'Canal: {televisao.canal}')
    televisao.power()
    print(f'Televisão está ligada: {televisao.ligada}')
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print(f'Canal: {televisao.canal}')
    televisao.diminui_canal()
    print(f'Canal: {televisao.canal}')
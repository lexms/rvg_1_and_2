# NIM : 10116370
# Nama : Alexander M S
# Kelas : MOSI-8
import math

class Simulate_case_2:
    def __init__(self):
        self.a = 7
        self.m = 128
        self.z0 = 12357
        self.beta = 0.1
        self.count = 10

    def multiplicative_formula(self,zi_minus_1):
        return (self.a * zi_minus_1) % self.m

    def ui_generate(self, zi):
        return zi / self.m

    def t_generate(self,ui):
        return -1*self.beta*math.log(ui)

    def multiplicative_list(self):
        _list = []
        for i in range(0,self.count):
            if i == 0:
                zi = self.multiplicative_formula(self.z0)
                ui = self.ui_generate(zi)
                t = self.t_generate(ui)
                _list.append({'Zi-1': self.z0, 'Zi' : zi, 'Ui' : ui, 'T': t})
            elif i>0:
                zi_minus_1 = self.multiplicative_formula(_list[i-1]['Zi-1'])   
                zi = self.multiplicative_formula(zi_minus_1)
                ui = self.ui_generate(zi)
                t = self.t_generate(ui)
                _list.append({'Zi-1': zi_minus_1, 'Zi' : zi, 'Ui' : ui, 'T': t})

        return _list

    def print_table(self):
        _list = self.multiplicative_list()
        print('No.\t | Zi\t\t | Ui\t\t | T(menit)\t\t')
        print('--------------------------------------------------------------------------')
        for i in range(0,len(_list)):
            print("| {}\t | {:.4f} \t | {:.4f} \t | {:.4f} \t |".format(i+1, _list[i]['Zi'], _list[i]['Ui'], _list[i]['T']))

    def get_mean_time(self):
        _list = self.multiplicative_list()
        x=0
        for i in range(0,len(_list)):
            x = _list[i]['T'] + x
        mean = x/self.count

        print('\n Rata-rata = ', mean)

test = Simulate_case_2()

test.print_table()
test.get_mean_time()

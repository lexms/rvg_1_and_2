# NIM : 10116370
# Nama : Alexander M S
# Kelas : MOSI-8

class Simulate_case_1:
    def __init__(self):
        self.a = 7
        self.m = 128
        self.z0 = 12357
        self.min = 800000
        self.max = 1000000

    def multiplicative_formula(self,zi_minus_1):
        return (self.a * zi_minus_1) % self.m

    def ui_generate(self, zi):
        return zi / self.m

    def x_generate(self, ui):
        return (self.min + ( (self.max - self.min) * ui) )

    def multiplicative_list(self):
        _list = []
        for i in range(0,10):
            if i == 0:
                zi = self.multiplicative_formula(self.z0)
                ui = self.ui_generate(zi)
                x = self.x_generate(ui)
                _list.append({'Zi-1': self.z0, 'Zi' : zi, 'Ui' : ui, 'X': x})
            elif i>0:
                zi_minus_1 = self.multiplicative_formula(_list[i-1]['Zi-1'])   
                zi = self.multiplicative_formula(zi_minus_1)
                ui = self.ui_generate(zi)
                x = self.x_generate(ui)
                _list.append({'Zi-1': zi_minus_1, 'Zi' : zi, 'Ui' : ui, 'X': x})

        return _list

    def print_table(self):
        _list = self.multiplicative_list()
        print('No.\t | Zi\t\t | Ui\t\t | x\t\t')
        print('--------------------------------------------------------------------------')
        for i in range(0,len(_list)):
            print("| {}\t | {:.4f} \t | {:.4f} \t | {:.4f} \t |".format(i+1, _list[i]['Zi'], _list[i]['Ui'], _list[i]['X']))

test = Simulate_case_1()

test.print_table()

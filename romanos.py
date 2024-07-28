import tkinter as tk
from tkinter import messagebox

#Classe de conversao númerica
class ConversorNumerico:
    def __init__(self):
        self.dict_real_romanos = {
            1000:'M', 900:'CM', 500:'D', 400:'CD',
            100:'C', 90:'XC', 50:'L', 40:'XL',
            10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'
        }
        self.dict_romano_para_real = {romano: valor for valor, romano in self.dict_real_romanos.items()}

    #Converte um número inteiro em romano
    def real_para_romano(self, numero):
        
        # Verifica se o número informado é válido e se está entre os valores de conversão
        if not isinstance(numero, int) or numero <= 0 or numero >= 4000:
            return {'erro': 'Número deve ser um inteiro entre 1 e 3999.'}
        
        romano = ''
        for valor, simbolo in self.dict_real_romanos.items():
            while numero >= valor:
                romano += simbolo
                numero -= valor
        return {'resultado': romano}

    #Converte um número romano em inteiro
    def romano_para_real(self, romano):        

        count = 0
        numero = 0

        while(count < len(romano)):
            #Verifica se existem 2 digitos e se existem no dicionario romano
            if(count + 1 < len(romano) and romano[count:count+2] in self.dict_romano_para_real):
                numero += self.dict_romano_para_real[romano[count:count+2]]
                count += 2
            elif (romano[count:count+1] in self.dict_romano_para_real): 
                numero += self.dict_romano_para_real[romano[count]]
                count += 1
            else:
                return {'erro': 'Por favor, informe um número romano válido.'}
            
            
        return {'resultado': numero}

class InterfaceGrafica:
    def __init__(self, root):
        self.conversor = ConversorNumerico()
        self.root = root
        self.root.title("Conversor númerico")
    
        # Título do App
        self.label1 = tk.Label(root, text="Conversor Númerico")
        self.label1.pack(pady=10)
        
        # Seção para Real para Romano
        self.label2 = tk.Label(root, text="Digite um número romano ou um número real:")
        self.label2.pack(pady=5)

        self.entry_real = tk.Entry(root)
        self.entry_real.pack(pady=5)

        self.button_convert = tk.Button(root, text="Converter :)", command=self.converter)
        self.button_convert.pack(pady=5)
        
        self.resultado = tk.Label(root, text="")
        self.resultado.pack(pady=5)

    def converter(self):
        numero = self.entry_real.get()
        if numero.isdigit():
            retorno = self.conversor.real_para_romano(int(numero))
        else: 
            retorno = self.conversor.romano_para_real(numero.upper())
        
        #Caso ocorra algum erro durante a conversão
        if 'erro' in retorno:
            messagebox.showerror("Erro", retorno['erro'])
        else:
            messagebox.showinfo('Convertido', f"O número {numero} foi convertido para {retorno['resultado']}")
        
        self.entry_real.delete(0, tk.END)

root = tk.Tk()
app = InterfaceGrafica(root)
root.mainloop()



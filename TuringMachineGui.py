import tk
from TuringMachine import TuringMachine

class TuringMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina de Turing - Suma Binaria")
        
        tk.Label(self.root, text="Ingrese la suma binaria (e.g., 10+1):").pack(pady=5)
        self.entry = tk.Entry(self.root, width=20)
        self.entry.pack(pady=5)

        self.calculate_button = tk.Button(self.root, text="Calcular", command=self.calculate_sum)
        self.calculate_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="Resultado: ")
        self.result_label.pack(pady=5)

    def calculate_sum(self):
        input_value = self.entry.get()
        if '+' in input_value:
            tm = TuringMachine(tape=input_value)
            result = tm.run()
            self.result_label.config(text=f"Resultado: {result}")
        else:
            self.result_label.config(text="Error: Por favor, ingrese en formato binario (ej. 10+1)")

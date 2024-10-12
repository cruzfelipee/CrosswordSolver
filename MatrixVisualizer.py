import tkinter as tk

#CODIGO GERADO COMPLETAMENTE POR IA GENERATIVA (CHAT GPT)
def visualizeMatrix(matriz):
    # Função para criar a interface gráfica para visualizar a matriz
    root = tk.Tk()
    root.title("Visualização da Matriz de Caracteres")

    rows = len(matriz)
    cols = len(matriz[0])

    # Criação de um frame para conter a matriz
    frame = tk.Frame(root)
    frame.grid(row=0, column=0)

    # Percorrendo a matriz e criando labels para cada caractere
    for i in range(rows):
        for j in range(cols):
            label = tk.Label(
                frame,
                text=matriz[i][j],
                font=('Arial', 20),
                width=2,
                height=1,
                padx=5,
                pady=5,
                borderwidth=1,
                relief="solid",
                background="black" if matriz[i][j] == "." else "white",
                )
            label.grid(row=i, column=j)

    # Executando a interface gráfica
    root.mainloop()
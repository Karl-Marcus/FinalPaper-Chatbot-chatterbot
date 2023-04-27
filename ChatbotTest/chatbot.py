from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import tkinter as tk

chatbot = ChatBot("Sócrates")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.portuguese.jorgeamado")
trainer.train('chatterbot.corpus.portuguese.conversas')

exit_conditions = ("tchau", ":q", "quit", "exit")

def enviar_mensagem(event):
    mensagem = caixa_de_texto.get()
    if mensagem.strip():
        resposta = chatbot.get_response(mensagem)
        caixa_de_resposta.configure(state="normal")
        caixa_de_resposta.insert(tk.END, f'Você: {mensagem}\n', "direita")
        caixa_de_resposta.insert(tk.END, f'Sócrates: {resposta}\n\n', "esquerda")
        caixa_de_resposta.configure(state="disabled")
        caixa_de_texto.delete(0, tk.END)
        
def fechar_janela():
    janela.quit()

janela = tk.Tk()
janela.title("Chatbot Sócrates")

# Criar widgets
frame_resposta = tk.Frame(janela)
scrollbar_resposta = tk.Scrollbar(frame_resposta)
caixa_de_resposta = tk.Text(frame_resposta, width=50, height=15, yscrollcommand=scrollbar_resposta.set)
scrollbar_resposta.config(command=caixa_de_resposta.yview)
scrollbar_resposta.pack(side=tk.RIGHT, fill=tk.Y)
caixa_de_resposta.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
caixa_de_texto = tk.Entry(janela, width=50)
botao_enviar = tk.Button(janela, text="Enviar", command=lambda: enviar_mensagem(None))

# Adicionar widgets à janela
frame_resposta.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
caixa_de_texto.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
botao_enviar.pack(side=tk.RIGHT, padx=10, pady=10)

# Bind Enter key to enviar_mensagem function
janela.bind('<Return>', enviar_mensagem)

# Configure window resizing behavior
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)

# Configurar tags para justificar mensagens
caixa_de_resposta.tag_configure("esquerda", justify="left")
caixa_de_resposta.tag_configure("direita", justify="right")

# Associate fechar_janela function with WM_DELETE_WINDOW event
janela.protocol("WM_DELETE_WINDOW", fechar_janela)

# Iniciar loop da GUI
janela.mainloop()

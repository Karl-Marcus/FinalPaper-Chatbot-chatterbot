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
        caixa_de_texto.delete(0, tk.END)
        adicionar_mensagem(mensagem, "usuario")
        adicionar_mensagem(str(resposta), "chatbot")

def fechar_janela():
    janela.quit()

def adicionar_mensagem(mensagem, remetente):
    frame_mensagem = tk.Frame(caixa_de_resposta, bg="#dcf8c6" if remetente == "usuario" else "#f1f0f0", padx=5, pady=5)
    frame_mensagem.pack(anchor="w", pady=5, padx=10, fill="x")

    label_mensagem = tk.Label(frame_mensagem, text=mensagem, bg=frame_mensagem["bg"], wraplength=250, justify="left")
    label_mensagem.pack(anchor="w")

janela = tk.Tk()
janela.title("Chatbot Sócrates")

# Criar widgets
frame_resposta = tk.Frame(janela)
caixa_de_resposta = tk.Frame(frame_resposta)
scrollbar_resposta = tk.Scrollbar(caixa_de_resposta)
scrollbar_resposta.pack(side=tk.RIGHT, fill=tk.Y)
caixa_de_resposta.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
caixa_de_resposta.columnconfigure(0, weight=1)
caixa_de_resposta.rowconfigure(0, weight=1)
scrollbar_resposta.config(command=caixa_de_resposta.yview)
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

# Associate fechar_janela function with WM_DELETE_WINDOW event
janela.protocol("WM_DELETE_WINDOW", fechar_janela)

# Iniciar loop da GUI
janela.mainloop()
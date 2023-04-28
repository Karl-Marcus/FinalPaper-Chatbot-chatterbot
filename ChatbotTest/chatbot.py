# importar as bibliotecas necessárias
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import tkinter as tk

# definir o chatbot e treinar
chatbot = ChatBot("Sócrates")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.portuguese.jorgeamado")
trainer.train('chatterbot.corpus.portuguese.conversas')

# interromper a execução do programa (Não funciona GUI)
exit_conditions = ("tchau", ":q", "quit", "exit")

# função para enviar e receber mensagens
def enviar_mensagem(event):
    mensagem = caixa_de_texto.get()
    if mensagem.strip():
        resposta = chatbot.get_response(mensagem)
        caixa_de_resposta.configure(state="normal")
        caixa_de_resposta.insert(tk.END, f'Você: {mensagem}\n', ("esquerda", "usuario"))
        caixa_de_resposta.insert(tk.END, f'Sócrates: {resposta}\n\n', ("direita", "chatbot"))
        caixa_de_resposta.configure(state="disabled")
        caixa_de_texto.delete(0, tk.END)
        
# função para fechar a janela
def fechar_janela():
    janela.quit()

# criar a janela
janela = tk.Tk()
janela.title("Chatbot Sócrates")

# Criar widgets
frame_resposta = tk.Frame(janela, bg="white")
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

# Bind Enter key para função enviar_mensagem
janela.bind('<Return>', enviar_mensagem)

# Configurar tamanho da janela
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)

# Configurar tags para justificar mensagens
caixa_de_resposta.tag_configure("esquerda", justify="right")
caixa_de_resposta.tag_configure("direita", justify="left")

# Adicionar tags para colorir mensagens
caixa_de_resposta.tag_configure("usuario", background="#b7e1cd")
caixa_de_resposta.tag_configure("chatbot", background="#b3b3b3")

# Associaar função fechar_janela com evento WM_DELETE_WINDOW
janela.protocol("WM_DELETE_WINDOW", fechar_janela)

# Iniciar loop da GUI
janela.mainloop()

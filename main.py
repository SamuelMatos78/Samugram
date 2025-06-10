import tkinter as tk
from tkinter import Toplevel, Canvas, Scrollbar
from PIL import Image, ImageTk
import conexaodb as conn

def criar_post(container, nome_usuario, conteudo_post, imagem_post_path, curtidas_iniciais, comentarios):
    bg_post = "#2c2f33"
    fg_nome = "#ffffff"
    fg_texto = "#cccccc"
    bg_botao = "#7289da"
    fg_botao = "#ffffff"
    
    frame_post = tk.Frame(container, bg=bg_post, bd=1, relief="solid", padx=10, pady=10)
    frame_post.pack(pady=10, fill='x')  # Preencher horizontalmente

    foto_perfil = conn.buscar_foto_perfil(nome_usuario)
    
    img = Image.open(foto_perfil).resize((50, 50))
    foto = ImageTk.PhotoImage(img)
    img_label = tk.Label(frame_post, image=foto, bg=bg_post)
    img_label.image = foto
    img_label.pack(side="left", anchor="n")

    dados = tk.Frame(frame_post, bg=bg_post)
    dados.pack(side="left", padx=15, fill="x")

    nome = tk.Label(dados, text=nome_usuario, font=("Helvetica", 12, "bold"), bg=bg_post, fg=fg_nome)
    nome.pack(anchor="w")

    texto = tk.Label(dados, text=conteudo_post, wraplength=400, justify="left", bg=bg_post, fg=fg_texto)
    texto.pack(anchor="w", pady=2)

    if imagem_post_path:
        img_post = Image.open(imagem_post_path).resize((300, 200))
        img_post_tk = ImageTk.PhotoImage(img_post)
        img_label_post = tk.Label(dados, image=img_post_tk, bg=bg_post)
        img_label_post.image = img_post_tk
        img_label_post.pack(pady=5)

    frame_interacoes = tk.Frame(dados, bg=bg_post)
    frame_interacoes.pack(anchor="w", pady=(5, 0))

    curtidas_var = tk.IntVar(value=curtidas_iniciais)
    curtiu = tk.BooleanVar(value=False)

    def alternar_curtida():
        if not curtiu.get():
            curtidas_var.set(curtidas_var.get() + 1)
            botao_curtir.config(text="Descurtir 💔")
            curtiu.set(True)
        else:
            curtidas_var.set(curtidas_var.get() - 1)
            botao_curtir.config(text="Curtir ❤️")
            curtiu.set(False)
        label_interacoes.config(text=f"❤️ {curtidas_var.get()}   💬 {comentarios}")

    botao_curtir = tk.Button(frame_interacoes, text="Curtir ❤️", command=alternar_curtida,
                             font=("Helvetica", 9), bg=bg_botao, fg=fg_botao,
                             activebackground="#5b6eae", activeforeground="#ffffff", bd=0, padx=8, pady=4)
    botao_curtir.pack(side="left")

    label_interacoes = tk.Label(frame_interacoes, text=f"❤️ {curtidas_var.get()}   💬 {comentarios}",
                               font=("Helvetica", 10), fg="#999999", bg=bg_post)
    label_interacoes.pack(side="left", padx=10)


def mostrar_perfil():
    perfil = Toplevel(janela)
    perfil.title("Meu Perfil")
    perfil.configure(bg="#23272a")
    perfil.geometry("300x250")
    perfil.resizable(False, False)

    header = tk.Frame(perfil, bg="#7289da", height=60)
    header.pack(fill="x")

    titulo = tk.Label(header, text="Meu Perfil", font=("Helvetica", 14, "bold"), bg="#7289da", fg="white")
    titulo.pack(pady=15)

    conteudo = tk.Frame(perfil, bg="#23272a", padx=20, pady=20)
    conteudo.pack(fill="both", expand=True)

    nome = tk.Label(conteudo, text="👤 João Silva", font=("Helvetica", 12, "bold"), bg="#23272a", fg="#ffffff")
    nome.pack(anchor="w")

    bio = tk.Label(conteudo,
                   text="Apaixonado por tecnologia, natureza e café ☕\nMembro desde 2022.",
                   font=("Helvetica", 10), bg="#23272a", fg="#bbbbbb", justify="left", wraplength=260)
    bio.pack(anchor="w", pady=10)

    fechar = tk.Button(conteudo, text="Fechar", command=perfil.destroy,
                       bg="#7289da", fg="white", font=("Helvetica", 10, "bold"), bd=0, padx=10, pady=6)
    fechar.pack(pady=10, anchor="center")


# Criando janela principal
janela = tk.Tk()
janela.title("Minha Timeline")
janela.configure(bg="#23272a")
janela.geometry("640x700")

header = tk.Frame(janela, bg="#7289da", height=60)
header.pack(fill="x")

titulo = tk.Label(header, text="Minha Timeline", font=("Helvetica", 16, "bold"), bg="#7289da", fg="white")
titulo.pack(side="left", padx=20, pady=10)

botao_perfil = tk.Button(header, text="Meu Perfil", command=mostrar_perfil,
                        bg="#2c2f33", fg="#7289da", font=("Helvetica", 10, "bold"), bd=0, padx=12, pady=6,
                        activebackground="#1f2124", activeforeground="#99aab5")
botao_perfil.pack(side="right", padx=20, pady=10)


def mostrar_encontrar_amigo():
    janela_busca = Toplevel(janela)
    janela_busca.title("Encontre um amigo")
    janela_busca.configure(bg="#23272a")
    janela_busca.geometry("300x200")
    janela_busca.resizable(False, False)

    header = tk.Frame(janela_busca, bg="#7289da", height=60)
    header.pack(fill="x")

    titulo = tk.Label(header, text="Encontre um amigo", font=("Helvetica", 14, "bold"), bg="#7289da", fg="white")
    titulo.pack(pady=15)

    campo_busca = tk.Entry(janela_busca, font=("Helvetica", 11), bg="#2c2f33", fg="white", insertbackground="white", width=30)
    campo_busca.pack(pady=20)

    botao_buscar = tk.Button(janela_busca, text="Buscar", bg="#7289da", fg="white", font=("Helvetica", 10, "bold"), bd=0, padx=10, pady=6)
    botao_buscar.pack()

# Botões no topo
botao_encontrar = tk.Button(header, text="Encontre um amigo", command=mostrar_encontrar_amigo,
                        bg="#2c2f33", fg="#7289da", font=("Helvetica", 10, "bold"), bd=0, padx=12, pady=6,
                        activebackground="#1f2124", activeforeground="#99aab5")
botao_encontrar.pack(side="right", padx=(0, 10), pady=10)

botao_perfil.pack_configure(padx=(0, 10))  # Ajuste do espaçamento

# Estrutura com canvas à esquerda e barra lateral à direita
container_principal = tk.Frame(janela, bg="#23272a")
container_principal.pack(fill="both", expand=True)

# Parte da timeline com scroll
container_scroll = tk.Frame(container_principal, bg="#23272a")
container_scroll.pack(side="left", fill="both", expand=True)

canvas = Canvas(container_scroll, bg="#23272a", highlightthickness=0)
scrollbar = Scrollbar(container_scroll, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#23272a", width=500)



# Função para centralizar dinamicamente o frame dentro do canvas
def centralizar_scrollable_frame(event=None):
    canvas_width = canvas.winfo_width()
    frame_width = scrollable_frame.winfo_reqwidth()
    x = (canvas_width - frame_width) // 2
    if x < 0:
        x = 0
    canvas.coords(canvas_window, x, 0)

scrollable_frame.bind(
    "<Configure>",
    lambda e: [canvas.configure(scrollregion=canvas.bbox("all")), centralizar_scrollable_frame()]
)

canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="n")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", centralizar_scrollable_frame)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Barra lateral direita
barra_direita = tk.Frame(container_principal, width=180, bg="#2c2f33")
barra_direita.pack(side="right", fill="y")

titulo_amigos = tk.Label(barra_direita, text="👥 Amigos Online", font=("Helvetica", 11, "bold"),
                         bg="#2c2f33", fg="white", pady=10)
titulo_amigos.pack(anchor="w", padx=10)

amigos = [
    ("Ana", "Vendo fotos"),
    ("Lucas", "Jogando"),
    ("Mariana", "Postando"),
    ("Carlos", "Online"),
]

for nome, status in amigos:
    frame = tk.Frame(barra_direita, bg="#2c2f33")
    frame.pack(anchor="w", padx=10, pady=4)

    bolinha = tk.Label(frame, text="●", font=("Helvetica", 10), fg="green", bg="#2c2f33")
    bolinha.pack(side="left")

    nome_label = tk.Label(frame, text=f" {nome} — {status}", font=("Helvetica", 10), fg="#bbbbbb", bg="#2c2f33")
    nome_label.pack(side="left")

janela.mainloop()
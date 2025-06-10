import pymysql

def conectar():
    return pymysql.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="bdrede",
        cursorclass=pymysql.cursors.DictCursor
    )

def cadastrar_usuario(nome, email, senha_hash, foto_perfil=None):
    if foto_perfil is None:
        foto_perfil = "default.jpg"  

    if not nome or not email or not senha_hash:
        raise ValueError("Nome, email e senha_hash são obrigatórios.")
    if len(nome) > 50 or len(email) > 100 or len(senha_hash) > 255:
        raise ValueError("Nome, email ou senha_hash excedem o tamanho máximo permitido.")
    if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(senha_hash, str):
        raise TypeError("Nome, email e senha_hash devem ser strings.")
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("Email inválido.")
    
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Usuario (nome, email, senha_hash, foto_perfil) VALUES (%s, %s, %s, LOAD_FILE(%s))"
            cursor.execute(sql, (nome, email, senha_hash, foto_perfil))
        conn.commit()
    finally:
        conn.close()

def validar_login(senha_hash, email=None, nome_perfil=None):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            if email is None and nome_perfil is None:
                raise ValueError("Pelo menos um dos parâmetros 'email' ou 'nome_perfil' deve ser fornecido.")
            if email:
                sql = "SELECT * FROM Usuario WHERE email = %s AND senha_hash = %s"
                cursor.execute(sql, (email, senha_hash))
                return cursor.fetchone()
            elif nome_perfil:
                sql = "SELECT * FROM Usuario WHERE nome = %s AND senha_hash = %s"
                cursor.execute(sql, (nome_perfil, senha_hash))
                return cursor.fetchone()
    finally:
        conn.close()

def buscar_usuario(nome_usuario):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM Usuario WHERE nome_usuario = %s"
            cursor.execute(sql, (nome_usuario,))
            return cursor.fetchone()
    finally:
        conn.close()

def buscar_foto_perfil(nome_usuario):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT foto_perfil FROM Usuario WHERE nome = %s"
            cursor.execute(sql, (nome_usuario,))
            resultado = cursor.fetchone()
            return resultado['foto'] if resultado else None
    finally:
        conn.close()

def inserir_post(usuario_id, conteudo, foto=None):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Post (usuario_id, conteudo, foto) VALUES (%s, %s, LOAD_FILE(%s))"
            cursor.execute(sql, (usuario_id, conteudo, foto))
        conn.commit()
    finally:
        conn.close()

def buscar_posts():
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = """
            SELECT Post.*, Usuario.nome 
            FROM Post 
            JOIN Usuario ON Post.usuario_id = Usuario.id
            ORDER BY Post.data_post DESC
            """
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()

def curtir_post(usuario_id, post_id):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT IGNORE INTO Curtida (usuario_id, post_id) VALUES (%s, %s)"
            cursor.execute(sql, (usuario_id, post_id))
        conn.commit()
    finally:
        conn.close()

def descurtir_post(usuario_id, post_id):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM Curtida WHERE usuario_id = %s AND post_id = %s"
            cursor.execute(sql, (usuario_id, post_id))
        conn.commit()
    finally:
        conn.close()

def comentar_post(usuario_id, post_id, conteudo):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Comentario (usuario_id, post_id, conteudo) VALUES (%s, %s, %s)"
            cursor.execute(sql, (usuario_id, post_id, conteudo))
        conn.commit()
    finally:
        conn.close()

def buscar_comentarios(post_id):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = """
            SELECT Comentario.*, Usuario.nome 
            FROM Comentario 
            JOIN Usuario ON Comentario.usuario_id = Usuario.id
            WHERE Comentario.post_id = %s
            ORDER BY Comentario.data_comentario ASC
            """
            cursor.execute(sql, (post_id,))
            return cursor.fetchall()
    finally:
        conn.close()

def contar_curtidas(post_id):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT COUNT(*) as total FROM Curtida WHERE post_id = %s"
            cursor.execute(sql, (post_id,))
            return cursor.fetchone()['total']
    finally:
        conn.close()
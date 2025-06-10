import pymysql

def conectar():
    return pymysql.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="bdrede",
        cursorclass=pymysql.cursors.DictCursor
    )

def inserir_usuario(nome, email, senha_hash):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Usuario (nome, email, senha_hash) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nome, email, senha_hash))
        conn.commit()
    finally:
        conn.close()

def buscar_usuario_por_email(email):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM Usuario WHERE email = %s"
            cursor.execute(sql, (email,))
            return cursor.fetchone()
    finally:
        conn.close()

def buscar_foto_perfil(nome_usuario):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT foto FROM Usuario WHERE nome = %s"
            cursor.execute(sql, (nome_usuario,))
            resultado = cursor.fetchone()
            return resultado['foto'] if resultado else None
    finally:
        conn.close()

def inserir_post(usuario_id, conteudo, foto=None):
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO Post (usuario_id, conteudo, foto) VALUES (%s, %s, %s)"
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
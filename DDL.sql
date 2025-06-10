CREATE DATABASE redesocial;
USE redesocial;

-- Tabela de Usuários (sem prestigio geral)
CREATE TABLE Usuario (
 id INT PRIMARY KEY AUTO_INCREMENT,
 nome VARCHAR(100),
 email VARCHAR(100) UNIQUE,
 foto_perfil LONGBLOB,
 senha_hash VARCHAR(255)
);
-- Tabela de Modalidades (áreas de prestígio, ex: Lógica, Criatividade)
CREATE TABLE Modalidade (
 id INT PRIMARY KEY AUTO_INCREMENT,
 nome VARCHAR(100) UNIQUE
);
-- Modalidades que o usuário pratica, com prestígio específico
CREATE TABLE UsuarioModalidade (
 id INT PRIMARY KEY AUTO_INCREMENT,
 usuario_id INT,
 modalidade_id INT,
 prestigio INT DEFAULT 0,
 FOREIGN KEY (usuario_id) REFERENCES Usuario(id),
 FOREIGN KEY (modalidade_id) REFERENCES Modalidade(id),
 UNIQUE(usuario_id, modalidade_id)
);
-- Tabela de Posts
CREATE TABLE Post (
 id INT PRIMARY KEY AUTO_INCREMENT,
 usuario_id INT,
 foto LONGBLOB,
 conteudo TEXT,
 data_post DATETIME DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY (usuario_id) REFERENCES Usuario(id)
);
-- Complexidade do post: quantos pontos vale em cada modalidade
CREATE TABLE ComplexidadePost (
 id INT PRIMARY KEY AUTO_INCREMENT,
 post_id INT,
 modalidade_id INT,
 pontos INT,
 FOREIGN KEY (post_id) REFERENCES Post(id),
 FOREIGN KEY (modalidade_id) REFERENCES Modalidade(id)
);
-- Colaboradores marcados no post
CREATE TABLE ColaboradorPost (
 id INT PRIMARY KEY AUTO_INCREMENT,
 post_id INT,
 colaborador_id INT,
 FOREIGN KEY (post_id) REFERENCES Post(id),
 FOREIGN KEY (colaborador_id) REFERENCES Usuario(id)
);
-- Histórico de quanto cada colaborador ganhou em cada modalidade ao ser marcado
CREATE TABLE PontosGanho (
 id INT PRIMARY KEY AUTO_INCREMENT,
 colaborador_id INT,
 post_id INT,
 modalidade_id INT,
 pontos INT,
 FOREIGN KEY (colaborador_id) REFERENCES Usuario(id),
 FOREIGN KEY (post_id) REFERENCES Post(id),
 FOREIGN KEY (modalidade_id) REFERENCES Modalidade(id)
);
-- Curtidas
CREATE TABLE Curtida (
 id INT PRIMARY KEY AUTO_INCREMENT,
 usuario_id INT,
 post_id INT,
 data_curtida DATETIME DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY (usuario_id) REFERENCES Usuario(id),
 FOREIGN KEY (post_id) REFERENCES Post(id),
 UNIQUE(usuario_id, post_id)
);
-- Comentários
CREATE TABLE Comentario (
 id INT PRIMARY KEY AUTO_INCREMENT,
 usuario_id INT,
 post_id INT,
 conteudo TEXT,
 data_comentario DATETIME DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY (usuario_id) REFERENCES Usuario(id),
 FOREIGN KEY (post_id) REFERENCES Post(id)
);
-- Amizades
CREATE TABLE Amizade (
 id INT PRIMARY KEY AUTO_INCREMENT,
 usuario_id INT,
 amigo_id INT,
 FOREIGN KEY (usuario_id) REFERENCES Usuario(id),
 FOREIGN KEY (amigo_id) REFERENCES Usuario(id),
 UNIQUE(usuario_id, amigo_id)
);
-- Interesses
CREATE TABLE Interesse (
 id INT PRIMARY KEY AUTO_INCREMENT,
 usuario_id INT,
 interesse_nome VARCHAR(100),
 UNIQUE(usuario_id, interesse_nome),
 FOREIGN KEY (usuario_id) REFERENCES Usuario(id)
);
-- Chatbot
CREATE TABLE Chatbot (
 id INT PRIMARY KEY AUTO_INCREMENT,
 usuario_id INT UNIQUE,
 ultima_msg_usuario TEXT,
 ultima_msg_llm TEXT,
 FOREIGN KEY (usuario_id) REFERENCES Usuario(id)
);
-- Histórico de mensagens do chatbot
CREATE TABLE ChatHistorico (
 id INT PRIMARY KEY AUTO_INCREMENT,
 chatbot_id INT,
 remetente ENUM('usuario', 'llm'),
 mensagem TEXT,
 data_mensagem DATETIME DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY (chatbot_id) REFERENCES Chatbot(id)
);
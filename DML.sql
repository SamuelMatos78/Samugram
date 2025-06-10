-- Populando Modalidade
INSERT INTO Modalidade (nome) VALUES 
('Lógica'),
('Criatividade'),
('Comunicação'),
('Colaboração');

-- Populando Usuario
INSERT INTO Usuario (nome, email, senha_hash) VALUES
('Alice Silva', 'alice@email.com', 'hash1'),
('Bruno Souza', 'bruno@email.com', 'hash2'),
('Carla Lima', 'carla@email.com', 'hash3'),
('Daniel Costa', 'daniel@email.com', 'hash4');

-- Populando UsuarioModalidade
INSERT INTO UsuarioModalidade (usuario_id, modalidade_id, prestigio) VALUES
(1, 1, 10), -- Alice - Lógica
(1, 2, 5),  -- Alice - Criatividade
(2, 1, 7),  -- Bruno - Lógica
(2, 3, 8),  -- Bruno - Comunicação
(3, 2, 12), -- Carla - Criatividade
(3, 4, 6),  -- Carla - Colaboração
(4, 3, 9),  -- Daniel - Comunicação
(4, 4, 11); -- Daniel - Colaboração

-- Populando Post
INSERT INTO Post (usuario_id, foto, conteudo) VALUES
(1, NULL, 'Primeiro post da Alice!'),
(2, NULL, 'Bruno compartilha uma ideia.'),
(3, NULL, 'Carla posta sobre criatividade.'),
(4, NULL, 'Daniel fala sobre colaboração.');

-- Populando ComplexidadePost
INSERT INTO ComplexidadePost (post_id, modalidade_id, pontos) VALUES
(1, 1, 3), -- Post 1 - Lógica
(1, 2, 2), -- Post 1 - Criatividade
(2, 1, 4), -- Post 2 - Lógica
(2, 3, 1), -- Post 2 - Comunicação
(3, 2, 5), -- Post 3 - Criatividade
(4, 4, 4); -- Post 4 - Colaboração

-- Populando ColaboradorPost
INSERT INTO ColaboradorPost (post_id, colaborador_id) VALUES
(1, 2), -- Bruno colaborou no post da Alice
(2, 1), -- Alice colaborou no post do Bruno
(3, 4), -- Daniel colaborou no post da Carla
(4, 3); -- Carla colaborou no post do Daniel

-- Populando PontosGanho
INSERT INTO PontosGanho (colaborador_id, post_id, modalidade_id, pontos) VALUES
(2, 1, 1, 2), -- Bruno ganhou pontos em Lógica no post 1
(1, 2, 1, 2), -- Alice ganhou pontos em Lógica no post 2
(4, 3, 2, 3), -- Daniel ganhou pontos em Criatividade no post 3
(3, 4, 4, 2); -- Carla ganhou pontos em Colaboração no post 4

-- Populando Curtida
INSERT INTO Curtida (usuario_id, post_id) VALUES
(1, 2),
(2, 1),
(3, 4),
(4, 3);

-- Populando Comentario
INSERT INTO Comentario (usuario_id, post_id, conteudo) VALUES
(2, 1, 'Muito bom, Alice!'),
(1, 2, 'Ótima ideia, Bruno!'),
(4, 3, 'Criatividade é tudo!'),
(3, 4, 'Colaboração faz a diferença!');

-- Populando Amizade
INSERT INTO Amizade (usuario_id, amigo_id) VALUES
(1, 2),
(2, 1),
(1, 3),
(3, 1),
(2, 4),
(4, 2),
(3, 4),
(4, 3);

-- Populando Interesse
INSERT INTO Interesse (usuario_id, interesse_nome) VALUES
(1, 'Matemática'),
(1, 'Arte'),
(2, 'Tecnologia'),
(3, 'Design'),
(4, 'Gestão');

-- Populando Chatbot
INSERT INTO Chatbot (usuario_id, ultima_msg_usuario, ultima_msg_llm) VALUES
(1, 'Oi, chatbot!', 'Olá, Alice! Como posso ajudar?'),
(2, 'Preciso de dicas.', 'Claro, Bruno! Sobre o que?'),
(3, 'Me ajude com criatividade.', 'Vamos lá, Carla!'),
(4, 'Como melhorar colaboração?', 'Ótima pergunta, Daniel!');

-- Populando ChatHistorico
INSERT INTO ChatHistorico (chatbot_id, remetente, mensagem) VALUES
(1, 'usuario', 'Oi, chatbot!'),
(1, 'llm', 'Olá, Alice! Como posso ajudar?'),
(2, 'usuario', 'Preciso de dicas.'),
(2, 'llm', 'Claro, Bruno! Sobre o que?'),
(3, 'usuario', 'Me ajude com criatividade.'),
(3, 'llm', 'Vamos lá, Carla!'),
(4, 'usuario', 'Como melhorar colaboração?'),
(4, 'llm', 'Ótima pergunta, Daniel!');
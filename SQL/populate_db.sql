USE mercado;

-- CARRINHO
INSERT INTO carrinho VALUES (1, 1);
INSERT INTO carrinho VALUES (2, 1);
INSERT INTO carrinho VALUES (3, 2);
INSERT INTO carrinho VALUES (4, 3);

-- PRODUTO
INSERT INTO produto VALUES (1, "creme de avelã", "30.0", "doces", "Nutella", "pote com 650g", NULL);
INSERT INTO produto VALUES (2, "macarrão", "2.0", "massas", "Aurora", "pacote com 500g", NULL);
INSERT INTO produto VALUES (3, "refrigerante", "10.0", "bebidas", "Coca-Cola", "garrafa pet de 2L", NULL);

-- PRODUTO CARRINHO
INSERT INTO carrinho_produto VALUES (1, 1, 1);
INSERT INTO carrinho_produto VALUES (1, 2, 5);
INSERT INTO carrinho_produto VALUES (1, 3, 2);
INSERT INTO carrinho_produto VALUES (2, 1, 2);
INSERT INTO carrinho_produto VALUES (3, 1, 1);
INSERT INTO carrinho_produto VALUES (4, 2, 4);

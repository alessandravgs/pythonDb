#Preenchimento de dados das tabelas clientes e produtos.
create table clientes
(
	id_clientes int primary key auto_increment, 
    nome varchar(255) not null,
    cpf varchar(255) not null unique,
    email varchar(255) not null unique,
    data_Nascimento date not null
);

insert into clientes (nome, cpf, email, data_Nascimento) values ("Ana Silva", "12345678901", "ana@email.com", "1990-01-01")
insert into clientes (nome, cpf, email, data_Nascimento) values ("João Oliveira", "98765432109", "joao@email.com", "1985-05-15")
insert into clientes (nome, cpf, email, data_Nascimento) values ("Maria Souza", "56789012345", "maria@email.com", "2000-10-20")
insert into clientes (nome, cpf, email, data_Nascimento) values ("Pedro Santos", "45678901234", "pedro@email.com", "1975-03-30")
insert into clientes (nome, cpf, email, data_Nascimento) values ("Carla Lima", "34567890123", "carla@email.com", "1988-12-10")

select *  from clientes;

create table produtos
(
	id_produtos int primary key auto_increment, 
    nome varchar(255) not null unique,
    descricao text,
    preco decimal not null,
    categoria varchar(255)
);

insert into produtos (nome, descricao, preco, categoria) values 
("dyssei G6", "Monitor Samsung QWHD...", 3500, "Monitor"),
("dyssei G5", "Monitor Samsung QWHD curvado...", 2500, "Monitor"),
("Galaxy Book 2 Pro", "Notebook 16GB, tela AMOLED", 8900.90, "Notebook"),
("Galaxy Book 3 Ultra", "Notebook 32GB, tela AMOLED", 18900.90, "Notebook"),
("Samsung s24", "celuar 32GB com IA da samsung", 4900.90, "Celular");

select *  from produtos;





--
-- File generated with SQLiteStudio v3.3.3 on ven apr 22 17:01:15 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: backup
DROP TABLE IF EXISTS backup;

CREATE TABLE backup (
    rowid INTEGER PRIMARY KEY AUTOINCREMENT
                  NOT NULL,
    data  DATE    NOT NULL
);


-- Table: caixa
DROP TABLE IF EXISTS caixa;

CREATE TABLE caixa (
    data           DATE,
    saldo_anterior DOUBLE,
    caixa_terenos  DOUBLE
);


-- Table: entradas
DROP TABLE IF EXISTS entradas;

CREATE TABLE entradas (
    nome            VARCHAR (100),
    data_referencia DATE          NOT NULL,
    data_deposito   DATE          NOT NULL,
    dizimo          DOUBLE,
    doacao_terenos  DOUBLE,
    doacao_missoes  DOUBLE,
    doacao_pam      DOUBLE,
    campanha_nome   VARCHAR (50),
    doacao_campanha DOUBLE,
    forma_pagamento VARCHAR (25)  NOT NULL
);


-- Table: membros
DROP TABLE IF EXISTS membros;

CREATE TABLE membros (
    nome            VARCHAR (100) NOT NULL,
    data_nascimento DATE,
    endereco        VARCHAR (75),
    numero          INT,
    complemento     VARCHAR (100),
    bairro          VARCHAR (60),
    uf              CHAR (2),
    cidade          VARCHAR (75),
    cep             CHAR (8),
    email           VARCHAR (255),
    celular         VARCHAR (14),
    diretoria       BOOLEAN
);


-- Table: saidas
DROP TABLE IF EXISTS saidas;

CREATE TABLE saidas (
    destino VARCHAR (100) NOT NULL,
    valor   DOUBLE        NOT NULL,
    data    DATE          NOT NULL
);


-- Table: usuarios
DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
    email VARCHAR (255) UNIQUE
                        NOT NULL,
    senha VARCHAR (255) NOT NULL
);


-- View: campanhas
DROP VIEW IF EXISTS campanhas;
CREATE VIEW campanhas AS
    SELECT DISTINCT campanha_nome
      FROM entradas;


-- View: dizimos
DROP VIEW IF EXISTS dizimos;
CREATE VIEW dizimos AS
    SELECT DISTINCT nome
      FROM (
               SELECT nome,
                      dizimo
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', '-5 month', 'start of month') AND date('now') 
           )
     WHERE dizimo != '' AND 
           dizimo > 0;


-- View: gastos
DROP VIEW IF EXISTS gastos;
CREATE VIEW gastos AS
    SELECT DISTINCT destino
      FROM saidas;


-- View: ofertas
DROP VIEW IF EXISTS ofertas;
CREATE VIEW ofertas AS
    SELECT nome
      FROM (
               SELECT nome,
                      doacao_terenos,
                      doacao_missoes,
                      doacao_pam,
                      doacao_campanha
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', '-5 month', 'start of month') AND date('now') 
           )
     WHERE (doacao_terenos != '' AND 
            doacao_terenos > 0) OR 
           (doacao_missoes != '' AND 
            doacao_missoes > 0) OR 
           (doacao_pam != '' AND 
            doacao_pam > 0) OR 
           (doacao_campanha != '' AND 
            doacao_campanha > 0);


-- View: total_abril
DROP VIEW IF EXISTS total_abril;
CREATE VIEW total_abril AS
    SELECT nome,
           sum(dizimo) AS dizimo,
           sum(doacao_terenos) AS doacao_terenos,
           sum(doacao_missoes) AS doacao_missoes,
           sum(doacao_pam) AS doacao_pam,
           sum(doacao_campanha) AS doacao_campanha
      FROM (
               SELECT nome,
                      dizimo,
                      doacao_terenos,
                      doacao_missoes,
                      doacao_pam,
                      doacao_campanha,
                      data_referencia
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', 'start of year', '+3 month') AND date('now', 'start of year', '+4 month', '-1 day') 
           )
     WHERE (dizimo > 0) AND 
           (doacao_terenos > 0) AND 
           (doacao_missoes > 0) AND 
           (doacao_pam > 0) AND 
           (doacao_campanha > 0) 
     GROUP BY nome;


-- View: total_agosto
DROP VIEW IF EXISTS total_agosto;
CREATE VIEW total_agosto AS
    SELECT nome,
           sum(dizimo) AS dizimo,
           sum(doacao_terenos) AS doacao_terenos,
           sum(doacao_missoes) AS doacao_missoes,
           sum(doacao_pam) AS doacao_pam,
           sum(doacao_campanha) AS doacao_campanha
      FROM (
               SELECT nome,
                      dizimo,
                      doacao_terenos,
                      doacao_missoes,
                      doacao_pam,
                      doacao_campanha,
                      data_referencia
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', 'start of year', '+7 month') AND date('now', 'start of year', '+8 month', '-1 day') 
           )
     WHERE (dizimo > 0) AND 
           (doacao_terenos > 0) AND 
           (doacao_missoes > 0) AND 
           (doacao_pam > 0) AND 
           (doacao_campanha > 0) 
     GROUP BY nome;


-- View: total_dezembro
DROP VIEW IF EXISTS total_dezembro;
CREATE VIEW total_dezembro AS
    SELECT nome,
           sum(dizimo) AS dizimo,
           sum(doacao_terenos) AS doacao_terenos,
           sum(doacao_missoes) AS doacao_missoes,
           sum(doacao_pam) AS doacao_pam,
           sum(doacao_campanha) AS doacao_campanha
      FROM (
               SELECT nome,
                      dizimo,
                      doacao_terenos,
                      doacao_missoes,
                      doacao_pam,
                      doacao_campanha,
                      data_referencia
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', 'start of year', '+11 month') AND date('now', 'start of year', '+12 month', '-1 day') 
           )
     WHERE (dizimo > 0) AND 
           (doacao_terenos > 0) AND 
           (doacao_missoes > 0) AND 
           (doacao_pam > 0) AND 
           (doacao_campanha > 0) 
     GROUP BY nome;


-- View: total_fevereiro
DROP VIEW IF EXISTS total_fevereiro;
CREATE VIEW total_fevereiro AS
    SELECT nome,
           sum(dizimo) AS dizimo,
           sum(doacao_terenos) AS doacao_terenos,
           sum(doacao_missoes) AS doacao_missoes,
           sum(doacao_pam) AS doacao_pam,
           sum(doacao_campanha) AS doacao_campanha
      FROM (
               SELECT nome,
                      dizimo,
                      doacao_terenos,
                      doacao_missoes,
                      doacao_pam,
                      doacao_campanha,
                      data_referencia
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', 'start of year', '+1 month') AND date('now', 'start of year', '+2 month', '-1 day') 
           )
     WHERE (dizimo > 0) AND 
           (doacao_terenos > 0) AND 
           (doacao_missoes > 0) AND 
           (doacao_pam > 0) AND 
           (doacao_campanha > 0) 
     GROUP BY nome;


-- View: total_janeiro
DROP VIEW IF EXISTS total_janeiro;
CREATE VIEW total_janeiro AS
    SELECT nome,
           sum(dizimo) AS dizimo,
           sum(doacao_terenos) AS doacao_terenos,
           sum(doacao_missoes) AS doacao_missoes,
           sum(doacao_pam) AS doacao_pam,
           sum(doacao_campanha) AS doacao_campanha
      FROM (
               SELECT nome,
                      dizimo,
                      doacao_terenos,
                      doacao_missoes,
                      doacao_pam,
                      doacao_campanha,
                      data_referencia
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', 'start of year') AND date('now', 'start of year', '+1 month', '-1 day') 
           )
     WHERE (dizimo > 0) AND 
           (doacao_terenos > 0) AND 
           (doacao_missoes > 0) AND 
           (doacao_pam > 0) AND 
           (doacao_campanha > 0) 
     GROUP BY nome;


-- View: total_julho
DROP VIEW IF EXISTS total_julho;
CREATE VIEW total_julho AS
    SELECT nome,
           sum(dizimo) AS dizimo,
           sum(doacao_terenos) AS doacao_terenos,
           sum(doacao_missoes) AS doacao_missoes,
           sum(doacao_pam) AS doacao_pam,
           sum(doacao_campanha) AS doacao_campanha
      FROM (
               SELECT nome,
                      dizimo,
                      doacao_terenos,
                      doacao_missoes,
                      doacao_pam,
                      doacao_campanha,
                      data_referencia
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', 'start of year', '+6 month') AND date('now', 'start of year', '+7 month', '-1 day') 
           )
     WHERE (dizimo > 0) AND 
           (doacao_terenos > 0) AND 
           (doacao_missoes > 0) AND 
           (doacao_pam > 0) AND 
           (doacao_campanha > 0) 
     GROUP BY nome;


-- View: total_junho
DROP VIEW IF EXISTS total_junho;
CREATE VIEW total_junho AS
    SELECT nome,
           sum(dizimo) AS dizimo,
           sum(doacao_terenos) AS doacao_terenos,
           sum(doacao_missoes) AS doacao_missoes,
           sum(doacao_pam) AS doacao_pam,
           sum(doacao_campanha) AS doacao_campanha
      FROM (
               SELECT nome,
                      dizimo,
                      doacao_terenos,
                      doacao_missoes,
                      doacao_pam,
                      doacao_campanha,
                      data_referencia
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', 'start of year', '+5 month') AND date('now', 'start of year', '+6 month', '-1 day') 
           )
     WHERE (dizimo > 0) AND 
           (doacao_terenos > 0) AND 
           (doacao_missoes > 0) AND 
           (doacao_pam > 0) AND 
           (doacao_campanha > 0) 
     GROUP BY nome;


-- View: total_maio
DROP VIEW IF EXISTS total_maio;
CREATE VIEW total_maio AS
    SELECT nome,
           sum(dizimo) AS dizimo,
           sum(doacao_terenos) AS doacao_terenos,
           sum(doacao_missoes) AS doacao_missoes,
           sum(doacao_pam) AS doacao_pam,
           sum(doacao_campanha) AS doacao_campanha
      FROM (
               SELECT nome,
                      dizimo,
                      doacao_terenos,
                      doacao_missoes,
                      doacao_pam,
                      doacao_campanha,
                      data_referencia
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', 'start of year', '+4 month') AND date('now', 'start of year', '+5 month', '-1 day') 
           )
     WHERE (dizimo > 0) AND 
           (doacao_terenos > 0) AND 
           (doacao_missoes > 0) AND 
           (doacao_pam > 0) AND 
           (doacao_campanha > 0) 
     GROUP BY nome;


-- View: total_marco
DROP VIEW IF EXISTS total_marco;
CREATE VIEW total_marco AS
    SELECT nome,
           sum(dizimo) AS dizimo,
           sum(doacao_terenos) AS doacao_terenos,
           sum(doacao_missoes) AS doacao_missoes,
           sum(doacao_pam) AS doacao_pam,
           sum(doacao_campanha) AS doacao_campanha
      FROM (
               SELECT nome,
                      dizimo,
                      doacao_terenos,
                      doacao_missoes,
                      doacao_pam,
                      doacao_campanha,
                      data_referencia
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', 'start of year', '+2 month') AND date('now', 'start of year', '+3 month', '-1 day') 
           )
     WHERE (dizimo > 0) AND 
           (doacao_terenos > 0) AND 
           (doacao_missoes > 0) AND 
           (doacao_pam > 0) AND 
           (doacao_campanha > 0) 
     GROUP BY nome;


-- View: total_novembro
DROP VIEW IF EXISTS total_novembro;
CREATE VIEW total_novembro AS
    SELECT nome,
           sum(dizimo) AS dizimo,
           sum(doacao_terenos) AS doacao_terenos,
           sum(doacao_missoes) AS doacao_missoes,
           sum(doacao_pam) AS doacao_pam,
           sum(doacao_campanha) AS doacao_campanha
      FROM (
               SELECT nome,
                      dizimo,
                      doacao_terenos,
                      doacao_missoes,
                      doacao_pam,
                      doacao_campanha,
                      data_referencia
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', 'start of year', '+10 month') AND date('now', 'start of year', '+11 month', '-1 day') 
           )
     WHERE (dizimo > 0) AND 
           (doacao_terenos > 0) AND 
           (doacao_missoes > 0) AND 
           (doacao_pam > 0) AND 
           (doacao_campanha > 0) 
     GROUP BY nome;


-- View: total_outubro
DROP VIEW IF EXISTS total_outubro;
CREATE VIEW total_outubro AS
    SELECT nome,
           sum(dizimo) AS dizimo,
           sum(doacao_terenos) AS doacao_terenos,
           sum(doacao_missoes) AS doacao_missoes,
           sum(doacao_pam) AS doacao_pam,
           sum(doacao_campanha) AS doacao_campanha
      FROM (
               SELECT nome,
                      dizimo,
                      doacao_terenos,
                      doacao_missoes,
                      doacao_pam,
                      doacao_campanha,
                      data_referencia
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', 'start of year', '+9 month') AND date('now', 'start of year', '+10 month', '-1 day') 
           )
     WHERE (dizimo > 0) AND 
           (doacao_terenos > 0) AND 
           (doacao_missoes > 0) AND 
           (doacao_pam > 0) AND 
           (doacao_campanha > 0) 
     GROUP BY nome;


-- View: total_setembro
DROP VIEW IF EXISTS total_setembro;
CREATE VIEW total_setembro AS
    SELECT nome,
           sum(dizimo) AS dizimo,
           sum(doacao_terenos) AS doacao_terenos,
           sum(doacao_missoes) AS doacao_missoes,
           sum(doacao_pam) AS doacao_pam,
           sum(doacao_campanha) AS doacao_campanha
      FROM (
               SELECT nome,
                      dizimo,
                      doacao_terenos,
                      doacao_missoes,
                      doacao_pam,
                      doacao_campanha,
                      data_referencia
                 FROM entradas
                WHERE data_referencia BETWEEN date('now', 'start of year', '+8 month') AND date('now', 'start of year', '+9 month', '-1 day') 
           )
     WHERE (dizimo > 0) AND 
           (doacao_terenos > 0) AND 
           (doacao_missoes > 0) AND 
           (doacao_pam > 0) AND 
           (doacao_campanha > 0) 
     GROUP BY nome;


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

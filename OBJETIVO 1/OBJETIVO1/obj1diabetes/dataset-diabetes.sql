drop database if exists diabetesDataset;
create database diabetesDataset;
use diabetesDataset;

create table objetivo1Diabetes(
 id INT AUTO_INCREMENT PRIMARY KEY,
 glucemia_mgdL decimal(5,2),
 presionArterialSistolica_mmHg decimal(5,2),
 presionArterialDiastolica_mmHg decimal(5,2),
 nivelInsulina_uUmL decimal(5,2),
 indiceMasaCorporal_kgm2 decimal(5,2),
nivelCetonasUrina_mgdL decimal(5,2),
 polidipsia int,
 poliuria int,
 polifagia int,
 anticuerpos_betaPancreas int,
antecedentesFamiliares int,
 edad int,
 diagnostico varchar(150)
);
drop table objetivo1Diabetes;
select * from objetivo1Diabetes;



DELIMITER //
CREATE PROCEDURE generarDataDiabetes(cantidadRegistros int)
BEGIN
    -- Código del procedimiento almacenado aquí
   
	DECLARE contador INT DEFAULT 0;
   /* DECLARE limite INT DEFAULT 1000;*/
    
    DECLARE glucemia DECIMAL(5, 2);
    DECLARE presionSistolica DECIMAL(5, 2);
    DECLARE presionDiastolica DECIMAL(5, 2);
    DECLARE nivelInsulina DECIMAL(5, 2);
    DECLARE indiceMasaCorporal DECIMAL(5, 2);
	DECLARE	nivelCetonasUrina decimal(5,2);
	DECLARE	polidipsia int;
	DECLARE	poliuria int;
	DECLARE	polifagia int;
    DECLARE anticuerpos_betaPancreas INT;
    DECLARE antecedentesFamiliares INT;
    DECLARE edad INT;
    DECLARE resultado VARCHAR(150);
    DECLARE controlDiabetes INT;
   
  

		

    WHILE contador < cantidadRegistros DO
    
        -- Código a ejecutar dentro del bucle
        SET controlDiabetes=   FLOOR(RAND() * 3);
       


    IF controlDiabetes = 0 THEN
		-- Código a ejecutar si controlDiabetes es igual a 0
		SET glucemia = ROUND(70 + (RAND() * 40), 2);
		SET presionSistolica = ROUND(110 + (RAND() * 10), 2);
		SET presionDiastolica = ROUND(70 + (RAND() * 10), 2);
		SET nivelInsulina = ROUND(5 + (RAND() * 15), 2);
		SET indiceMasaCorporal = ROUND(18.5 + (RAND() * 6.4), 2);
		SET nivelCetonasUrina = ROUND(RAND() * 10, 2);
		SET polidipsia = FLOOR(RAND() * 2);
		SET poliuria = FLOOR(RAND() * 2);
		SET polifagia = FLOOR(RAND() * 2);
        SET anticuerpos_betaPancreas= 0;
		SET antecedentesFamiliares = FLOOR(RAND() * 2);
		SET edad = FLOOR(10 + RAND() * (70 - 10 + 1)) ;
		SET resultado = 'SIN DIABETES';

		INSERT INTO objetivo1Diabetes 
		(glucemia_mgdL, presionArterialSistolica_mmHg, presionArterialDiastolica_mmHg, nivelInsulina_uUmL,
		indiceMasaCorporal_kgm2, nivelCetonasUrina_mgdL, polidipsia, poliuria, polifagia
        ,anticuerpos_betaPancreas,antecedentesFamiliares, edad, diagnostico)
		VALUES (glucemia, presionSistolica, presionDiastolica, nivelInsulina, indiceMasaCorporal, nivelCetonasUrina, polidipsia, poliuria, polifagia,
        anticuerpos_betaPancreas,antecedentesFamiliares, edad, resultado);

	ELSEIF controlDiabetes = 1 THEN
		SET glucemia = ROUND(115 + (RAND() * 100), 2);
		SET presionSistolica = ROUND(110 + (RAND() * 60), 2);
		SET presionDiastolica = ROUND(70 + (RAND() * 50), 2);
		SET nivelInsulina = ROUND(RAND() * 5, 2) ;
        SET indiceMasaCorporal= ROUND(16 + RAND() * 19, 2);
		SET nivelCetonasUrina= ROUND(10 + RAND() * 17, 2);
        SET polidipsia =FLOOR(RAND() * 2);
        SET poliuria=FLOOR(RAND() * 2);
        SET polifagia=FLOOR(RAND() * 2);
         SET anticuerpos_betaPancreas= 1;
		/*SET antecedentesFamiliares = FLOOR(RAND() * 2);*/
        SET antecedentesFamiliares =0;
		SET edad =  FLOOR(10 + RAND() * (32 - 10 + 1)) ;
		SET resultado = 'DIABETES TIPO 1';

		INSERT INTO objetivo1Diabetes 
		(glucemia_mgdL, presionArterialSistolica_mmHg, presionArterialDiastolica_mmHg, nivelInsulina_uUmL,
		indiceMasaCorporal_kgm2, nivelCetonasUrina_mgdL, polidipsia, poliuria, polifagia,
        anticuerpos_betaPancreas,antecedentesFamiliares, edad, diagnostico)
		VALUES (glucemia, presionSistolica, presionDiastolica, nivelInsulina, indiceMasaCorporal, nivelCetonasUrina, polidipsia, poliuria, polifagia,
        anticuerpos_betaPancreas,antecedentesFamiliares, edad, resultado);

	ELSEIF controlDiabetes = 2 THEN
		SET glucemia = ROUND(126 + (RAND() * 100), 2);
		SET presionSistolica = ROUND(110 + (RAND() * 60), 2);
		SET presionDiastolica = ROUND(70 + (RAND() * 50), 2);
		SET nivelInsulina = ROUND(20 + (RAND() * 15), 2);
        /*SET nivelInsulina = ROUND(RAND() * 5, 2) ;*/
        /*SET indiceMasaCorporal= ROUND(16 + RAND() * 19, 2);*/  /*factor importante +*/
        /*SET indiceMasaCorporal=ROUND((RAND() * 4.5) + 14, 2);*/
		SET indiceMasaCorporal= ROUND(25 + RAND() * (80 - 25), 2) ;
		/*SET nivelCetonasUrina= ROUND(10 + RAND() * 17, 2);*/
        SET nivelCetonasUrina = ROUND(RAND() * 10, 2);
        SET polidipsia =FLOOR(RAND() * 2);
        SET poliuria=FLOOR(RAND() * 2);
        SET polifagia=FLOOR(RAND() * 2);
         SET anticuerpos_betaPancreas=0;
		/*SET antecedentesFamiliares = FLOOR(RAND() * 2);*/
        SET antecedentesFamiliares = 1;
		SET edad = FLOOR(32 + RAND() * (79 - 32 + 1));

		SET resultado = 'DIABETES TIPO 2';
        
        INSERT INTO objetivo1Diabetes 
		(glucemia_mgdL, presionArterialSistolica_mmHg, presionArterialDiastolica_mmHg, nivelInsulina_uUmL,
		indiceMasaCorporal_kgm2, nivelCetonasUrina_mgdL, polidipsia, poliuria, polifagia,
        anticuerpos_betaPancreas,antecedentesFamiliares, edad, diagnostico)
		VALUES (glucemia, presionSistolica, presionDiastolica, nivelInsulina, indiceMasaCorporal, nivelCetonasUrina, polidipsia, poliuria, polifagia,
        anticuerpos_betaPancreas,antecedentesFamiliares, edad, resultado);
	END IF;

        
       
      
        -- Incrementar el contador u otras operaciones
        SET contador = contador + 1;
    END WHILE;
END//
DELIMITER ;

SET max_execution_time = 60;
SET wait_timeout = 600;


drop procedure generarDataDiabetes;
CALL generarDataDiabetes(1000);
DELETE FROM objetivo1Diabetes WHERE id > 0;
ALTER TABLE objetivo1Diabetes AUTO_INCREMENT = 1;

select count(*) from objetivo1Diabetes;

use diabetesDataset;
SELECT 'id', 'glucemia_mgdL', 'presionArterialSistolica_mmHg', 'presionArterialDiastolica_mmHg', 'nivelInsulina_uUmL', 'indiceMasaCorporal_kgm2', 'nivelCetonasUrina_mgdL', 'polidipsia', 'poliuria', 'polifagia', 'anticuerpos_betaPancreas', 'antecedentesFamiliares', 'edad', 'diagnostico'
UNION
SELECT id, glucemia_mgdL, presionArterialSistolica_mmHg, presionArterialDiastolica_mmHg, nivelInsulina_uUmL, indiceMasaCorporal_kgm2, nivelCetonasUrina_mgdL, polidipsia, poliuria, polifagia, anticuerpos_betaPancreas, antecedentesFamiliares, edad, diagnostico
FROM objetivo1Diabetes 
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/diabetes-dataset18.csv'
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SHOW INDEXES FROM objetivo1Diabetes;


SHOW VARIABLES LIKE "secure_file_priv";


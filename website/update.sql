BEGIN TRANSACTION;

UPDATE pokedex SET type = json_set(type, '$.type1', 4) WHERE 
pokedex_nbr = 336 OR pokedex_nbr = 434 OR pokedex_nbr = 435 OR pokedex_nbr = 451
OR pokedex_nbr = 452 OR pokedex_nbr = 453 OR pokedex_nbr = 454 OR pokedex_nbr = 568
OR pokedex_nbr = 569 OR pokedex_nbr = 690 OR pokedex_nbr = 691 OR pokedex_nbr = 747
OR pokedex_nbr = 748 OR pokedex_nbr = 757 OR pokedex_nbr = 758;

UPDATE pokedex SET type = json_set(type, '$.type2', 4) WHERE 
pokedex_nbr = 406 OR pokedex_nbr = 407 OR pokedex_nbr = 543 OR pokedex_nbr = 544
OR pokedex_nbr = 545 OR pokedex_nbr = 590 OR pokedex_nbr = 591;
COMMIT;

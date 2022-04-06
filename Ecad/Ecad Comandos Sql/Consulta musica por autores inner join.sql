SELECT * FROM tbl_Musicas
INNER JOIN Tbl_Musicas_Autores
ON tbl_Musicas.Id_musica = Tbl_Musicas_Autores.Id_musica
INNER JOIN tbl_Autores
ON tbl_Autores.Id_autor = Tbl_Musicas_Autores.Id_autor
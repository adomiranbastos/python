/****** Script do comando SelectTopNRows de SSMS  ******/
SELECT TOP (1000) [Id_autor]
      ,[Nome_autor]
      ,[Nacionalidade]
  FROM [dbo].[tbl_Autores] where Nacionalidade= 'Brasileira'
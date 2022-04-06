USE [DatabaseEcad]


INSERT INTO [dbo].[tbl_Execucao]
           ([Id_musica]
           ,[Data_execucao])
     VALUES
           (1, GETDATE() AT TIME ZONE 'UTC' AT TIME ZONE 'E. South America Standard Time')




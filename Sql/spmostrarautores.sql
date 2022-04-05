Use DatabaseEcad

--procedimento mostrar
create proc spmostrar_tbl_Autores
as
Select * from tbl_Autores
order by Id_autor desc
go
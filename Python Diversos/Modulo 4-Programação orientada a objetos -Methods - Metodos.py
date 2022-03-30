#Métodos: Os métodos contêm a funcionalidade do objeto. Eles são definidos na classe.

class BibliotecaLivro(object):
    """
    A library book.
    """
         
    def __init__(self, titulo, autor, pub_ano, num_telefone):
        self.titulo = titulo
        self.autor = autor
        self.ano = pub_ano
        self.num_telefone = num_telefone
    
    """
    Methods for BibliotecaLivro
    """  

    # Returns the titulo and autor information of the book as a string
    def titulo_e_autor(self):
        return "{} {}: {}".format(self.autor[1], self.autor[0], self.titulo) 
    
    # Prints all information associated with a book in this format
    def __str__(self): #make sure that __str__ returns a string!
        return "{} {} ({}): {}".format(self.autor[1], self.autor[0], self.year, self.titulo) 

    # Returns a string representation of the book with it' titulo and num_telefone   
    def __repr__(self): 
        return "<Book: {} ({})>".format(self.titulo, self.num_telefone)
        
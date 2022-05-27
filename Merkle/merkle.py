#!/usr/bin/python3
importar  hashlib , sistema
    
clase  MerkleTreeNode :
    def  __init__ ( auto , valor ):
        uno mismo izquierda  =  Ninguno
        uno mismo derecho  =  ninguno
        uno mismo valor  =  valor
        uno mismo hashValue  =  hashlib . sha256 ( valor . codificar ( 'utf-8' )). resumen hexadecimal ()
    
def  buildTree ( hojas , f ):
    nodos  = []
    para  i  en  hojas :
        nodos _ agregar ( MerkleTreeNode ( i ))

    mientras que  len ( nodos ) ! = 1 :
        temperatura  = []
        para  i  en el  rango ( 0 , len ( nodos ), 2 ):
            nodo1  =  nodos [ i ]
            si  i + 1  <  len ( nodos ):
                nodo2  =  nodos [ i + 1 ]
            más :
                temperatura _ agregar ( nodos [ i ])
                romper
            F. _ write ( "Left child:" +  node1 . value  +  "| Hash:"  +  node1 . hashValue  + " \n " )
            F. _ write ( "Hijo derecho:" +  nodo2 . valor  +  "| Hash:"  +  nodo2 . hashValue  + " \n " )
            concatenatedHash  =  node1 . valor hash + nodo2  . valor hash 
            padre  =  MerkleTreeNode ( concatenatedHash )
            padre _ izquierda  =  nodo1
            padre _ derecha  =  nodo2
            F. _ write ( "Parent(concatenación de " +  node1 . value  +  " y "  +  node2 . value  +  ") : "  + parent . value  +  " | Hash : "  +  parent . hashValue  + " \n " )
            temperatura _ agregar ( padre )
        nodos  =  temperatura 
     nodos de retorno [ 0 ]

cadena de entrada  =  sys . arg [ 1 ]
hojasCadena  =  cadenaEntrada [ 1 : largo ( CadenaEntrada ) - 1 ]
hojas  =  cadenahojas . dividir ( "," )
f  =  abierto ( "merkle.tree" , "w" )
root  =  buildTree ( hojas , f )
F. _ cerrar ()
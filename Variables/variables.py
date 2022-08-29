#conversiones
a = 20
b = 50
nombre = 'marco cruzado'
print(type(a))
print(type(nombre))
print("la sumas es :" + str(a+b))

a= str(a)
b= str(b)
resultado = a+b

print("ahora el valor de a es  : "+ str(type(a)))
print("ahora el valor de b es : " + str(type(b)))
print("ahora la suma de a + b es : "+ resultado)

#cadenas de texto
texto = 'hola bienvemido a python'

print(texto[5:])
print(texto[-5:])
print(texto.upper())
print(texto.lower())
print(texto.capitalize())
cadena = "java,selenium,php,seleniun"
print(cadena.split(','))

#imprimir cadenas

name = 'juan'
last_name = 'cruzado'
country = 'Lima'
print("Tu nombre completo es {}, {} y actualmente estas viviendo en {}".format(last_name, name, country))
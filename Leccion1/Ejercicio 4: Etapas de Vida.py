"""
Ejercicio 4: Etapas de Vida

Haremos un programa que cuando el usuario
ingrese su edad le diga, o imprima la etapa de
su vida en una breve oración:
0 a 10 = La infancia es increible y bella.
10 a 19 = Tienes muchos cambios, mucho que estudiar.
20 a 29 = Amor y comienza el trabajo.
Para las siguientes etapas, deberás completarlo...

"""

edad = int(input("Digite su edad: "))
resultado = None
if 0 <= edad < 10:
    resultado = "La infancia es increible y bella."
elif 10 <= edad < 20:
    resultado = "Tienes muchos cambios, mucho que estudiar."
elif 20 <= edad < 30:
    resultado = "Amor y comienza el trabajo."
elif 30 <= edad < 40:
    resultado = "La familia se agranda y asenso en el trabajo!."
elif 40 <= edad < 50:
    resultado = "Lo chicos no paran de crecer, se renueva el hogar, bodas de plata."
elif 50 <= edad < 60:
    resultado = "Los chicos ya no son chicos, mas espacio en la casa."
elif 60 <= edad < 70:
    resultado = "Lo chicos no paran de crecer, se renueva el hogar."
elif 70 <= edad < 80:
    resultado = "Ya somos abuelos felices y orgullosos, bodas de oro."
else:
    resultado = "Etapa de la vida no registrada"
print(f"Tu edad es: {edad}, {resultado}")
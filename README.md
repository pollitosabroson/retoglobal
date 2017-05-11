# Prueba

Para correr el siguiente proyecto se debe de tener instalado lo siguiente

  - [Python]
  - [MySql]
  - [VirtualEnv] o [VirtualEnvWraprer]
 
1. Primero se tien que crear un entorno virtual dependiendo del el entorno virtual que uses puede ser lo siguiente:
  - VirtualEnv
    ```sh
    $ virtualenv ENV
    ```
    
  - VirtualEnvWraprer
    ```sh
    $ mkvirtualenv env1
    ```
2. Dependiendo del entorno virutal se deben de configurar las siguientes variables de entorno:
```sh
    DB_NAME='NameDB'
    DB_USER='NameUser'
    DB_PASSWORD="PASSWORD"
    DB_HOST='HOST'
```
3. Una vez dentro de nuestro entorno virtual se ejecuta el siguiente comando:

```sh
    $ pip install -r requirements/requirements.txt
```
4. Ejecutar las migraciones:
```sh
    $ python manage.py migrate
```
5. Agregar los Fixtures que contiene los dos de las tablas de Genero y de Hobbies:
```sh
    $ python manage.py loaddata genres
    $ python manage.py loaddata hobbies
```
6. Listo ya esta el sistema para poder usarse

## Creación de usuarios random

1. para  la creación de usuario randmon se debe ejecutar el siguiente comando:
```sh
    $ python manage.py random_user NUMERO_DE_USUARIOS_A_CREAR
```
Ejemplo
```sh
    $ python manage.py random_user 10
```

## End-Point del filtrado de usuarios
A continuacion una breve explicación de los filtros de usuarios de los parametros get:
| Nombre | Función |
| ------ | ------ |
| same_sex | String que regresa filtrado del mismo sexo que se le indica |
| age | Entero que regresa los usuarios que tengan la edad exacta que se envia |
| range_age | Entero que regresa los usuarios que esten dentro del rango de la edad, con una diferencia de edad de 3 años [Hardcodeada] |
| hobbies | Array que regresa los usuarios que tengan los mismos hobbies.|
| distinc_sex | String que regresa el sexo contrario por el cual se esta filtrando |

Example:
```sh
    http://localhost:8000/users?hobbies=natacion,correr&range_age=22&diferent_sex=male
```

Regresa lo siguiente:

```json
    [
        {
            "id":2,
            "age":22,
            "genre":"female",
            "hobbies":[
                {
                    "name":"Natacion"
                },
                {
                    "name":"Comer"
                }
            ],
            "last_name":"simpson",
            "name":"pauline"
        }
    ]
```
## End-Point para mostrar el perfil de un usuario

End-Point diseñado para mostrar el Perfil de un usuario
```sh
    http://localhost:8000/users/ID_USUARIO
```
Ejemplo:
```sh
    http://localhost:8000/users/1
```

Regresa lo siguiente:
```json
    {
    "id":1,
    "age":12,
    "genre":"male",
    "hobbies":[
        {
            "name":"Correr"
        },
        {
            "name":"Caminar"
        }
    ],
    "last_name":"Rosales",
    "name":"Alejandro"
}
```
## End-Point para ver usuarios que tengan un match con un perfil

End-Point diseñado para mostrar los usuarios que tengan cierta similitudes con un usario:
```sh
    http://localhost:8000/users/ID_USUARIO/match-users
```
Ejemplo:
```sh
    http://localhost:8000/users/1/match-users
```

Regresa lo siguiente:
```json
   [
        {
            "id":258,
            "age":25,
            "genre":"female",
            "hobbies":[
                {
                    "name":"Correr"
                },
                {
                    "name":"Estudiar"
                }
            ],
            "last_name":"hoffman",
            "name":"kenneth"
        },
        {
            "id":373,
            "age":24,
            "genre":"female",
            "hobbies":[
                {
                    "name":"Natacion"
                },
                {
                    "name":"Correr"
                }
            ],
            "last_name":"gomez",
            "name":"terry"
        }
    ]
```

## End-Point Para ver todos los usuarios
End-Point diseñado para mostrar todos los usuarios:
```sh
    http://localhost:8000/users
```
Ejemplo:
```sh
    http://localhost:8000
```

Regresa lo siguiente:
```json
   [
        {
            "id":258,
            "age":25,
            "genre":"female",
            "hobbies":[
                {
                    "name":"Correr"
                },
                {
                    "name":"Estudiar"
                }
            ],
            "last_name":"hoffman",
            "name":"kenneth"
        },
        {
            "id":373,
            "age":24,
            "genre":"female",
            "hobbies":[
                {
                    "name":"Natacion"
                },
                {
                    "name":"Correr"
                }
            ],
            "last_name":"gomez",
            "name":"terry"
        }
    ]
```

## Correr pruebas

Para ejecutar las pruebas se debe de correr los test:
```sh
    $ python manage.py test
```
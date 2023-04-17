#
# Test Squadmakers (Backend)
Por: Leonardo Patiño Rodriguez
## &nbsp; [![pyVersion38](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/download/releases/3.8/)

## Tecnologías y arquitectura del proyecto
<p align="justify">
<strong>Arquitectura Hexagonal</strong>
</p>
<p align="justify">
El principal motivo para separar la aplicación en dos capas (joke:challenge, math_challenge) es que cuente con su propia responsabilidad. De esta manera consigue desacoplar capas de nuestra aplicación permitiendo que evolucionen de manera aislada. Además, tener el sistema separado por responsabilidades nos facilitará:
</p>

- La reutilización y mantenibilidad
- Pruebas unitarias
- Más tolerantes a cambios (Responsabilidad única)
- Desacoplamiento

## Uso de buenas prácticas.
<p align="justify">
<strong>Implementación de principios solid</strong>
</p>

- Principio de Responsabilidad Única
- Principio de Inversión de Dependencias

<p align="justify">
<strong>Flake8 - Isort</strong>
</p>

<p align="justify">
Implementación de flake8 e Isort para estandarización y limpieza de código. 
</p>

## Patrones de diseño utilizados.
<p align="justify">
<strong>Patrón de arquitectura REST</strong>
</p>
<p align="justify">
Se utiliza el patrón de serialización para convertir los modelos de Django en formatos de datos que se pueden enviar a través de una API web. DRF proporciona serializadores, que son clases que convierten los modelos de Django en formatos como JSON o XML.
</p>

<p align="justify">
<strong>Patrón de serialización</strong>
</p>
<p align="justify">
Se utiliza una estructura de URL clara y jerárquica para representar los recursos, y HTTP para definir las acciones que se realizan en esos recursos.
</p>

<p align="justify">
<strong>Patrón de controlador de vista</strong>
</p>
<p align="justify">
Se utiliza el patrón de controlador de vista, que separa la lógica de presentación de la lógica de negocio. Los controladores de vista de DRF manejan las solicitudes HTTP y la lógica de negocio asociada con ellas, como la validación de datos y la autorización.
</p>

<p align="justify">
<strong>Patròn 3 Capas</strong>
</p>
<p align="justify">
Un patrón común como la arquitectura de 3 niveles, donde la aplicación se divide en capa de presentación, capa lógica y capa de datos.
</p>

<p align="justify">
<strong>Patròn separación de intereses (SoC)</strong>
</p>
<p align="justify">
Se divide la aplicación en componentes independientes que se centran en un aspecto específico de la funcionalidad de la aplicación.es decir separar la lógica del negocio de la lógica de presentación, lo que permite que los componentes de la aplicación sean más mantenibles y escalables, en este caso, la capa services.py actúa como una capa intermedia entre las vistas (interfaz de usuario) y los modelos (lógica del negocio). 
</p>

<p align="justify">
<strong>Patròn Connector</strong>
</p>
<p align="justify">
Este patròn se divide en dos partes principales: el conector y el componente. El conector actúa como una interfaz que conecta los componentes y permite que se comuniquen entre sí. Por su parte, el componente es la unidad funcional que realiza una tarea específica dentro del sistema.
</p>

## Documentación Swagger y Redoc

http://localhost:8000/swagger/
http://localhost:8000/redoc/

<div align="center">
	<img height="700" src="https://leoesleoesleo.github.io/imagenes/swagger_challenge.png">
</div> 

## Coverage

<div align="center">
	<img height="600" src="https://leoesleoesleo.github.io/imagenes/coverage_challenge.png">
</div> 
<div align="center">
	<img height="300" src="https://leoesleoesleo.github.io/imagenes/test_challenge.png">
</div> 

## Decisiones que se tomaron en el proyecto

<p align="justify">
Inicialmente se elige el framework DRF dado que sigue las mejores prácticas de desarrollo de software, lo que asegura que el código sea limpio, escalable y fácil de mantener.
</p>

<p align="justify">
Se opta por utilizar MySQL dado que es uno de los motores de base de datos más populares y ampliamente utilizados en la industria, por lo que es compatible con una amplia variedad de herramientas, aplicaciones y frameworks.
</p>

<p align="justify">
Se opta por implementar una arquitectura que permita desacoplar las aplicaciones, como se menciona al inicio de este documento.
</p>

<p align="justify">
Se opta por implementar patrón de diseño conector, que proporciona una abstracción para que los componentes se comuniquen sin tener que preocuparse por los detalles de implementación, en este caso el consumo de las APIS con la librería requests.
</p>

<p align="justify">
Para evitar problemas de compatibilidad y configuración se opta por dockerizar la aplicaciòn
</p>


## Manual de instalación

### Pasos para Docker

- Clonar repositorio
	```
	git clone https://github.com/leoesleoesleo/03_project_.git
	```

- Levantar contenedor Docker
	```
	docker-compose -p challenge_project up --build
	```

- Entrar al contenedor en modo bash (opcional)
	```
	docker-compose -p challenge_project run web bash
	```

### Pasos para entorno virtual

- Crear entorno

    Ejemplo anaconda
	```
	conda create -n env_project_challenge python=3.8
	```
	```
	conda activate env_project_challenge
	```
    Ejemplo virtualenv Linux
    ```
	pip install virtualenv
	```
	```
	python3 -m venv env_project_challenge
	```
	```
	source env_project_challenge/bin/activate
	```
	
- Navegar hasta la carpeta del proyecto en la carpeta requirements para instalar dependencias
    ```
    pip install -r requirements.txt
    ```

### Pasos generales

- Crear archivo de variables de entorno .env basado en .env.example

- Migrar la base de datos, en la altura del archivo manage.py
    ```
   python manage.py makemigrations
    ```
    ```
   python manage.py migrate
    ``` 

- Ejecutar pruebas unitarias (Opcional)
   ```
   pytest -v  
    ``` 

- Validar cobertura de la aplicación (Opcional)
    ```
   coverage run -m pytest -v -p no:cacheprovider --junitxml=junit/test-results.xml --cov=. --cov-report=xml --cov-report=html  
    ```    
    
- Levantar servicio
    ```
   python manage.py runserver
    ```

## Pruebas Postman

<div align="center">
	<img height="500" src="https://leoesleoesleo.github.io/imagenes/get_joke.png">
</div> 
<div align="center">
	<img height="500" src="https://leoesleoesleo.github.io/imagenes/post_joke.png">
</div>
<div align="center">
	<img height="500" src="https://leoesleoesleo.github.io/imagenes/put_joke.png">
</div>
<div align="center">
	<img height="500" src="https://leoesleoesleo.github.io/imagenes/delete_joke.png">
</div>
<div align="center">
	<img height="500" src="https://leoesleoesleo.github.io/imagenes/lcm_math.png">
</div>
<div align="center">
	<img height="500" src="https://leoesleoesleo.github.io/imagenes/plus_one_math.png">
</div>

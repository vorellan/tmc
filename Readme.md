# Cálculo tasa TMC



### Instalación 🔧

1.  Clonar repositorio

2.  Crear entorno virtual

```
virtualenv env -p python3

```

3.  Activar entorno virtual

```
activate env

```

4.  Instalar dependencias

```
pip install -r requirements.txt

```

5.  Correr servidor

```
python manage.py runserver 0.0.0.0:8080

```

## Ejemplos de ingreso de datos en el formulario ⚙️

- monto_uf (decimal): ej: 28345,43
- plazo (días): ej: 30
- fecha (año-mes-día): ej: 2020-01-16


### Supuestos ⌨️

- Una vez identificada la tmc correspondiente a la fecha se aplico una tasa de interés simple: Monto x tmc x días
- Se asume el ultimo valor para fechas superiores a 2020-06-16, dado que hay muchos valores para ella, y todos sin fecha limite


Saludos 🤓.


# PDFFormFillerDB
### Rellenar formularios con una db mysql


# Instalacion
## **En el archivo data.sql la base de datos se crea por defecto como "reports" y luego se crea la tabla "forms".**


#### en el archivo example.env estan las variables que se necesitan. crea un archivo **.env** , copie y pegue lo de abajo. solo modifique username y password con su login correspondiente. 

```bash
        export DATABASE_HOST = "localhost"
        export DATABASE_NAME = "reports"
        export DATABASE_USERNAME = "root"
        export DATABASE_PASSWORD = ""
        
        export FILENAME = "formulario nueva instalacion.pdf"
```
    
    
## Dependencias
    pip install -r requirements.txt

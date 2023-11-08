# ChallengeMM_ENVIRONMENT

este challenge cuantiza la temperatura, humedad y ozono obtenida con el movil

# DESCRIPCION y FIABILIDAD
ENVIRONMENT es un challenge que piden al usuario hacer una captura de tipo geolocation para comprobar que se encuentra en un lugar concreto
el challenge obtiene la temperatura cuantizada , la humedad cuantizada y el ozono cuantizado
el challenge tiene una fiabilidad media porque el usuario puede saber los parametros del lugar pero  pero es muy dificil forzar el resultado del movil. 

# FUNCIONAMIENTO:
cada medida se cuantiza en tramos de diferente tamano t se ofrece un resultado de 3 digitos (uno por cada medida)


# requisitos:
la variable de entorno **SECUREMIRROR_CAPTURES** debe existir y apuntar al path donde el server bluetooth deposita las capturas
el fichero de captura se debe llamar "capture.env".

Hay una variable en el challenge  llamada **"DEBUG_MODE"** que la puedes cambiar a True o False. En caso True en lugar del fichero capture.env se usa test.env y ademas no se borra el fichero capture.env despues de procesar. 

ejemplo de config json
```json
{
"FileName": "challenge_loader_python.dll",
"Description": "check environmen",
"Props": {
  "module_python": "environment",
  "validity_time": 3600,
  "refresh_time": 10,
  "interactionText": "Por favor haz una captura de datos de environment",
  },
"Requirements": "environment sensors" 
}
```

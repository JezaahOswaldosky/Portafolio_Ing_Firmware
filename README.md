# Documentación de Firmware
## 1. DESCRIPCION GENERAL
_Nombre del Proyecto: Iluminación para Pasillos_
_Versión del Firmware: V.0.1_
_Autor(es): Jesus Osvaldo Sandoval S._
_Fecha: 09/10/2026_
_Objetivo del Hardware: Proporcionar alumbrado en un pasillo utilizando dos interruptores y el microcontrolador ESP32._ 

Descripción:
Breve explicación de lo que hace el firmware.
##2. Hardware
Microcontrolador / SoC:
Periféricos utilizados (UART, SPI, I2C, GPIO, etc.):
Componentes externos (sensors, memory, actuators, etc.):
##3. Estructura del Firmware
Explicar cómo está organizado el código Firmware:
Ejemplo de directorios:
/src
   main.c
   module1.c
   module2.c
/drivers
   uart_driver.c
   spi_driver.c
##4. Build Instructions
IDE / Toolchain: Espressif IDE
Compiler: 

Build Steps: 
1. Open project
2. Build firmware
3. Flash to device
5. Firmware 
Explicar el flujo de trabajo de la función main del firmware.
Ejemplo:
1. Inicializar el hardware
2. Lee sensores
3. Procesa los datos
4. Envía resultados por comunicación serial o mostrar en displays
6. Funciones 
Explicar el funcionamiento de cada función a detalle. Tipo de datos de entrada, cantidad entradas, y cantidad de salidas. 
Explicar en diagrama de flujo cada bloque o modulo. 
##6. Interfaces / Comunicación 
Describe los protocolos de comunicación utilizados: 
Ejemplo:
Configuración UART:
Tasa de Baud:
Formato de los datos:
Mensaje (Ejemplo):
##7. Problemas/fallos conocidos 
Enlistar las limitaciones o bugs encontrados en el firmware.
##8. Futuras mejoras
Enlistar mejoras o características futuras.  
##9. Imágenes de funcionamiento
Colocar imágenes de funcionamiento del Firmware/Hardware.  

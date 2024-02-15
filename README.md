# CONSULTA A LA API DEL BCRA

El scrit en el archivo api-bcra.py permite realizar consultas a la API del Banco Central de la República Argentina (BCRA) para obtener información sobre la cotizacion de USD. Utiliza el endpoint https://api.estadisticasbcra.com/USD (a modo de ejemplo) para recuperar datos históricos relacionados con la base monetaria del país. 
Al final de este docomento detallo todos los endpoints disponibles para consultar.

# Requisitos
+ Python 3.x
+ Biblioteca requests de Python. Puede instalarse mediante el comando pip install requests.

# Configuración
Antes de ejecutar el script, necesitarás obtener un token de autorización de la API del BCRA. Este token se adquiere registrándose en el sitio oficial de estadísticas del BCRA y es necesario para autenticar las solicitudes a la API. Su validez es por un año.

Link de registro: http://estadisticasbcra.com/api/registracion

# Uso
+ Clona o descarga este repositorio en tu sistema local.
+ Asegurate de tener instalada la biblioteca requests.
+ Abri el script y reemplaza 'tu_token_AQUI' con tu token de autorización que obtuviste.

# Respuesta
La API devuelve un array de objetos JSON, donde cada objeto contiene dos claves: d para la fecha (en formato MySQL YYYY-MM-DD) y v para el valor de la base monetaria en esa fecha.

# Limitaciones
Tené en cuenta que la API del BCRA permite un máximo de 100 consultas diarias por token.

# Base de datos disponibles
+ http://api.estadisticasbcra.com/milestones : eventos relevantes (presidencia, ministros de economía, presidentes del BCRA, cepo al dólar)
+ http://api.estadisticasbcra.com/base : base monetaria
+ http://api.estadisticasbcra.com/base_usd: base monetaria dividida USD
+ http://api.estadisticasbcra.com/reservas : reservas internacionales
+ http://api.estadisticasbcra.com/base_div_res : base monetaria dividida reservas internacionales
+ http://api.estadisticasbcra.com/usd : cotización del USD
+ http://api.estadisticasbcra.com/usd_of : cotización del USD Oficial
+ http://api.estadisticasbcra.com/cuentas_corrientes : cuentas corrientes
+ http://api.estadisticasbcra.com/cajas_ahorro : cajas de ahorro
+ http://api.estadisticasbcra.com/plazo_fijo : plazos fijos
+ http://api.estadisticasbcra.com/otros_depositos : otros depositos
+ http://api.estadisticasbcra.com/tasa_int_dep : tasa de interés por depósitos
+ http://api.estadisticasbcra.com/tasa_badlar : tasa BADLAR
+ http://api.estadisticasbcra.com/tasa_baibar : tasa BAIBAR
+ http://api.estadisticasbcra.com/cer : CER
+ http://api.estadisticasbcra.com/uva : UVA
+ http://api.estadisticasbcra.com/uvi : UVI
+ http://api.estadisticasbcra.com/m2_privado_variacion_mensual : M2 privado variación mensual
+ http://api.estadisticasbcra.com/var_usd_vs_usd_of : porcentaje de variación entre la cotización del USD y el USD oficial
+ http://api.estadisticasbcra.com/lebac : LEBACs
+ http://api.estadisticasbcra.com/lebac_nominal : LEBACs (Nominal)
+ http://api.estadisticasbcra.com/circulacion_monetaria : circulación monetaria
+ http://api.estadisticasbcra.com/billetes_y_monedas : billetes y monedas
+ http://api.estadisticasbcra.com/efectivo_en_ent_fin : efectivo en entidades financieras
+ http://api.estadisticasbcra.com/depositos_cuenta_ent_fin : depositos de entidades financieras en cuenta del BCRA
+ http://api.estadisticasbcra.com/var_usd_anual : variación anual del dólar (porcentaje de variación de la cotización del dólar un año despues a la cotización de la fecha indicada)
+ http://api.estadisticasbcra.com/var_usd_of_anual : variación anual del dólar oficial (porcentaje de variación de la cotización del dólar oficial un año despues a la cotización de la fecha indicada)
+ http://api.estadisticasbcra.com/var_merval_anual : variación anual del MERVAL (porcentaje de variación del MERVAL un año despues al la cotización de la fecha indicada)
+ http://api.estadisticasbcra.com/merval : MERVAL
+ http://api.estadisticasbcra.com/merval_usd : MERVAL dividido cotización del USD


Espero que les haya sido de utilidad!

Emiliano Urrutia
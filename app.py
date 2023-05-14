from flask import Flask, render_template, request
import psycopg2


app = Flask(__name__)
app.debug = True

# # Define the connection parameters
# conn_params = {
#     "host": "172.24.100.8",
#     "port": "1433",
#     "database": "MDMCONTROLPROCESO",
#     "user": "sa",
#     "password": "sa"
# }

# # Create a connection object
# conn = psycopg2.connect(**conn_params)

# cursor = conn.cursor()


@app.route('/')
def home():
    return render_template('acceso.html')


@app.route('/insertar_acceso', methods=['POST'])
def insertar_acceso():
    # Obtener los datos del formulario HTML
    codigoAcceso = request.form['codigoAcceso']
    integrado = request.form['integrado']
    usuario = request.form['usuario']
    clave = request.form['clave']
    claveHuellaDigital = request.form['claveHuellaDigital']
    certificadoDigital = request.form['certificadoDigital']
    fechaIngreso = request.form['fechaIngreso']
    usuarioIngreso = request.form['usuarioIngreso']

    # Insertar los datos en la base de datos
    # cursor.execute("INSERT INTO mdd.mcpTbAcceso (codigoAcceso, integrado, usuario, clave, claveHuellaDigital, certificadoDigital, fechaIngreso, usuarioIngreso) VALUES (?,?,?,?,?,?,?,?)",
    #                (codigoAcceso, integrado, usuario, clave, claveHuellaDigital, certificadoDigital, fechaIngreso, usuarioIngreso))
    # conn.commit()

    return render_template('tipo_acceso.html')


@app.route('/insertar_tipo_acceso', methods=['POST'])
def insertar_tipo_acceso():
    codigoTipoAcceso = request.form['codigoTipoAcceso']
    accesoFuente = request.form['accesoFuente']
    accesoDireccion = request.form['accesoDireccion']
    accesoRemoto = request.form['accesoRemoto']

    # # Insertar el registro en la base de datos
    # cursor.execute("INSERT INTO mcpTbTipoAcceso (codigoTipoAcceso, accesoFuente, accesoDireccion, accesoRemoto) VALUES (%s, %s, %s, %s)", (codigoTipoAcceso, accesoFuente, accesoDireccion, accesoRemoto))

    # # Confirmar los cambios en la base de datos
    # conn.commit()

    # # Cerrar la conexión a la base de datos
    # cursor.close()
    # conn.close()

    # Redirigir a la página de éxito
    return render_template('home.html')


@app.route('/file_type', methods=['POST'])
def file_type():
    selected_option = request.form['options']
    if selected_option == 'archivo':
        print('-----entraaa------')
        return render_template('archivo.html')
    return render_template('base_datos.html')


@app.route('/insertar_archivo', methods=['POST'])
def insertar_archivo():
    codigoArchivo = request.form['codigoArchivo']
    descripcionArchivo = request.form['descripcionArchivo']
    nombreGestorConexion = request.form['nombreGestorConexion']
    codigoTipoArchivo = request.form['codigoTipoArchivo']
    nombreLogico = request.form['nombreLogico']
    nombreLogicoProcesado = request.form['nombreLogicoProcesado']
    nombreLogicoCompresion = request.form['nombreLogicoCompresion']
    patronNombreArchivo = request.form['patronNombreArchivo']
    requiereCompresion = request.form['requiereCompresion']
    requiereDescompresion = request.form['requiereDescompresion']
    claveCompresion = request.form['claveCompresion']
    validacionInterna = request.form['validacionInterna']
    criterioProcesado = request.form['criterioProcesado']
    sentenciaValidacion = request.form['sentenciaValidacion']
    separadorColumna = request.form['separadorColumna']
    filaValidacion = request.form['filaValidacion']
    columnaValidacion = request.form['columnaValidacion']
    posicionInicio = request.form['posicionInicio']
    posicionFin = request.form['posicionFin']
    indicadorEliminarArchivoOrigen = request.form['indicadorEliminarArchivoOrigen']
    formatoArchivo = request.form['formatoArchivo']
    delimitadorCabecera = request.form['delimitadorCabecera']
    saltoFila = request.form['saltoFila']
    cabeceraPrimeraFila = request.form['cabeceraPrimeraFila']
    fuenteInformacion = request.form['fuenteInformacion']
    disponible = request.form['disponible']
    fechaUltimaActualizacion = request.form['fechaUltimaActualizacion']
    diasVigencia = request.form['diasVigencia']
    fechaCaducidad = request.form['fechaCaducidad']
    fechaIngreso = request.form['fechaIngreso']
    usuarioIngreso = request.form['usuarioIngreso']

    # cursor.execute("INSERT INTO mcpTbArchivo(codigoArchivo, descripcionArchivo, nombreGestorConexion, codigoTipoArchivo, nombreLogico, nombreLogicoProcesado, nombreLogicoCompresion, patronNombreArchivo, requiereCompresion, requiereDescompresion, claveCompresion, validacionInterna, criterioProcesado, sentenciaValidacion, columnaValidacion,separadorColumna, filaValidacion, posicionInicio, posicionFin, indicadorEliminarArchivoOrigen, formatoArchivo, delimitadorCabecera, saltoFila, cabeceraPrimeraFila, fuenteInformacion, disponible, fechaUltimaActualizacion, diasVigencia, fechaCaducidad, fechaIngreso, usuarioIngreso) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
    #                (codigoArchivo, descripcionArchivo, nombreGestorConexion, codigoTipoArchivo, nombreLogico, nombreLogicoProcesado, nombreLogicoCompresion, patronNombreArchivo, requiereCompresion, requiereDescompresion, claveCompresion, validacionInterna, criterioProcesado, sentenciaValidacion, separadorColumna, columnaValidacion, filaValidacion, posicionInicio, posicionFin, indicadorEliminarArchivoOrigen, formatoArchivo, delimitadorCabecera, saltoFila, cabeceraPrimeraFila, fuenteInformacion, disponible, fechaUltimaActualizacion, diasVigencia, fechaCaducidad, fechaIngreso, usuarioIngreso))

    # conn.commit()
    # conn.close()
    return render_template('archivo_proceso.html')


@app.route('/insertar_archivo_proceso', methods=['POST'])
def insertar_archivo_proceso():
    codigoProceso = request.form['codigoProceso']
    codigoServidor = request.form['codigoServidor']
    codigoArchivo = request.form['codigoArchivo']
    codigoDirectorio = request.form['codigoDirectorio']
    codigoTipoAcceso = request.form['codigoTipoAcceso']
    codigoAcceso = request.form['codigoAcceso']
    flujoAcceso = request.form['flujoAcceso']
    fechaIngreso = request.form['fechaIngreso']
    usuarioIngreso = request.form['usuarioIngreso']

    # # Conectar con la base de datos
    # conn = psycopg2.connect(
    #     host='localhost', dbname='nombre_db', user='nombre_usuario', password='contraseña')

    # # Crear cursor y ejecutar la consulta de inserción
    # cursor = conn.cursor()
    # cursor.execute("INSERT INTO mdd.mcpTbTabla (codigoProceso, codigoServidor, codigoArchivo, codigoDirectorio, codigoTipoAcceso, codigoAcceso, flujoAcceso, fechaIngreso, usuarioIngreso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
    #                (codigoProceso, codigoServidor, codigoArchivo, codigoDirectorio, codigoTipoAcceso, codigoAcceso, flujoAcceso, fechaIngreso, usuarioIngreso))

    # # Confirmar los cambios en la base de datos y cerrar la conexión
    # conn.commit()
    # conn.close()

    # Redirigir a una página de éxito
    return ('exito!')


@app.route('/insertar_base_datos', methods=['POST'])
def insertar_base_datos():
    # Obtener los datos del formulario
    codigoBaseDatos = request.form['codigoBaseDatos']
    codigoServidor = request.form['codigoServidor']
    codigoMotorBaseDatos = request.form['codigoMotorBaseDatos']
    nombreBaseDatos = request.form['nombreBaseDatos']
    nombreInstancia = request.form['nombreInstancia']
    puerto = request.form['puerto']
    fechaIngreso = request.form['fechaIngreso']
    usuarioIngreso = request.form['usuarioIngreso']
    nombreGestorConexion = request.form['nombreGestorConexion']

    # # Conectar a la base de datos
    # conn = psycopg2.connect(
    #     host="localhost",
    #     database="nombre_de_la_base_de_datos",
    #     user="nombre_de_usuario",
    #     password="contraseña"
    # )

    # # Crear un cursor para realizar operaciones en la base de datos
    # cur = conn.cursor()

    # # Preparar el comando SQL para insertar un nuevo registro en la tabla mcpTbBaseDatos
    # sql = """
    #     INSERT INTO mdd.mcpTbBaseDatos (codigoBaseDatos, codigoServidor, codigoMotorBaseDatos, nombreBaseDatos,
    #     nombreInstancia, puerto, fechaIngreso, usuarioIngreso, nombreGestorConexion)
    #     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    #     """

    # # Ejecutar el comando SQL con los datos del formulario
    # cur.execute(sql, (codigoBaseDatos, codigoServidor, codigoMotorBaseDatos, nombreBaseDatos, nombreInstancia, puerto,
    #                   fechaIngreso, usuarioIngreso, nombreGestorConexion))

    # # Guardar los cambios en la base de datos
    # conn.commit()

    # # Cerrar la conexión a la base de datos
    # cur.close()
    # conn.close()

    return render_template('base_datos_proceso.html')


@app.route('/insertar_proceso_base_datos', methods=['POST'])
def insertar_proceso_base_datos():
    codigo_acceso = request.form['codigoAcceso']
    codigo_base_datos = request.form['codigoBaseDatos']
    codigo_proceso = request.form['codigoProceso']
    fecha_ingreso = request.form['fechaIngreso']
    usuario_ingreso = request.form['usuarioIngreso']

    # Insertar los datos en la base de datos
    # cur = conn.cursor()
    # cur.execute("INSERT INTO mdd.mcpTbAccesoBaseDatos (codigoAcceso, codigoBaseDatos, codigoProceso, fechaIngreso, usuarioIngreso) VALUES (%s, %s, %s, %s, %s)",
    #             (codigo_acceso, codigo_base_datos, codigo_proceso, fecha_ingreso, usuario_ingreso))
    # conn.commit()
    # cur.close()

    return render_template('tabla.html')


@app.route('/insertar_tabla', methods=['POST'])
def insertar_tabla():
    codigoBaseDatos = request.form['codigoBaseDatos']
    codigoTabla = request.form['codigoTabla']
    esquemaTabla = request.form['esquemaTabla']
    nombreTabla = request.form['nombreTabla']
    disponible = request.form['disponible']
    fechaUltimaActualizacion = request.form['fechaUltimaActualizacion']
    diasVigencia = request.form['diasVigencia']
    fechaCaducidad = request.form['fechaCaducidad']
    usuarioIngreso = request.form['usuarioIngreso']
    fechaIngreso = request.form['fechaIngreso']

    # # conexión a la base de datos y cursor
    # conn = psycopg2.connect(**db_config)
    # cur = conn.cursor()

    # # insertar registro en la tabla
    # cur.execute('''
    #         INSERT INTO mdd.mcpTbTabla(codigoBaseDatos, codigoTabla, esquemaTabla, nombreTabla, disponible, fechaUltimaActualizacion, diasVigencia, fechaCaducidad, usuarioIngreso, fechaIngreso)
    #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    #     ''', (codigoBaseDatos, codigoTabla, esquemaTabla, nombreTabla, disponible, fechaUltimaActualizacion, diasVigencia, fechaCaducidad, usuarioIngreso, fechaIngreso))

    # # confirmar cambios y cerrar conexión
    # conn.commit()
    # cur.close()
    # conn.close()

    return render_template('tabla_proceso.html')


@app.route('/insertar_proceso_tabla', methods=['POST'])
def insertar_proceso_tabla():
    codigoProceso = request.form['codigoProceso']
    codigoBaseDatos = request.form['codigoBaseDatos']
    codigoTabla = request.form['codigoTabla']
    flujoAcceso = request.form['flujoAcceso']
    fechaIngreso = request.form['fechaIngreso']
    usuarioIngreso = request.form['usuarioIngreso']

    # Insertar los valores en la tabla
    # cur = conn.cursor()
    # cur.execute(
    #     "INSERT INTO mdd.mcpTbTabla (codigoProceso, codigoBaseDatos, codigoTabla, flujoAcceso, fechaIngreso, usuarioIngreso) VALUES (%s, %s, %s, %s, %s, %s)",
    #     (codigoProceso, codigoBaseDatos, codigoTabla,
    #      flujoAcceso, fechaIngreso, usuarioIngreso)
    # )
    # conn.commit()
    # cur.close()
    return 'Registro insertado exitosamente!'


if __name__ == '__main__':
    app.run(debug=True)

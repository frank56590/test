# Librerias externas
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, flash
import pymysql
from fpdf import FPDF

app = Flask(__name__)
app.secret_key = "PwvBSAYAdZUno7TS8OxN9TSaztLTWYkk"

def obtener_datos():
    connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM unidades INNER JOIN docentes ON unidades.id_docente = docentes.id")
    datos = cursor.fetchall()
    cursor.close()

    return datos

def obtener_carreras():
    connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM carreras")
    datos = cursor.fetchall()
    cursor.close()

    return datos

def obtener_docentes():
    connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM docentes")
    datos = cursor.fetchall()
    cursor.close()

    return datos

@app.route("/")
def Index():
    datos = obtener_datos()
    carreras = obtener_carreras()
    docentes = obtener_docentes()
    print(docentes)

    if "usuario" in session:
        return render_template("pag_principal.html", datos=datos, carreras=carreras, docentes=docentes)
    else:
        return redirect(url_for("loggin"))

@app.route("/añadir", methods=["POST", "GET"])
def añadir():
    if "unidad" in request.args:
        docente = request.form["formSelecDocente"]
        nombre = request.form["formNombre"]
        carrera = request.form["formSelectCarrera"]
        horario = request.form.getlist("seleccionHorario")
        horario_L_in = request.form["formHorario_l_in"]
        horario_L_out = request.form["formHorario_l_out"]
        horario_MA_in = request.form["formHorario_ma_in"]
        horario_MA_out = request.form["formHorario_ma_out"]
        horario_MI_in = request.form["formHorario_mi_in"]
        horario_MI_out = request.form["formHorario_mi_out"]
        horario_J_in = request.form["formHorario_j_in"]
        horario_J_out = request.form["formHorario_j_out"]
        horario_V_in = request.form["formHorario_v_in"]
        horario_V_out = request.form["formHorario_v_out"]
        horario_dias = ""
        contenido_programatico = request.form['formcontenidoProgramatico']
        asistencia_semanal = request.form['formasistenciaSemanal'] 

        for i in horario:
            if i != "L" and i != horario[0]:
                horario_dias+= "-"
            horario_dias += i

        filas = "id_docente,unidad,carrera,dias,contenidoprogramatico,asistenciasemanal"
        formato = "%s,%s,%s,%s,%s,%s"
        valores = [docente, nombre, carrera, horario_dias, contenido_programatico, asistencia_semanal]

        if "L" in horario_dias:
            filas += ",horario_l_in,horario_l_out"
            formato += ",%s,%s"
            valores.extend([horario_L_in, horario_L_out])
        if "MA" in horario_dias:
            filas += ",horario_ma_in,horario_ma_out"
            formato += ",%s,%s"
            valores.extend([horario_MA_in, horario_MA_out])
        if "MI" in horario_dias:
            filas += ",horario_mi_in,horario_mi_out"
            formato += ",%s,%s"
            valores.extend([horario_MI_in, horario_MI_out])
        if "J" in horario_dias:
            filas += ",horario_j_in,horario_j_out"
            formato += ",%s,%s"
            valores.extend([horario_J_in, horario_J_out])
        if "V" in horario_dias:
            filas += ",horario_v_in,horario_v_out"
            formato += ",%s,%s"
            valores.extend([horario_V_in, horario_V_out])

        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO unidades ("+filas+") values("+formato+")", valores)
        connection.commit()
        cursor.close()

        return redirect(url_for("Index"))
    elif "docente" in request.args:
        nombre = request.form["formNombreDocente"]
        apellido = request.form["formApellidoDocente"]
        cedula = request.form["formCedulaDocente"]

        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM docentes WHERE cedula=%s", [cedula], )
        docentes = cursor.fetchall()
        cursor.close()

        if len(docentes) > 0:
            flash(u'Este docente ya existe.', 'danger')
            return redirect(url_for("Index"))

        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO docentes (nombre,apellido,cedula) values(%s,%s,%s)", (nombre, apellido, cedula))
        connection.commit()
        cursor.close()
        return redirect(url_for("Index"))
    elif "carrera" in request.args:
        titulo = request.form["formTituloCarrera"]

        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM unidades WHERE carrera=%s", [titulo], )
        unidades = cursor.fetchall()
        cursor.close()

        if len(unidades) > 0:
            flash(u'Esta carrera ya existe.', 'danger')
            return redirect(url_for("Index"))

        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO carreras (titulo) values(%s)", [titulo], )
        connection.commit()
        cursor.close()
        return redirect(url_for("Index"))

@app.route("/eliminar", methods = ["GET", "POST"])
def eliminar():
    if "unidad" in request.args:
        uid = request.args["unidad"]
        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM unidades WHERE id={0}".format(uid))
        connection.commit()
        cursor.close()

        return redirect(url_for("Index"))
    elif "docente" in request.args:
        did = request.args["docente"]
        
        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM unidades WHERE id_docente={0}".format(did))
        unidades = cursor.fetchall()
        cursor.close()

        if len(unidades) > 0:
            flash(u'Docente en asignaturas.', 'danger')
            return redirect(url_for("Index"))

        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM docentes WHERE id={0}".format(did))
        connection.commit()
        cursor.close()

        return redirect(url_for("Index"))
    elif "carrera" in request.args:
        nid = request.args["carrera"]
        
        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM unidades WHERE carrera=%s", [nid], )
        unidades = cursor.fetchall()
        cursor.close()

        if len(unidades) > 0:
            flash(u'Esta carrera esta en uso.', 'danger')
            return redirect(url_for("Index"))

        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM carreras WHERE titulo=%s", [nid], )
        connection.commit()
        cursor.close()

        return redirect(url_for("Index"))

@app.route("/reporte", methods = ["GET", "POSRT"])
def generar_reporte():
    if "unidad" in request.args:
        uid = request.args["unidad"]

        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM unidades INNER JOIN docentes ON unidades.id_docente=docentes.id WHERE unidades.id={0}".format(uid))
        unidad = cursor.fetchone()
        cursor.close()

        if len(unidad) < 1: 
            flash("No hay historiales.","danger")
            return redirect(url_for("Index"))

        pdf = FPDF("P", "mm", "A4")
        pdf.add_page()
        pdf.set_font("Times", "B", 11)
        pdf.image("static/img/banner.jpg",w=190)
        pdf.cell(190, 5, "Registro Académico (ID: {0})".format(unidad[0]),10, 25,"C")
        pdf.ln()

        pdf.cell(190, 5, "Carrera: {0}".format(unidad[3]),10, 25,"L")
        pdf.cell(190, 5, "Unidad: {0}".format(unidad[2]),10, 25,"L")
        pdf.cell(60, 5, ("DOCENTE"), 1, 0, "C")
        pdf.cell(25, 5, ("LUNES"), 1, 0, "C")
        pdf.cell(25, 5, ("MARTES"), 1, 0, "C")
        pdf.cell(25, 5, ("MIERCOLES"), 1, 0, "C")
        pdf.cell(25, 5, ("JUEVES"), 1, 0, "C")
        pdf.cell(25, 5, ("VIERNES"), 1, 1, "C")

        pdf.cell(60, 5,"%s %s [%s]" % (unidad[16], unidad[17], unidad[18]), 1, 0, "C")
        pdf.cell(25, 5, "%s-%s" % (unidad[5], unidad[6]), 1, 0, "C")
        pdf.cell(25, 5, "%s-%s" % (unidad[7], unidad[8]), 1, 0, "C")
        pdf.cell(25, 5, "%s-%s" % (unidad[9], unidad[10]), 1, 0, "C")
        pdf.cell(25, 5, "%s-%s" % (unidad[11], unidad[12]), 1, 0, "C")
        pdf.cell(25, 5, "%s-%s" % (unidad[13], unidad[14]), 1, 1, "C")

        documento = make_response(pdf.output(dest="S").encode("latin-1"))
        documento.headers.set("Content-Disposition", "attachment", filename="Horario_"+str(unidad[0])+"_unidad.pdf")
        documento.headers.set("Content-Type", "application/pdf")
        return documento
    elif "docente" in request.args:
        did = request.args["docente"]

        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM unidades INNER JOIN docentes ON unidades.id_docente=docentes.id WHERE unidades.id_docente={0}".format(did))
        unidades = cursor.fetchall()
        cursor.close()

        if len(unidades) < 1: 
            flash("No hay historiales.","danger")
            return redirect(url_for("Index"))

        pdf = FPDF("P", "mm", "A4")
        pdf.add_page()
        pdf.set_font("Times", "B", 8)
        pdf.image("static/img/banner.jpg",w=190)
        pdf.cell(190, 5, "HORARIO UNIDAD ACREDITABLE (ID: {0})".format(unidades[0][0]),10, 25,"C")
        pdf.ln()

        pdf.cell(190, 5, "Docente: %s %s [%s]"% (unidades[0][16], unidades[0][17], unidades[0][18]),10, 25,"L")
        pdf.cell(45, 5, ("CARRERA"), 1, 0, "C")
        pdf.cell(45, 5, ("UNIDAD"), 1, 0, "C")
        pdf.cell(21, 5, ("LUNES"), 1, 0, "C")
        pdf.cell(21, 5, ("MARTES"), 1, 0, "C")
        pdf.cell(25, 5, ("MIERCOLES"), 1, 0, "C")
        pdf.cell(21, 5, ("JUEVES"), 1, 0, "C")
        pdf.cell(21, 5, ("VIERNES"), 1, 1, "C")

        for unidad in unidades:
            pdf.cell(45, 5, "%s" % (unidad[3]), 1, 0, "C")
            pdf.cell(45, 5, "%s" % (unidad[2]), 1, 0, "C")
            pdf.cell(21, 5, "%s-%s" % (unidad[5], unidad[6]), 1, 0, "C")
            pdf.cell(21, 5, "%s-%s" % (unidad[7], unidad[8]), 1, 0, "C")
            pdf.cell(25, 5, "%s-%s" % (unidad[9], unidad[10]), 1, 0, "C")
            pdf.cell(21, 5, "%s-%s" % (unidad[11], unidad[12]), 1, 0, "C")
            pdf.cell(21, 5, "%s-%s" % (unidad[13], unidad[14]), 1, 1, "C")

        documento = make_response(pdf.output(dest="S").encode("latin-1"))
        documento.headers.set("Content-Disposition", "attachment", filename="Horario_"+str(unidad[0])+"_docente.pdf")
        documento.headers.set("Content-Type", "application/pdf")
        return documento
    elif "carrera" in request.args:
        cid = request.args["carrera"]

        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM unidades INNER JOIN docentes ON unidades.id_docente=docentes.id WHERE unidades.carrera=%s", [cid], )
        unidades = cursor.fetchall()
        cursor.close()

        if len(unidades) < 1: 
            flash("No hay historiales.","danger")
            return redirect(url_for("Index"))

        pdf = FPDF("P", "mm", "A4")
        pdf.add_page()
        pdf.set_font("Times", "B", 8)
        pdf.image("static/img/banner.jpg",w=190)
        pdf.cell(190, 5, "HORARIO UNIDAD ACREDITABLE (ID: {0})".format(unidades[0][0]),10, 25,"C")
        pdf.ln()

        pdf.cell(45, 5, ("UNIDAD"), 1, 0, "C")
        pdf.cell(45, 5, ("DOCENTE"), 1, 0, "C")
        pdf.cell(21, 5, ("LUNES"), 1, 0, "C")
        pdf.cell(21, 5, ("MARTES"), 1, 0, "C")
        pdf.cell(25, 5, ("MIERCOLES"), 1, 0, "C")
        pdf.cell(21, 5, ("JUEVES"), 1, 0, "C")
        pdf.cell(21, 5, ("VIERNES"), 1, 1, "C")

        for unidad in unidades:
            pdf.cell(45, 5, "%s" % (unidad[2]), 1, 0, "C")
            pdf.cell(45, 5, "%s %s [%s]"% (unidades[0][16], unidades[0][17], unidades[0][18]), 1, 0, "C")
            pdf.cell(21, 5, "%s-%s" % (unidad[5], unidad[6]), 1, 0, "C")
            pdf.cell(21, 5, "%s-%s" % (unidad[7], unidad[8]), 1, 0, "C")
            pdf.cell(25, 5, "%s-%s" % (unidad[9], unidad[10]), 1, 0, "C")
            pdf.cell(21, 5, "%s-%s" % (unidad[11], unidad[12]), 1, 0, "C")
            pdf.cell(21, 5, "%s-%s" % (unidad[13], unidad[14]), 1, 1, "C")

        documento = make_response(pdf.output(dest="S").encode("latin-1"))
        documento.headers.set("Content-Disposition", "attachment", filename="Horario_"+str(unidad[0])+"_carrera.pdf")
        documento.headers.set("Content-Type", "application/pdf")
        return documento
    else:
        return redirect(url_for("loggin"))


@app.route("/entrar", methods=["POST","GET"])
def loggin():
    if request.method == "GET":
        if "estado" in session:
            return redirect(url_for("Index"))
        else:
            return render_template("pag_inicio.html")
    else:
        usuario = request.form["formUser"]
        contraseña = request.form["formPw"]

        connection = pymysql.connect(host="localhost", user="root", passwd="", db="srcededb")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM acceso WHERE usuario=%s and clave=%s",[usuario, contraseña])
        usuario = cursor.fetchone()
        cursor.close()

        if usuario != None:
            session["usuario"]=usuario[1]
            session["estado"]=True
            return redirect(url_for("Index"))
        else:
            flash("Usuario o contraseña erroneos.","warning")
            return redirect(url_for("loggin"))

@app.route("/salir")
def Salir():
    session.clear()
    return redirect(url_for("Index"))

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)

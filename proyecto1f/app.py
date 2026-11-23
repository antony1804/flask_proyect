from datetime import date, datetime

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# usuario:contraseña@servidor:puerto/base_de_datos
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://antony:ant2613z@127.0.0.1:3308/tareas_db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

CATEGORIAS = ["trabajo", "hogar", "prioritarias"]


class Tarea(db.Model):
    __tablename__ = "tareas"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(20), nullable=False)
    fecha_limite = db.Column(db.Date, nullable=True)
    completada = db.Column(db.Boolean, default=False, nullable=False)

    @property
    def dias_restantes(self):
        if self.fecha_limite is None:
            return None
        return (self.fecha_limite - date.today()).days

    @property
    def vencida(self):
        return (
            not self.completada
            and self.dias_restantes is not None
            and self.dias_restantes < 0
        )


@app.route("/")
def inicio():
    q = request.args.get("q", "").strip()

    consulta = Tarea.query
    if q:
        consulta = consulta.filter(Tarea.titulo.ilike(f"%{q}%"))

    tareas_por_categoria = {
        cat: consulta.filter_by(categoria=cat)
        .order_by(Tarea.completada, Tarea.fecha_limite)
        .all()
        for cat in CATEGORIAS
    }
    total = sum(len(lista) for lista in tareas_por_categoria.values())

    return render_template(
        "index.html",
        tareas_por_categoria=tareas_por_categoria,
        categorias=CATEGORIAS,
        q=q,
        total=total,
        hoy=date.today().isoformat(),
    )


@app.route("/agregar", methods=["POST"])
def agregar():
    titulo = request.form.get("titulo", "").strip()
    categoria = request.form.get("categoria")
    fecha_texto = request.form.get("fecha_limite")

    if titulo and categoria in CATEGORIAS:
        fecha = None
        if fecha_texto:
            fecha = datetime.strptime(fecha_texto, "%Y-%m-%d").date()
        db.session.add(Tarea(titulo=titulo, categoria=categoria, fecha_limite=fecha))
        db.session.commit()

    return redirect(url_for("inicio", q=request.form.get("q") or None))


@app.route("/completar/<int:tarea_id>", methods=["POST"])
def completar(tarea_id):
    tarea = db.get_or_404(Tarea, tarea_id)
    tarea.completada = not tarea.completada
    db.session.commit()
    return redirect(url_for("inicio", q=request.form.get("q") or None))


@app.route("/eliminar/<int:tarea_id>", methods=["POST"])
def eliminar(tarea_id):
    tarea = db.get_or_404(Tarea, tarea_id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for("inicio", q=request.form.get("q") or None))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
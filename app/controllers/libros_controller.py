from flask import Blueprint,  request, render_template, redirect, url_for
from app.forms.libro_form import LibroForm
from app.models.libro import Libro
from app.services.libros_service import listar_libros, buscar_libro, editar_libro, crear_libro, prestar_libro, devolver_libro, listar_libros_disponibles, listar_libros_prestados, eliminar_libro
from app.forms.buscar_libro_form import BuscarLibroForm
from app.forms.prestamo_form import PrestamoForm
from app.forms.devolucion_form import DevolucionForm
from app.services.socio_service import listar_socios
from app.utils.decorators import login_required

libros_bp = Blueprint(
    "libros",
    __name__,
    url_prefix="/libros"
)

@libros_bp.route("/")
def listar():
    libros = listar_libros()
    return render_template("paginas/libros/libros.html", libros=libros)

@libros_bp.route("/grid")
def grid():
    libros = listar_libros()
    return render_template("paginas/libros/librosGrid.html", libros=libros)

@libros_bp.route("/disponibles")
def disponibles():
    libros = listar_libros_disponibles()
    return render_template("paginas/libros/librosDisponibles.html", libros=libros)

@libros_bp.route("/buscar", methods=["GET", "POST"])
def buscar():
    form = BuscarLibroForm()
    libros_encontrados = []

    if form.validate_on_submit():
        termino = form.titulo.data
        libros_encontrados = buscar_libro(termino)
    return render_template("paginas/libros/librosBuscar.html", form=form, libros=libros_encontrados)

@libros_bp.route("/<int:id>", methods=["GET","POST"])
@login_required
def detalle(id):
    libro = Libro.query.get(id)
    form = LibroForm(obj=libro)  # ← precarga datos
    if request.method == "POST":
        if form.validate_on_submit():
            libro.titulo = form.titulo.data
            libro.autor = form.autor.data
            libro.resumen = form.resumen.data
            libro.año = form.año.data
            libro.categoria = form.año.data

            editar_libro(
                libro_id=id,
                titulo=libro.titulo,
                autor=libro.autor,
                resumen=libro.resumen,
                año=libro.año,
                categoria=libro.categoria
            )
        return redirect(url_for("libros.listar"))
    return render_template("paginas/libros/libro_editar.html", form=form, libro=libro)

@libros_bp.route("/crear", methods=["GET", "POST"])
@login_required
def crear():
    form = LibroForm()
    if request.method == "POST":
        if form.validate_on_submit():
            titulo = form.titulo.data
            autor = form.autor.data
            resumen = form.resumen.data
            año = form.año.data
            categoria = form.categoria.data

            crear_libro(titulo, autor, resumen, año, categoria)

            return redirect(url_for("libros.listar"))

    return render_template("paginas/libros/libro_crear.html", form=form)

@libros_bp.route("/eliminar/<int:id>")
@login_required
def eliminar(id):
    eliminar_libro(id)

    return redirect(url_for("libros.listar"))

@libros_bp.route("/prestamo", defaults={'id': None}, methods=["GET", "POST"])
@libros_bp.route("/prestamo/<int:id>", methods=["GET", "POST"])
@login_required
def prestamo(id):
    form = PrestamoForm()
    
    libros_libres = listar_libros_disponibles()
    lista_socios = listar_socios()
    
    form.libro_id.choices = [(l.id, l.titulo) for l in libros_libres]
    form.socio_id.choices = [(s.id, f"{s.nombre} ({s.email})") for s in lista_socios]

    if request.method == 'GET' and id:
        form.libro_id.data = id

    if form.validate_on_submit():
        prestar_libro(form.libro_id.data, form.socio_id.data)
        return redirect(url_for("libros.listar"))
    
    return render_template("paginas/libros/libro_prestar.html", form=form)

@libros_bp.route("/devolucion", defaults={'id': None}, methods=["GET", "POST"])
@libros_bp.route("/devolucion/<int:id>", methods=["GET", "POST"])
@login_required
def devolucion(id):
    form = DevolucionForm()

    libros_prestados = listar_libros_prestados()

    form.libro_id.choices = [(l.id, f"{l.titulo} (Socio ID: {l.id_socio_prestado})") for l in libros_prestados]

    if request.method == 'GET' and id:
        form.libro_id.data = id
    
    if form.validate_on_submit():
        devolver_libro(form.libro_id.data)
        return redirect(url_for("libros.listar"))
    
    return render_template("paginas/libros/libro_devolver.html", form=form)
from flask import Blueprint,  request, render_template, redirect, url_for
from app.forms.libro_form import LibroForm
from app.models.libro import Libro
from app.services.libros_service import listar_libros, buscar_libro, editar_libro, crear_libro, prestar_libro, devolver_libro, listar_libros_disponibles, listar_libros_prestados
from app.forms.buscar_libro_form import BuscarLibroForm
from app.services.socio_service import listar_socios

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
def detalle(id):
    libro = Libro.query.get(id)
    form = LibroForm(obj=libro)  # ← precarga datos
    if request.method == "POST":
        if form.validate_on_submit():
            libro.titulo = form.titulo.data
            libro.autor = form.autor.data
            libro.resumen = form.resumen.data

            editar_libro(
                libro_id=id,
                titulo=libro.titulo,
                autor=libro.autor,
                resumen=libro.resumen
            )

          
   #return render_template("libro.html", form=form, libro=libro)
    return render_template("paginas/libros/libro_editar.html", form=form, libro=libro)

@libros_bp.route("/crear", methods=["GET", "POST"])
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

@libros_bp.route("/prestamo", defaults={'id': None}, methods=["GET", "POST"])

@libros_bp.route("/prestamo/<int:id>", methods=["GET", "POST"])
def prestamo(id):
    if request.method == "POST":
        libro_id_form = request.form.get("libro_id")
        socio_id_form = request.form.get("socio_id")
        
        prestar_libro(libro_id_form, socio_id_form)
        return redirect(url_for("libros.listar"))

    libros_libres = listar_libros_disponibles()
    lista_socios = listar_socios()
    
    return render_template("paginas/libros/libro_prestar.html", libros=libros_libres, socios=lista_socios, id_preseleccionado=id)

@libros_bp.route("/devolucion", defaults={'id': None}, methods=["GET", "POST"])
@libros_bp.route("/devolucion/<int:id>", methods=["GET", "POST"])
def devolucion(id):
    if request.method == "POST":
        libro_id_form = request.form.get("libro_id")
        
        devolver_libro(libro_id_form)
        return redirect(url_for("libros.listar"))

    libros_ocupados = listar_libros_prestados()
    
    return render_template("paginas/libros/libro_devolver.html", libros=libros_ocupados, id_preseleccionado=id)
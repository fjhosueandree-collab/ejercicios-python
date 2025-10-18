#!/usr/bin/env python3
"""
Programa de Recetas Sostenibles - Con Soporte de Imágenes
=========================================================
Versión que incluye funcionalidad para agregar imágenes a las recetas.
Si no tienes PIL/Pillow instalado, el programa funcionará sin imágenes.
"""

import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from datetime import datetime
import shutil

# Intentar importar PIL, si no está disponible, usar versión sin imágenes
try:
    from PIL import Image, ImageTk
    PIL_DISPONIBLE = True
    print("✅ PIL/Pillow disponible - Soporte completo de imágenes")
except ImportError:
    PIL_DISPONIBLE = False
    print("⚠️ PIL/Pillow no disponible - Funcionalidad de imágenes limitada")

class RecetasConImagenes:
    def __init__(self):
        self.recetas = []
        self.archivo_datos = "recetas_sostenibles.json"
        self.cargar_recetas()
        self.crear_interfaz()
    
    def cargar_recetas(self):
        """Carga las recetas desde el archivo JSON"""
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                    self.recetas = json.load(f)
                print(f"✅ Cargadas {len(self.recetas)} recetas")
            except Exception as e:
                print(f"❌ Error al cargar recetas: {e}")
                self.recetas = []
        else:
            self.recetas_iniciales()
    
    def guardar_recetas(self):
        """Guarda las recetas en el archivo JSON"""
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                json.dump(self.recetas, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("Éxito", "Recetas guardadas exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {e}")
    
    def recetas_iniciales(self):
        """Agrega algunas recetas de ejemplo"""
        # Buscar imágenes disponibles
        carpeta_imagenes = "imagenes_recetas"
        imagenes_disponibles = []
        if os.path.exists(carpeta_imagenes):
            import glob
            imagenes_disponibles = glob.glob(os.path.join(carpeta_imagenes, "*.png"))
            imagenes_disponibles.extend(glob.glob(os.path.join(carpeta_imagenes, "*.jpg")))
            imagenes_disponibles.extend(glob.glob(os.path.join(carpeta_imagenes, "*.jpeg")))
        
        def obtener_imagen_receta(indice):
            """Obtiene la imagen correspondiente a una receta por su índice"""
            for imagen_path in imagenes_disponibles:
                if f"receta_{indice}_" in os.path.basename(imagen_path):
                    return imagen_path
            return ""
        
        recetas_ejemplo = [
            {
                "id": 1,
                "nombre": "Ceviche de Pescado Fresco",
                "categoria": "Ensalada",
                "tiempo_preparacion": 25,
                "ingredientes": "Pescado blanco fresco (400g), limón (4), cebolla morada (1), ají amarillo (1), cilantro, sal, camote (1), choclo (1)",
                "instrucciones": "Cortar pescado en cubos, marinar con limón 15 minutos. Agregar cebolla, ají y cilantro. Servir con camote y choclo cocidos",
                "beneficios": "Pescado fresco local, sin cocción, ingredientes peruanos tradicionales, rico en proteínas y vitamina C",
                "imagen": obtener_imagen_receta(1),
                "fecha_creacion": datetime.now().isoformat()
            },
            {
                "id": 2,
                "nombre": "Lomo Saltado Peruano",
                "categoria": "Principal",
                "tiempo_preparacion": 20,
                "ingredientes": "Lomo de res (300g), cebolla (1), tomate (2), ají amarillo (1), papas fritas, arroz, salsa de soja, vinagre, aceite, cilantro",
                "instrucciones": "Cortar lomo en tiras, saltear con cebolla y tomate. Agregar ají, salsa de soja y vinagre. Servir con papas fritas y arroz blanco",
                "beneficios": "Cocina fusión peruana-china, ingredientes frescos locales, técnica de salteado rápida, sabor auténtico peruano",
                "imagen": obtener_imagen_receta(2),
                "fecha_creacion": datetime.now().isoformat()
            },
            {
                "id": 3,
                "nombre": "Hummus de Garbanzos Locales",
                "categoria": "Aperitivos",
                "tiempo_preparacion": 15,
                "ingredientes": "Garbanzos cocidos (400g), tahini (3 cdas), jugo de limón (2 cdas), ajo (2 dientes), comino, aceite de oliva, sal, agua",
                "instrucciones": "Procesar todos los ingredientes hasta obtener una pasta cremosa. Ajustar consistencia con agua si es necesario. Servir con verduras crudas locales.",
                "beneficios": "Legumbres de cultivo local, sin conservantes, packaging mínimo, rico en proteínas vegetales",
                "imagen": obtener_imagen_receta(3),
                "fecha_creacion": datetime.now().isoformat()
            },
            {
                "id": 4,
                "nombre": "Quiche de Espinacas y Champiñones",
                "categoria": "Principal",
                "tiempo_preparacion": 45,
                "ingredientes": "Masa de hojaldre (250g), espinacas frescas (200g), champiñones (150g), huevos (4), leche (200ml), queso rallado (100g), cebolla (1), aceite de oliva, sal, pimienta",
                "instrucciones": "Cocinar espinacas y champiñones. Batir huevos con leche y queso. Forrar molde con masa, agregar verduras y mezcla de huevos. Hornear 25 minutos a 180°C.",
                "beneficios": "Verduras de temporada, reducción de desperdicio alimentario, ingredientes frescos locales",
                "imagen": "",
                "fecha_creacion": datetime.now().isoformat()
            },
            {
                "id": 5,
                "nombre": "Gazpacho Andaluz Tradicional",
                "categoria": "Sopas",
                "tiempo_preparacion": 20,
                "ingredientes": "Tomates maduros (1kg), pepino (1), pimiento verde (1), ajo (2 dientes), aceite de oliva (4 cdas), vinagre (2 cdas), sal, pan duro (50g)",
                "instrucciones": "Triturar todos los ingredientes. Colar y enfriar en nevera. Servir con cubitos de hielo y guarniciones frescas.",
                "beneficios": "Receta tradicional sin procesamiento, aprovecha pan duro, ingredientes de temporada, sin conservantes",
                "imagen": "",
                "fecha_creacion": datetime.now().isoformat()
            },
            {
                "id": 6,
                "nombre": "Curry de Lentejas con Coco",
                "categoria": "Principal",
                "tiempo_preparacion": 35,
                "ingredientes": "Lentejas rojas (300g), leche de coco (400ml), cebolla (1), tomate (2), jengibre, ajo, curry en polvo, aceite de coco, cilantro, arroz integral",
                "instrucciones": "Cocinar lentejas. Sofreír cebolla, agregar especias, tomate y lentejas. Añadir leche de coco y cocinar 15 minutos. Servir con arroz integral.",
                "beneficios": "Proteínas vegetales, especias sin procesar, ingredientes secos con larga vida útil, reducción de huella de carbono",
                "imagen": "",
                "fecha_creacion": datetime.now().isoformat()
            },
            {
                "id": 7,
                "nombre": "Ensalada de Frutas de Temporada",
                "categoria": "Postre",
                "tiempo_preparacion": 10,
                "ingredientes": "Manzanas (2), peras (2), uvas (200g), granada (1), miel (2 cdas), jugo de limón, menta fresca",
                "instrucciones": "Lavar y cortar todas las frutas en cubos. Mezclar con miel y limón. Decorar con granos de granada y menta.",
                "beneficios": "Frutas de temporada local, sin procesamiento, rico en vitaminas naturales, cero desperdicio",
                "imagen": "",
                "fecha_creacion": datetime.now().isoformat()
            },
            {
                "id": 8,
                "nombre": "Pan Integral Casero",
                "categoria": "Panadería",
                "tiempo_preparacion": 180,
                "ingredientes": "Harina integral (500g), agua tibia (300ml), levadura seca (7g), sal (10g), aceite de oliva (2 cdas), semillas de girasol (50g)",
                "instrucciones": "Mezclar ingredientes, amasar 10 minutos. Dejar reposar 2 horas. Hornear 35 minutos a 200°C hasta dorar.",
                "beneficios": "Sin conservantes, control total de ingredientes, packaging casero, harina integral nutritiva",
                "imagen": "",
                "fecha_creacion": datetime.now().isoformat()
            },
            {
                "id": 9,
                "nombre": "Batido de Avena y Plátano",
                "categoria": "Desayuno",
                "tiempo_preparacion": 5,
                "ingredientes": "Avena (50g), plátano (1), leche vegetal (300ml), miel (1 cda), canela, hielo (opcional)",
                "instrucciones": "Remojar avena 5 minutos. Licuar con plátano, leche y miel. Servir con canela espolvoreada.",
                "beneficios": "Energía sostenible, ingredientes naturales, sin procesamiento industrial, rico en fibra",
                "imagen": "",
                "fecha_creacion": datetime.now().isoformat()
            },
            {
                "id": 10,
                "nombre": "Ratatouille Provenzal",
                "categoria": "Guarnición",
                "tiempo_preparacion": 40,
                "ingredientes": "Berenjena (1), calabacín (2), tomates (3), pimiento rojo (1), cebolla (1), ajo (3 dientes), hierbas provenzales, aceite de oliva",
                "instrucciones": "Cortar verduras en rodajas. Sofreír cebolla y ajo. Capas de verduras en cazuela con hierbas. Hornear 30 minutos a 180°C.",
                "beneficios": "Receta tradicional, aprovecha verduras de temporada, técnicas de cocción eficientes, sabor intenso natural",
                "imagen": "",
                "fecha_creacion": datetime.now().isoformat()
            }
        ]
        self.recetas = recetas_ejemplo
        self.guardar_recetas()
    
    def crear_interfaz(self):
        """Crea la interfaz gráfica principal"""
        self.root = tk.Tk()
        self.root.title("🌱 Recetas Sostenibles - Con Imágenes")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f8f0')
        
        # Título con estado de imágenes
        titulo_texto = "🌱 Recetas Sostenibles"
        if PIL_DISPONIBLE:
            titulo_texto += " 📷"
        else:
            titulo_texto += " ⚠️"
        
        titulo = tk.Label(self.root, text=titulo_texto, 
                         font=('Arial', 20, 'bold'), bg='#f0f8f0')
        titulo.pack(pady=20)
        
        # Información sobre imágenes
        if not PIL_DISPONIBLE:
            info_frame = tk.Frame(self.root, bg='#fff3cd', relief=tk.RAISED, bd=1)
            info_frame.pack(fill=tk.X, padx=20, pady=(0, 10))
            tk.Label(info_frame, text="⚠️ Para funcionalidad completa de imágenes, instala: pip install Pillow", 
                    font=('Arial', 10), bg='#fff3cd', fg='#856404').pack(pady=5)
        
        # Frame para botones
        frame_botones = tk.Frame(self.root, bg='#f0f8f0')
        frame_botones.pack(pady=10)
        
        # Botones principales
        tk.Button(frame_botones, text="➕ Nueva Receta", 
                 command=self.nueva_receta, font=('Arial', 12), 
                 bg='#4CAF50', fg='white', padx=20, pady=10).pack(side=tk.LEFT, padx=5)
        
        tk.Button(frame_botones, text="📋 Ver Todas", 
                 command=self.ver_todas, font=('Arial', 12), 
                 bg='#2196F3', fg='white', padx=20, pady=10).pack(side=tk.LEFT, padx=5)
        
        tk.Button(frame_botones, text="🔍 Buscar", 
                 command=self.buscar_receta, font=('Arial', 12), 
                 bg='#FF9800', fg='white', padx=20, pady=10).pack(side=tk.LEFT, padx=5)
        
        tk.Button(frame_botones, text="📊 Estadísticas", 
                 command=self.mostrar_estadisticas, font=('Arial', 12), 
                 bg='#9C27B0', fg='white', padx=20, pady=10).pack(side=tk.LEFT, padx=5)
        
        # Frame para mostrar recetas
        frame_recetas = tk.Frame(self.root, bg='#f0f8f0')
        frame_recetas.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Listbox para mostrar recetas
        tk.Label(frame_recetas, text="📋 Lista de Recetas:", 
                font=('Arial', 14, 'bold'), bg='#f0f8f0').pack(anchor=tk.W)
        
        self.listbox = tk.Listbox(frame_recetas, font=('Arial', 11), height=15)
        self.listbox.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(frame_recetas)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        
        # Frame para botones de acción
        frame_acciones = tk.Frame(self.root, bg='#f0f8f0')
        frame_acciones.pack(pady=10)
        
        tk.Button(frame_acciones, text="👁️ Ver Detalles", 
                 command=self.ver_detalles, font=('Arial', 12), 
                 bg='#607D8B', fg='white', padx=15, pady=8).pack(side=tk.LEFT, padx=5)
        
        tk.Button(frame_acciones, text="🗑️ Eliminar", 
                 command=self.eliminar_receta, font=('Arial', 12), 
                 bg='#F44336', fg='white', padx=15, pady=8).pack(side=tk.LEFT, padx=5)
        
        tk.Button(frame_acciones, text="💾 Guardar", 
                 command=self.guardar_recetas, font=('Arial', 12), 
                 bg='#795548', fg='white', padx=15, pady=8).pack(side=tk.LEFT, padx=5)
        
        # Actualizar lista
        self.actualizar_lista()
    
    def actualizar_lista(self):
        """Actualiza la lista de recetas"""
        self.listbox.delete(0, tk.END)
        for receta in self.recetas:
            # Agregar indicador de imagen
            icono_imagen = "📷" if receta.get('imagen') else "📝"
            self.listbox.insert(tk.END, f"{icono_imagen} {receta['nombre']} ({receta['categoria']}) - {receta['tiempo_preparacion']} min")
    
    def nueva_receta(self):
        """Agrega una nueva receta"""
        ventana = tk.Toplevel(self.root)
        ventana.title("➕ Nueva Receta Sostenible")
        ventana.geometry("700x800")
        ventana.configure(bg='#f0f8f0')
        
        # Variables para la imagen
        self.imagen_path = tk.StringVar()
        self.imagen_preview = None
        
        # Título
        tk.Label(ventana, text="🍃 Nueva Receta Sostenible", 
                font=('Arial', 16, 'bold'), bg='#f0f8f0').pack(pady=20)
        
        # Frame principal con scroll
        canvas = tk.Canvas(ventana, bg='#f0f8f0')
        scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#f0f8f0')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Frame para formulario
        frame_form = tk.Frame(scrollable_frame, bg='#f0f8f0')
        frame_form.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Campos del formulario
        tk.Label(frame_form, text="Nombre de la receta:", bg='#f0f8f0', font=('Arial', 11, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        entry_nombre = tk.Entry(frame_form, width=60, font=('Arial', 11))
        entry_nombre.pack(pady=(0, 15))
        
        tk.Label(frame_form, text="Categoría:", bg='#f0f8f0', font=('Arial', 11, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        entry_categoria = tk.Entry(frame_form, width=60, font=('Arial', 11))
        entry_categoria.pack(pady=(0, 15))
        
        tk.Label(frame_form, text="Tiempo de preparación (minutos):", bg='#f0f8f0', font=('Arial', 11, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        entry_tiempo = tk.Entry(frame_form, width=60, font=('Arial', 11))
        entry_tiempo.pack(pady=(0, 15))
        
        # Frame para imagen
        frame_imagen = tk.LabelFrame(frame_form, text="🖼️ Imagen de la Receta", bg='#f0f8f0', font=('Arial', 11, 'bold'))
        frame_imagen.pack(fill=tk.X, pady=(0, 15))
        
        # Cuadro de imagen
        self.label_imagen = tk.Label(frame_imagen, text="📷 Sin imagen seleccionada\n\nHaz clic en 'Seleccionar Imagen'\npara agregar una foto", 
                                   bg='#f8f8f8', relief=tk.SUNKEN, width=40, height=8, 
                                   font=('Arial', 10), fg='#666')
        self.label_imagen.pack(pady=10, padx=10)
        
        # Botones para imagen
        frame_btn_imagen = tk.Frame(frame_imagen, bg='#f0f8f0')
        frame_btn_imagen.pack(pady=(0, 10))
        
        def seleccionar_imagen():
            if not PIL_DISPONIBLE:
                messagebox.showwarning("Advertencia", "Para usar imágenes, instala Pillow:\npip install Pillow")
                return
                
            archivo = filedialog.askopenfilename(
                title="Seleccionar imagen",
                filetypes=[
                    ("Imágenes", "*.jpg *.jpeg *.png *.gif *.bmp"),
                    ("JPEG", "*.jpg *.jpeg"),
                    ("PNG", "*.png"),
                    ("Todos los archivos", "*.*")
                ]
            )
            if archivo:
                self.imagen_path.set(archivo)
                self.mostrar_preview_imagen(archivo)
        
        def eliminar_imagen():
            self.imagen_path.set("")
            self.label_imagen.config(image='', text="📷 Sin imagen seleccionada\n\nHaz clic en 'Seleccionar Imagen'\npara agregar una foto")
            self.imagen_preview = None
        
        tk.Button(frame_btn_imagen, text="📁 Seleccionar Imagen", command=seleccionar_imagen, 
                 font=('Arial', 10), bg='#2196F3', fg='white', padx=15, pady=5).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn_imagen, text="🗑️ Eliminar Imagen", command=eliminar_imagen, 
                 font=('Arial', 10), bg='#F44336', fg='white', padx=15, pady=5).pack(side=tk.LEFT, padx=5)
        
        # Información sobre PIL si no está disponible
        if not PIL_DISPONIBLE:
            tk.Label(frame_imagen, text="⚠️ Instala 'pip install Pillow' para usar imágenes", 
                    font=('Arial', 9), bg='#f0f8f0', fg='#f44336').pack(pady=5)
        
        tk.Label(frame_form, text="Ingredientes:", bg='#f0f8f0', font=('Arial', 11, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        text_ingredientes = tk.Text(frame_form, height=4, width=60, font=('Arial', 11))
        text_ingredientes.pack(pady=(0, 15))
        
        tk.Label(frame_form, text="Instrucciones:", bg='#f0f8f0', font=('Arial', 11, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        text_instrucciones = tk.Text(frame_form, height=4, width=60, font=('Arial', 11))
        text_instrucciones.pack(pady=(0, 15))
        
        tk.Label(frame_form, text="Beneficios sostenibles:", bg='#f0f8f0', font=('Arial', 11, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        text_beneficios = tk.Text(frame_form, height=3, width=60, font=('Arial', 11))
        text_beneficios.pack(pady=(0, 20))
        
        def guardar():
            nombre = entry_nombre.get().strip()
            if not nombre:
                messagebox.showerror("Error", "El nombre de la receta es obligatorio")
                return
            
            # Copiar imagen a carpeta de recetas si se seleccionó una
            imagen_guardada = ""
            if self.imagen_path.get():
                try:
                    # Crear carpeta de imágenes si no existe
                    carpeta_imagenes = "imagenes_recetas"
                    if not os.path.exists(carpeta_imagenes):
                        os.makedirs(carpeta_imagenes)
                    
                    # Generar nombre único para la imagen
                    extension = os.path.splitext(self.imagen_path.get())[1]
                    nombre_imagen = f"receta_{len(self.recetas) + 1}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{extension}"
                    ruta_destino = os.path.join(carpeta_imagenes, nombre_imagen)
                    
                    # Copiar imagen
                    shutil.copy2(self.imagen_path.get(), ruta_destino)
                    imagen_guardada = ruta_destino
                    
                except Exception as e:
                    messagebox.showwarning("Advertencia", f"No se pudo guardar la imagen: {e}")
            
            nueva_receta = {
                "id": len(self.recetas) + 1,
                "nombre": nombre,
                "categoria": entry_categoria.get().strip(),
                "tiempo_preparacion": int(entry_tiempo.get()) if entry_tiempo.get().isdigit() else 0,
                "ingredientes": text_ingredientes.get(1.0, tk.END).strip(),
                "instrucciones": text_instrucciones.get(1.0, tk.END).strip(),
                "beneficios": text_beneficios.get(1.0, tk.END).strip(),
                "imagen": imagen_guardada,
                "fecha_creacion": datetime.now().isoformat()
            }
            
            self.recetas.append(nueva_receta)
            self.actualizar_lista()
            self.guardar_recetas()
            ventana.destroy()
            messagebox.showinfo("Éxito", f"Receta '{nombre}' agregada exitosamente!")
        
        # Botones
        frame_btn = tk.Frame(ventana, bg='#f0f8f0')
        frame_btn.pack(pady=20)
        
        tk.Button(frame_btn, text="💾 Guardar Receta", command=guardar, 
                 font=('Arial', 12, 'bold'), bg='#4CAF50', fg='white', padx=25, pady=10).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="❌ Cancelar", command=ventana.destroy, 
                 font=('Arial', 12), bg='#F44336', fg='white', padx=25, pady=10).pack(side=tk.LEFT, padx=5)
        
        # Configurar scroll
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Hacer que la ventana sea redimensionable
        ventana.resizable(True, True)
    
    def mostrar_preview_imagen(self, ruta_imagen):
        """Muestra un preview de la imagen seleccionada"""
        if not PIL_DISPONIBLE:
            self.label_imagen.config(text="⚠️ PIL no disponible")
            return
            
        try:
            # Cargar y redimensionar la imagen
            imagen_original = Image.open(ruta_imagen)
            
            # Redimensionar manteniendo proporción (máximo 200x150)
            imagen_original.thumbnail((200, 150), Image.Resampling.LANCZOS)
            
            # Convertir para Tkinter
            self.imagen_preview = ImageTk.PhotoImage(imagen_original)
            
            # Actualizar el label
            self.label_imagen.config(image=self.imagen_preview, text="")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")
            self.label_imagen.config(image='', text="❌ Error al cargar imagen")
    
    def ver_todas(self):
        """Muestra todas las recetas"""
        if not self.recetas:
            messagebox.showinfo("Info", "No hay recetas registradas")
            return
        
        ventana = tk.Toplevel(self.root)
        ventana.title("📋 Todas las Recetas")
        ventana.geometry("700x500")
        
        # Texto con todas las recetas
        texto = tk.Text(ventana, font=('Arial', 11))
        texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for i, receta in enumerate(self.recetas, 1):
            icono_imagen = "📷" if receta.get('imagen') else "📝"
            texto.insert(tk.END, f"{i}. {icono_imagen} {receta['nombre']}\n")
            texto.insert(tk.END, f"   📂 Categoría: {receta['categoria']}\n")
            texto.insert(tk.END, f"   ⏱️ Tiempo: {receta['tiempo_preparacion']} minutos\n")
            texto.insert(tk.END, f"   📝 Ingredientes: {receta['ingredientes']}\n")
            texto.insert(tk.END, f"   🌱 Beneficios: {receta['beneficios']}\n\n")
        
        texto.config(state=tk.DISABLED)
    
    def buscar_receta(self):
        """Busca recetas"""
        termino = simpledialog.askstring("🔍 Buscar", "Ingresa el término de búsqueda:")
        if not termino:
            return
        
        termino = termino.lower()
        resultados = []
        
        for receta in self.recetas:
            if (termino in receta['nombre'].lower() or 
                termino in receta['categoria'].lower() or 
                termino in receta['ingredientes'].lower()):
                resultados.append(receta)
        
        if resultados:
            ventana = tk.Toplevel(self.root)
            ventana.title(f"🔍 Resultados para '{termino}'")
            ventana.geometry("600x400")
            
            texto = tk.Text(ventana, font=('Arial', 11))
            texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            for receta in resultados:
                icono_imagen = "📷" if receta.get('imagen') else "📝"
                texto.insert(tk.END, f"{icono_imagen} {receta['nombre']}\n")
                texto.insert(tk.END, f"📂 {receta['categoria']} | ⏱️ {receta['tiempo_preparacion']} min\n\n")
            
            texto.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Búsqueda", f"No se encontraron recetas con '{termino}'")
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas"""
        if not self.recetas:
            messagebox.showinfo("Estadísticas", "No hay recetas registradas")
            return
        
        total = len(self.recetas)
        categorias = {}
        tiempo_total = 0
        recetas_con_imagen = 0
        
        for receta in self.recetas:
            cat = receta['categoria']
            categorias[cat] = categorias.get(cat, 0) + 1
            tiempo_total += receta['tiempo_preparacion']
            if receta.get('imagen'):
                recetas_con_imagen += 1
        
        tiempo_promedio = tiempo_total / total
        
        stats = f"""📊 ESTADÍSTICAS
        
Total de recetas: {total}
Recetas con imagen: {recetas_con_imagen} ({recetas_con_imagen/total*100:.1f}%)
Tiempo promedio: {tiempo_promedio:.1f} minutos

📂 Por categoría:"""
        
        for categoria, cantidad in categorias.items():
            stats += f"\n• {categoria}: {cantidad}"
        
        if PIL_DISPONIBLE:
            stats += "\n\n📷 Soporte de imágenes: ✅ Disponible"
        else:
            stats += "\n\n📷 Soporte de imágenes: ❌ Instala 'pip install Pillow'"
        
        messagebox.showinfo("📊 Estadísticas", stats)
    
    def ver_detalles(self):
        """Muestra detalles de la receta seleccionada"""
        seleccion = self.listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona una receta primero")
            return
        
        indice = seleccion[0]
        receta = self.recetas[indice]
        
        ventana = tk.Toplevel(self.root)
        ventana.title(f"🍃 {receta['nombre']}")
        ventana.geometry("800x600")
        
        # Frame principal
        frame = tk.Frame(ventana)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        tk.Label(frame, text=f"🍃 {receta['nombre']}", 
                font=('Arial', 16, 'bold')).pack(pady=(0, 20))
        
        # Frame para imagen y detalles básicos
        frame_superior = tk.Frame(frame)
        frame_superior.pack(fill=tk.X, pady=(0, 20))
        
        # Mostrar imagen si existe y PIL está disponible
        if receta.get('imagen') and os.path.exists(receta['imagen']) and PIL_DISPONIBLE:
            try:
                imagen_detalle = Image.open(receta['imagen'])
                imagen_detalle.thumbnail((250, 200), Image.Resampling.LANCZOS)
                imagen_tk = ImageTk.PhotoImage(imagen_detalle)
                
                # Frame para la imagen
                frame_imagen_detalle = tk.Frame(frame_superior)
                frame_imagen_detalle.pack(side=tk.LEFT, padx=(0, 20))
                
                tk.Label(frame_imagen_detalle, image=imagen_tk, relief=tk.SUNKEN).pack()
                tk.Label(frame_imagen_detalle, text="🖼️ Imagen de la receta", 
                        font=('Arial', 10), fg='#666').pack(pady=(5, 0))
                
                # Guardar referencia para evitar garbage collection
                frame_imagen_detalle.imagen_tk = imagen_tk
                
            except Exception as e:
                print(f"Error al cargar imagen: {e}")
        
        # Frame para detalles básicos
        frame_detalles_basicos = tk.Frame(frame_superior)
        frame_detalles_basicos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Detalles básicos
        tk.Label(frame_detalles_basicos, text=f"📂 Categoría: {receta['categoria']}", 
                font=('Arial', 12)).pack(anchor=tk.W, pady=2)
        tk.Label(frame_detalles_basicos, text=f"⏱️ Tiempo: {receta['tiempo_preparacion']} minutos", 
                font=('Arial', 12)).pack(anchor=tk.W, pady=2)
        
        if receta.get('imagen'):
            if os.path.exists(receta['imagen']):
                estado_imagen = "✅ Con imagen" if PIL_DISPONIBLE else "📷 Imagen guardada (PIL no disponible)"
            else:
                estado_imagen = "❌ Imagen no encontrada"
            tk.Label(frame_detalles_basicos, text=f"🖼️ {estado_imagen}", 
                    font=('Arial', 12)).pack(anchor=tk.W, pady=2)
        
        # Separador
        tk.Frame(frame, height=2, bg='#ddd').pack(fill=tk.X, pady=10)
        
        # Frame para texto con scroll
        frame_texto = tk.Frame(frame)
        frame_texto.pack(fill=tk.BOTH, expand=True)
        
        # Crear área de texto con scroll
        texto_detalles = tk.Text(frame_texto, font=('Arial', 11), wrap=tk.WORD, height=15)
        scrollbar_texto = tk.Scrollbar(frame_texto, orient="vertical", command=texto_detalles.yview)
        texto_detalles.configure(yscrollcommand=scrollbar_texto.set)
        
        # Insertar contenido
        texto_detalles.insert(tk.END, "📝 INGREDIENTES:\n", "titulo")
        texto_detalles.insert(tk.END, f"{receta['ingredientes']}\n\n")
        
        texto_detalles.insert(tk.END, "👨‍🍳 INSTRUCCIONES:\n", "titulo")
        texto_detalles.insert(tk.END, f"{receta['instrucciones']}\n\n")
        
        texto_detalles.insert(tk.END, "🌱 BENEFICIOS SOSTENIBLES:\n", "titulo")
        texto_detalles.insert(tk.END, f"{receta['beneficios']}")
        
        # Configurar formato
        texto_detalles.tag_configure("titulo", font=('Arial', 12, 'bold'), foreground='#2E7D32')
        
        # Pack
        texto_detalles.pack(side="left", fill="both", expand=True)
        scrollbar_texto.pack(side="right", fill="y")
        
        # Hacer el texto de solo lectura
        texto_detalles.config(state=tk.DISABLED)
    
    def eliminar_receta(self):
        """Elimina la receta seleccionada"""
        seleccion = self.listbox.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona una receta para eliminar")
            return
        
        indice = seleccion[0]
        receta = self.recetas[indice]
        
        respuesta = messagebox.askyesno("Confirmar", 
                                      f"¿Eliminar la receta '{receta['nombre']}'?")
        if respuesta:
            # Eliminar imagen si existe
            if receta.get('imagen') and os.path.exists(receta['imagen']):
                try:
                    os.remove(receta['imagen'])
                except Exception as e:
                    print(f"Error al eliminar imagen: {e}")
            
            del self.recetas[indice]
            self.actualizar_lista()
            self.guardar_recetas()
            messagebox.showinfo("Éxito", "Receta eliminada exitosamente")
    
    def ejecutar(self):
        """Ejecuta la aplicación"""
        self.root.mainloop()


def main():
    """Función principal - SOLO PARA PYTHON - NO MARKDOWN"""
    print("🐍 INICIANDO CON PYTHON DEBUGGER - NO MARKDOWN")
    print("=" * 60)
    print("❌ NO usar Markdown debugger")
    print("✅ SOLO usar Python debugger")
    
    try:
        # Verificar Tkinter
        import tkinter as tk
        print("✅ Tkinter disponible para Python")
        
        # Verificar PIL
        try:
            from PIL import Image, ImageTk
            print("✅ PIL/Pillow disponible para Python")
        except ImportError:
            print("⚠️ PIL/Pillow no disponible")
        
        print("🚀 Creando aplicación con PYTHON...")
        app = RecetasConImagenes()
        
        print("🖼️ Abriendo ventana con PYTHON...")
        print("🐍 Ejecutando con Python debugger únicamente")
        
        # Ejecutar SOLO con Python
        app.ejecutar()
        
    except ImportError as e:
        print(f"❌ Error de Python: {e}")
        print("💡 Ejecuta con: python recetas_con_imagenes.py")
        
    except Exception as e:
        print(f"❌ Error de Python: {e}")
        print("💡 NO uses Markdown debugger, usa Python")


if __name__ == "__main__":
    main()

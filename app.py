from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import get_connection

SEDE_MENU = ['Amberes', 'Azcapotzalco', 'Benito Juárez', 'Iztapalapa']
AREA_MENU = ['Administración', 'Auditorio', 'Calidad', 'Call Center', 'Comunicación', 'Dirección', 'Jurídico', 'Líderes-Call', 'Papelería', 'Psicología', 'Sala de Juntas', 'Secretaría', 'Supervisión-Call', 'TI', 'Terapeutas', 'Trata']
TIPO_EQUIPO_MENU = ['PC', 'Laptop']
QUESTION_MENU = ['Sí', 'No']
METODO_CONEXION_MENU = ['Cableado', 'Wifi', 'Cableado / Wifi']

TABLE_NAME = "inventario"
BG_COLOR = "#2e2f45"
FG_COLOR = "white"
OBSERVATIONS_BTN_COLOR = "#537FE7"
FONT_STYLE_TREEVIEW = "Arial"
FONT_BTN_TUPLE = ("Calibri", 10, "bold")
FONT_TITLE_TUPLE = ("Courier", 28, "bold")
FONT_TUPLE = ("Calibri", 10, "normal")
DELETE_BTN_COLOR = "#820000"
SEARCH_BTN_COLOR = "#567189"
SAVE_BTN_COLOR = "#046A44"
PADY_TITLE = 20
PADY_GRID = 10
PADX_GRID = 10
LINE_ENTRY_COLOR = "#30E3DF"
LINE = 2
OPTIONMENU_WIDTH = 19
ENTRY_WIDTH = 25
SUBMIT_BTN_WIDTH = 15
IMAGE_APP_URL = r'./images/inventario.ico'

window = Tk()
window.grid_rowconfigure(0, weight=1, uniform="rows_g1")
window.grid_rowconfigure(1, weight=5, uniform="rows_g1")
window.grid_columnconfigure(0, weight=3, uniform="cols_g1")
window.grid_columnconfigure(1, weight=1, uniform="cols_g1")
window.state('zoomed')
window.minsize(height=710, width=700)
window.maxsize(height=2000, width=2500)
window.title("Gestor de Inventario")
window.iconbitmap(IMAGE_APP_URL)

main_frame = Frame(window)
main_frame.grid(column=0, row=0, columnspan=2, rowspan=2, sticky="nsew")
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

tabs = ttk.Notebook(main_frame, style="TNotebook")

first_frame = Frame(tabs, bg=BG_COLOR)
second_frame = Frame(tabs, bg=BG_COLOR)
third_frame = Frame(tabs, bg=BG_COLOR)

for i in range(0, 4):
    second_frame.grid_columnconfigure(i, weight=1,  uniform="cols_g1")
    third_frame.grid_columnconfigure(i, weight=1,  uniform="cols_g1")

for i in range(0, 13):
    second_frame.grid_rowconfigure(i, weight=1)

for i in range(4, 18):
    third_frame.grid_rowconfigure(i, weight=1)

##################  INICIO DE LA PESTAÑA 1 - BASE DE DATOS #####################
# INICIO: ORDENAR COLUMNAS POR ASCENDENTE Ó DESCENDENTE
def sort_by(order_by, asc_or_desc):
    conexion = get_connection()
    with conexion.cursor() as cursor:
        sql_insert = f'SELECT * FROM inventario ORDER BY {order_by} {asc_or_desc}'
        cursor.execute(sql_insert)
        db = cursor.fetchall()
        conexion.close()
    return db


def insert_row(function_sort_by):
    items = table.get_children()
    for row in items:
        table.delete(row)
    val = function_sort_by
    _count = 0
    for i in range(len(val)):
        if _count % 2 == 0: 
            table.insert('', END, text=val[i][0], values=val[i][1:], tags=('evenrow'))
        else:
            table.insert('', END, text=val[i][0], values=val[i][1:], tags=('oddrow'))
        _count += 1


id_global_count = 1
def sort_by_id(column_name='id'):
    global id_global_count
    if id_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        id_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        id_global_count -= 3

sede_global_count = 1
def sort_by_sede(column_name='sede'):
    global sede_global_count
    if sede_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        sede_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        sede_global_count -= 3

area_global_count = 1
def sort_by_area(column_name='area'):
    global area_global_count
    if area_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        area_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        area_global_count -= 3

tipo_equipo_global_count = 1
def sort_by_tipo_equipo(column_name='tipo_equipo'):
    global tipo_equipo_global_count
    if tipo_equipo_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        tipo_equipo_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        tipo_equipo_global_count -= 3

nombre_equipo_global_count = 1
def sort_by_nombre_equipo(column_name='nombre_equipo'):
    global nombre_equipo_global_count
    if nombre_equipo_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        nombre_equipo_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        nombre_equipo_global_count -= 3

modelo_global_count = 1
def sort_by_modelo(column_name='modelo'):
    global modelo_global_count
    if modelo_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        modelo_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        modelo_global_count -= 3

tiene_monitor_global_count = 1
def sort_by_tiene_monitor(column_name='tiene_monitor'):
    global tiene_monitor_global_count
    if tiene_monitor_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        tiene_monitor_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        tiene_monitor_global_count -= 3

marca_monitor_global_count = 1
def sort_by_marca_monitor(column_name='marca_monitor'):
    global marca_monitor_global_count
    if marca_monitor_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        marca_monitor_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        marca_monitor_global_count -= 3

num_serie_global_count = 1
def sort_by_num_serie(column_name='num_serie'):
    global num_serie_global_count
    if num_serie_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        num_serie_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        num_serie_global_count -= 3

num_inventario_global_count = 1
def sort_by_num_inventario(column_name='num_inventario'):
    global num_inventario_global_count
    if num_inventario_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        num_inventario_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        num_inventario_global_count -= 3

caracteristicas_equipo_global_count = 1
def sort_by_caracteristicas_equipo(column_name='caracteristicas_equipo'):
    global caracteristicas_equipo_global_count
    if caracteristicas_equipo_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        caracteristicas_equipo_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        caracteristicas_equipo_global_count -= 3

usuario_global_count = 1
def sort_by_usuario(column_name='usuario'):
    global usuario_global_count
    if usuario_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        usuario_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        usuario_global_count -= 3

ip_global_count = 1
def sort_by_ip(column_name='ip'):
    global ip_global_count
    if ip_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        ip_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        ip_global_count -= 3

metodo_conexion_global_count = 1
def sort_by_metodo_conexion(column_name='metodo_conexion'):
    global metodo_conexion_global_count
    if metodo_conexion_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        metodo_conexion_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        metodo_conexion_global_count -= 3

bitdefender_global_count = 1
def sort_by_bitdefender(column_name='bitdefender'):
    global bitdefender_global_count
    if bitdefender_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        bitdefender_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        bitdefender_global_count -= 3

tiene_global_global_count = 1
def sort_by_tiene_global(column_name='tiene_global'):
    global tiene_global_global_count
    if tiene_global_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        tiene_global_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        tiene_global_global_count -= 3

agente_global_global_count = 1
def sort_by_agente_global(column_name='agente_global'):
    global agente_global_global_count
    if agente_global_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        agente_global_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        agente_global_global_count -= 3

cuenta_impresora_global_count = 1
def sort_by_cuenta_impresora(column_name='cuenta_impresora'):
    global cuenta_impresora_global_count
    if cuenta_impresora_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        cuenta_impresora_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        cuenta_impresora_global_count -= 3

pin_impresora_global_count = 1
def sort_by_pin_impresora(column_name='pin_impresora'):
    global pin_impresora_global_count
    if pin_impresora_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        pin_impresora_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        pin_impresora_global_count -= 3

no_break_global_count = 1
def sort_by_no_break(column_name='no_break'):
    global no_break_global_count
    if no_break_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        no_break_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        no_break_global_count -= 3

num_extension_global_count = 1
def sort_by_num_extension(column_name='num_extension'):
    global num_extension_global_count
    if num_extension_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        num_extension_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        num_extension_global_count -= 3

nombre_extension_global_count = 1
def sort_by_nombre_extension(column_name='nombre_extension'):
    global nombre_extension_global_count
    if nombre_extension_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        nombre_extension_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        nombre_extension_global_count -= 3

observaciones_global_count = 1
def sort_by_observaciones(column_name='observaciones'):
    global observaciones_global_count
    if observaciones_global_count == 1:
        insert_row(sort_by(column_name, 'asc'))
        observaciones_global_count += 3
    else:
        insert_row(sort_by(column_name, 'desc'))
        observaciones_global_count -= 3
# FIN: ORDENAR COLUMNAS POR ASCENDENTE Ó DESCENDENTE

def please_select_record():
    messagebox.showwarning(title="Advertencia", message="Primero seleccione un registro.")
    

def update_successful_message():
    messagebox.showinfo(title="Actualización del Registro", message="¡Se ha actualizado exitosamente el registro!")


def show_records():
    global count
    count = 0
    table.tag_configure('evenrow', background='white')
    table.tag_configure('oddrow', background='lightgray')
    conexion = get_connection()
    with conexion.cursor() as cursor:
        sql_insert = f'SELECT * FROM {TABLE_NAME}'
        cursor.execute(sql_insert)
        db_values = cursor.fetchall()
        if len(db_values) > 0:
            for index in range(0, len(db_values)):
                if count % 2 == 0:
                    table.insert("", index, text=db_values[index][0], values = db_values[index][1:], tags=('evenrow'))
                else:
                    table.insert("", index, text=db_values[index][0], values = db_values[index][1:], tags=('oddrow'))
                count += 1


def delete_record():
    selected_row = table.focus()
    if len(selected_row) > 3:
        id_selected_row = table.item(selected_row, option="text")
        delete_question = messagebox.askokcancel(title="Eliminar Registro", message="¿Estás seguro que deseas eliminarlo?")
        if delete_question == True:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                sql_insert = '''DELETE FROM {} WHERE id='{}';'''.format(TABLE_NAME, id_selected_row)
                # print(sql_insert)
                cursor.execute(sql_insert)
                conexion.commit()
                conexion.close()
            table.delete(selected_row)
    else:
        please_select_record()


def view_observations():
    selected_row = table.focus()
    selected_row_data = table.item(selected_row)
    id_ = selected_row_data['text']
    if id_ == '':
        please_select_record()
    else:
        view_observations_window = Toplevel()
        view_observations_window.title("Observaciones")
        view_observations_window.minsize(height=250, width=400)
        view_observations_window.maxsize(height=250, width=400)
        view_observations_window.iconbitmap(IMAGE_APP_URL)
        
        view_observations_input = Text(view_observations_window)
        view_observations_input.grid(column=0, row=0)

        observations = selected_row_data['values'][21]
        view_observations_input.insert(END, observations)

        view_observations_input.config(state=DISABLED)
        update_record_button.config(state=DISABLED)
        delete_record_button.config(state=DISABLED)
        view_observations_button.config(state=DISABLED)

        def on_close():
            view_observations_window.destroy()
            update_record_button.config(state=NORMAL)
            delete_record_button.config(state=NORMAL)
            view_observations_button.config(state=NORMAL)
        view_observations_window.protocol("WM_DELETE_WINDOW", on_close)


def character_limiter(assigned_range, *entry_text_args):
    entry_text_args_list = [*entry_text_args]
    is_exceeded_char = []
    for word_entry in entry_text_args_list:
        if len(word_entry) > assigned_range:
            is_exceeded_char.append(True)
    if True in is_exceeded_char:
        return True
    return False


def pc_names_founder(nombre_equipo_get):
    names_founded = []
    conexion = get_connection()
    with conexion.cursor() as cursor:
        sql_insert = f'SELECT nombre_equipo FROM {TABLE_NAME}'
        cursor.execute(sql_insert)
        db_nombre_de_equipos = cursor.fetchall()
        conexion.close()
        for nombre_equipo in db_nombre_de_equipos:
            str_names = str(nombre_equipo[0])
            names_founded.append(str_names.upper())
    if nombre_equipo_get in names_founded:
        return True
    return False


def ip_founder(ip_get):
    ip_founded = []
    conexion = get_connection()
    with conexion.cursor() as cursor:
        sql_insert = f'SELECT ip FROM {TABLE_NAME}'
        cursor.execute(sql_insert)
        db_ips = cursor.fetchall()
        conexion.close()
        for ip in db_ips:
            str_names = str(ip[0])
            ip_founded.append(str_names.upper())
    # print(ip_founded)
    if ip_get in ip_founded:
        return True
    return False



def item_founder_pc_names(selected_row_item):
    items = table.get_children()
    for item in items:
        nombre_equipo = table.item(item)['values'][3]
        if selected_row_item == nombre_equipo:
            return item


def pc_names_founder_edit(selected_row_item, nombre_equipo_get):
    names_founded = []
    get_value_item_founder = item_founder_pc_names(selected_row_item)
    items = table.get_children()
    for item in items:
        nombre_equipo = table.item(item)['values'][3]
        if item == get_value_item_founder:
            pass
        else:
            names_founded.append(nombre_equipo)
    if nombre_equipo_get in names_founded:
        return True
    return False


def item_founder_ip(selected_row_item):
    items = table.get_children()
    for item in items:
        ip = table.item(item)['values'][11]
        if selected_row_item == ip:
            return item


def ip_founder_edit(selected_row_item, ip_equipo_get):
    ip_founded = []
    get_value_item_founder = item_founder_ip(selected_row_item)
    items = table.get_children()
    for item in items:
        ip_equipo = table.item(item)['values'][11]
        if item == get_value_item_founder:
            pass
        else:
            ip_founded.append(ip_equipo)
    if ip_equipo_get in ip_founded:
        return True
    return False

####################################  INICIO VENTANA 2 - EDITAR REGISTRO EN BASE DE DATOS #######################################
def selected_record_section():

    def successfully_updated():
        update_successful_message()
        on_close()

    def w2_add_observations():
        w2_add_observations_window = Toplevel()
        w2_add_observations_window.title("Editar Observaciones")
        w2_add_observations_window.minsize(height=250, width=400)
        w2_add_observations_window.maxsize(height=250, width=400)
        w2_add_observations_window.iconbitmap(IMAGE_APP_URL)
        
        w2_add_observations_input = Text(w2_add_observations_window)
        w2_add_observations_input.pack()
        w2_add_observations_input.insert(END, w2_observaciones_input.get())
        w2_observaciones_input.delete(0, END)

        w2_submit_btn.config(state=DISABLED)
        w2_observaciones_input.config(state=DISABLED)

        def on_close_edit_observations_w():
            w2_submit_btn.config(state=NORMAL)
            w2_observaciones_input.config(state=NORMAL)
            w2_observaciones_input.insert(0, w2_add_observations_input.get('1.0', 'end-1c'))
            w2_add_observations_window.destroy()
        w2_add_observations_window.protocol("WM_DELETE_WINDOW", on_close_edit_observations_w)

    selected_row = table.focus()
    items = table.get_children()
    w2_selected_row_values = table.item(selected_row)

    if selected_row in items:
        w2_sede_name = w2_selected_row_values['values'][0]
        w2_area_name = w2_selected_row_values['values'][1]
        w2_tipo_equipo = w2_selected_row_values['values'][2]
        w2_tiene_monitor = w2_selected_row_values['values'][5]
        w2_metodo_conexion = w2_selected_row_values['values'][12]
        w2_bitdefender = w2_selected_row_values['values'][13]
        w2_global = w2_selected_row_values['values'][14]
        w2_no_break = w2_selected_row_values['values'][18]

        def insert_values():

            index_sede = SEDE_MENU.index(w2_sede_name)           
            w2_sede_value_option_menu.set(SEDE_MENU[index_sede])

            index_area = AREA_MENU.index(w2_area_name)   
            w2_area_value_option_menu.set(AREA_MENU[index_area])

            index_equipo = TIPO_EQUIPO_MENU.index(w2_tipo_equipo)
            w2_equipo_value_option_menu.set(TIPO_EQUIPO_MENU[index_equipo])
         
            w2_nombre_equipo_input.insert(0, w2_selected_row_values['values'][3].upper())
            w2_modelo_input.insert(0, w2_selected_row_values['values'][4])

            index_tiene_monitor = QUESTION_MENU.index(w2_tiene_monitor)
            w2_tiene_monitor_value_option_menu.set(QUESTION_MENU[index_tiene_monitor])

            w2_marca_monitor_input.insert(0, w2_selected_row_values['values'][6])
            w2_num_serie_input.insert(0, w2_selected_row_values['values'][7])
            w2_num_inventario_input.insert(0, w2_selected_row_values['values'][8])
            w2_caracteristicas_input.insert(0, w2_selected_row_values['values'][9])
            w2_usuario_input.insert(0, w2_selected_row_values['values'][10])
            w2_ip_input.insert(0, w2_selected_row_values['values'][11])

            index_metodo_conexion = METODO_CONEXION_MENU.index(w2_metodo_conexion)
            w2_conexion_value_option_menu.set(METODO_CONEXION_MENU[index_metodo_conexion])

            index_bitdefender = QUESTION_MENU.index(w2_bitdefender)
            w2_bitdefender_value_option_menu.set(QUESTION_MENU[index_bitdefender])

            index_global = QUESTION_MENU.index(w2_global)
            w2_global_value_option_menu.set(QUESTION_MENU[index_global])

            w2_agente_global_input.insert(0, w2_selected_row_values['values'][15])
            w2_impresora_input.insert(0, w2_selected_row_values['values'][16])
            w2_pin_impresora_input.insert(0, w2_selected_row_values['values'][17])

            index_no_break = QUESTION_MENU.index(w2_no_break)
            w2_no_break_value_option_menu.set(QUESTION_MENU[index_no_break])

            w2_num_extension_input.insert(0, w2_selected_row_values['values'][19])
            w2_nombre_extension_input.insert(0, w2_selected_row_values['values'][20])
            w2_observaciones_input.insert(0, w2_selected_row_values['values'][21])

        def w2_update_record_section():

            def w2_update_record():
                conexion = get_connection()
                with conexion.cursor() as cursor:
                    sql_insert = '''UPDATE {} 
                    SET sede='{}',
                        area='{}',
                        tipo_equipo='{}',
                        nombre_equipo='{}',
                        modelo='{}',
                        tiene_monitor='{}',
                        marca_monitor='{}',
                        num_serie='{}',
                        num_inventario='{}',
                        caracteristicas_equipo='{}',
                        usuario='{}',
                        ip='{}',
                        metodo_conexion='{}',
                        bitdefender='{}',
                        tiene_global='{}',
                        agente_global='{}',
                        cuenta_impresora='{}',
                        pin_impresora='{}',
                        no_break='{}',
                        num_extension='{}',
                        nombre_extension='{}',
                        observaciones='{}'
                    WHERE id={};'''.format(
                        TABLE_NAME, 
                        *w2_got_values,
                        w2_selected_row_values['text'])
                    # print(sql_insert)
                    cursor.execute(sql_insert)
                    conexion.commit()
                    conexion.close()
                get_children = table.get_children()
                for children in get_children:
                    table.delete(children)
                show_records()
                successfully_updated()    

            w2_sede_value = w2_sede_value_option_menu.get()
            w2_area_value = w2_area_value_option_menu.get()
            w2_equipo_value = w2_equipo_value_option_menu.get()
            w2_nombre_equipo_value = w2_nombre_equipo_input.get().upper()
            w2_modelo_value = w2_modelo_input.get()
            w2_tiene_monitor_value = w2_tiene_monitor_value_option_menu.get()
            w2_marca_monitor_value = w2_marca_monitor_input.get()
            w2_num_serie_value = w2_num_serie_input.get()
            w2_num_inventario_value = w2_num_inventario_input.get()
            w2_caracteristicas_equipo_value = w2_caracteristicas_input.get()
            w2_usuario_value = w2_usuario_input.get()
            w2_ip_value = w2_ip_input.get()
            w2_conexion_value = w2_conexion_value_option_menu.get()
            w2_bitdefender_value = w2_bitdefender_value_option_menu.get()
            w2_global_value = w2_global_value_option_menu.get()
            w2_agente_global_value = w2_agente_global_input.get()
            w2_impresora_value = w2_impresora_input.get()
            w2_pin_impresora_value = w2_pin_impresora_input.get()
            w2_no_break_value = w2_no_break_value_option_menu.get()
            w2_num_extension_value = w2_num_extension_input.get()
            w2_nombre_extension_value = w2_nombre_extension_input.get()
            w2_observaciones_value = w2_observaciones_input.get()

            w2_got_values = [
                w2_sede_value,
                w2_area_value,
                w2_equipo_value,
                w2_nombre_equipo_value,
                w2_modelo_value,
                w2_tiene_monitor_value,
                w2_marca_monitor_value,
                w2_num_serie_value,
                w2_num_inventario_value,
                w2_caracteristicas_equipo_value,
                w2_usuario_value,
                w2_ip_value,
                w2_conexion_value,
                w2_bitdefender_value,
                w2_global_value,
                w2_agente_global_value,
                w2_impresora_value,
                w2_pin_impresora_value,
                w2_no_break_value,
                w2_num_extension_value,
                w2_nombre_extension_value,
                w2_observaciones_value,
            ]

            w2_values_list = [
                len(w2_nombre_equipo_value), 
                len(w2_modelo_value), 
                len(w2_marca_monitor_value), 
                len(w2_num_serie_value), 
                len(w2_num_inventario_value), 
                len(w2_caracteristicas_equipo_value),
                len(w2_usuario_value), 
                len(w2_ip_value),
                len(w2_conexion_value),
                len(w2_bitdefender_value),
                len(w2_global_value),
                len(w2_agente_global_value),
                len(w2_impresora_value),
                len(w2_pin_impresora_value),
                len(w2_no_break_value),
                len(w2_num_extension_value),
                len(w2_nombre_extension_value),
                len(w2_observaciones_value)
            ]
            is_a_w2_empty_field = False
            for w2_value in w2_values_list:
                if w2_value == 0:
                    is_a_w2_empty_field = True

            # INCIO: LIMITANDO CARACTERES DE LA VENTANA 2
            w2_five_character = [
                w2_tiene_monitor_value_option_menu.get(),
                w2_bitdefender_value_option_menu.get(),
                w2_global_value_option_menu.get(),
                w2_no_break_value_option_menu.get(),
                w2_num_extension_input.get()
                ]
            
            w2_twenty_character = [
                w2_sede_value_option_menu.get(),
                w2_area_value_option_menu.get(),
                w2_equipo_value_option_menu.get(),
                w2_nombre_equipo_input.get(),
                w2_marca_monitor_input.get(),
                w2_num_serie_input.get(),
                w2_num_inventario_input.get(),
                w2_ip_input.get(),
                w2_conexion_value_option_menu.get(),
                w2_agente_global_input.get(),
                w2_impresora_input.get(),
            ]
            
            w2_fifty_character = [
                w2_modelo_input.get(),
                w2_caracteristicas_input.get(),
                w2_usuario_input.get(),
                w2_nombre_extension_input.get()
            ]

            w2_are_too_much_chars_5 = character_limiter(5, *w2_five_character)
            w2_are_too_much_chars_20 = character_limiter(20, *w2_twenty_character)
            w2_are_too_much_chars_50 = character_limiter(50, *w2_fifty_character)
            w2_are_too_much_chars_250 = character_limiter(250, w2_observaciones_input.get())
            # FIN: LIMITANDO CARACTERES DE LA VENTANA 2

            w2_repeated_name = pc_names_founder_edit(w2_selected_row_values['values'][3], w2_nombre_equipo_input.get().upper())
            w2_repeated_ip = ip_founder_edit(w2_selected_row_values['values'][11], w2_ip_input.get())

            if w2_are_too_much_chars_5 or w2_are_too_much_chars_20 or w2_are_too_much_chars_50 or w2_are_too_much_chars_250:
                messagebox.showerror(title='Error', message='Uno o más campos exeden el número de caractéres permitidos. Pulsa el botón de ayuda que está en la pestaña de "Añadir Registro" para conocer más acerca de este error.')
            elif w2_repeated_name and len(w2_nombre_equipo_input.get()) > 0:
                messagebox.showerror(title='Duplicación en el Nombre del Equipo', message='Este nombre de equipo ya está en uso. Intente con otro.')
            elif w2_repeated_ip and len(w2_ip_input.get()) > 0:
                messagebox.showerror(title='Duplicación en la IP', message='Esta IP ya está en uso. Intente con otra.')
            elif is_a_w2_empty_field:
                question = messagebox.askokcancel(title='Advertencia', message='Uno o más campos están vacios. ¿Deseas continuar?')
                if question:
                    w2_update_record()
            else:
                w2_update_record()


        window2 = Toplevel()
        window2.title("Editar Registro")
        window2.minsize(height=400, width=650)
        window2.maxsize(height=600, width=650)
        window2.iconbitmap(IMAGE_APP_URL)
        window2.config(bg=BG_COLOR)

        update_record_button.config(state=DISABLED)
        delete_record_button.config(state=DISABLED)
        view_observations_button.config(state=DISABLED)

        title_label = Label(window2, text="Editar Registro", bg=BG_COLOR,  fg=FG_COLOR, font=FONT_TITLE_TUPLE)
        title_label.grid(column=0, row=0, columnspan=4, sticky='nsew', pady=PADY_TITLE)

        w2_sede_value_option_menu = StringVar()
        w2_sede_value_option_menu.set('')
        w2_sede_label = Label(window2, text="Sede", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_sede_label.grid(column=0, row=2, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_sede_input = OptionMenu(window2, w2_sede_value_option_menu, *SEDE_MENU)
        w2_sede_input.grid(column=1, row=2, sticky='w', pady=PADY_GRID)
        w2_sede_input.config(width=OPTIONMENU_WIDTH)

        w2_area_value_option_menu = StringVar()
        w2_area_value_option_menu.set('')
        w2_area_label = Label(window2, text="Area", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_area_label.grid(column=2, row=2, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_area_input = OptionMenu(window2, w2_area_value_option_menu, *AREA_MENU)
        w2_area_input.grid(column=3, row=2, sticky='w', pady=PADY_GRID)
        w2_area_input.config(width=OPTIONMENU_WIDTH)

        w2_equipo_value_option_menu = StringVar()
        w2_equipo_value_option_menu.set('')
        w2_equipo_label = Label(window2, text="Equipo", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_equipo_label.grid(column=0, row=3, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_equipo_input = OptionMenu(window2, w2_equipo_value_option_menu, *TIPO_EQUIPO_MENU)
        w2_equipo_input.grid(column=1, row=3, sticky='w')
        w2_equipo_input.config(width=OPTIONMENU_WIDTH)

        w2_nombre_equipo_label = Label(window2, text="Nombre del Equipo", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_nombre_equipo_label.grid(column=2, row=3, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_nombre_equipo_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_nombre_equipo_input.grid(column=3, row=3, sticky='w')

        w2_modelo_label = Label(window2, text="Modelo", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_modelo_label.grid(column=0, row=4, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_modelo_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_modelo_input.grid(column=1, row=4, sticky='w')

        w2_tiene_monitor_value_option_menu = StringVar()
        w2_tiene_monitor_value_option_menu.set('')
        w2_tiene_monitor_label = Label(window2, text="Tiene Monitor?", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_tiene_monitor_label.grid(column=2, row=4, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_tiene_monitor_input = OptionMenu(window2, w2_tiene_monitor_value_option_menu, *QUESTION_MENU)
        w2_tiene_monitor_input.grid(column=3, row=4, sticky='w')
        w2_tiene_monitor_input.config(width=OPTIONMENU_WIDTH)

        w2_marca_monitor_label = Label(window2, text="Marca del Monitor", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_marca_monitor_label.grid(column=0, row=5, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_marca_monitor_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_marca_monitor_input.grid(column=1, row=5, sticky='w')

        w2_num_serie_label = Label(window2, text="No. de Serie", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_num_serie_label.grid(column=2, row=5, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_num_serie_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_num_serie_input.grid(column=3, row=5, sticky='w')

        w2_num_inventario_label = Label(window2, text="No. de Inventario", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_num_inventario_label.grid(column=0, row=6, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_num_inventario_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_num_inventario_input.grid(column=1, row=6, sticky='w')

        w2_caracteristicas_label = Label(window2, text="Características de Equipo", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_caracteristicas_label.grid(column=2, row=6, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
        w2_caracteristicas_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_caracteristicas_input.grid(column=3, row=6, sticky='w')

        w2_usuario_label = Label(window2, text="Usuario", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_usuario_label.grid(column=0, row=7, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_usuario_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_usuario_input.grid(column=1, row=7, sticky='w')

        w2_ip_label = Label(window2, text="IP", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_ip_label.grid(column=2, row=7, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
        w2_ip_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_ip_input.grid(column=3, row=7, sticky='w')

        w2_conexion_value_option_menu = StringVar()
        w2_conexion_value_option_menu.set('')
        w2_conexion_label = Label(window2, text="Método de Conexión", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_conexion_label.grid(column=0, row=8, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_conexion_input = OptionMenu(window2, w2_conexion_value_option_menu, *METODO_CONEXION_MENU)
        w2_conexion_input.grid(column=1, row=8, sticky='w')
        w2_conexion_input.config(width=OPTIONMENU_WIDTH)

        w2_bitdefender_value_option_menu = StringVar()
        w2_bitdefender_value_option_menu.set('')
        w2_bitdefender_label = Label(window2, text="Tiene Bitdefender?", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_bitdefender_label.grid(column=2, row=8, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
        w2_bitdefender_input = OptionMenu(window2, w2_bitdefender_value_option_menu, *QUESTION_MENU)
        w2_bitdefender_input.grid(column=3, row=8, sticky='w')
        w2_bitdefender_input.config(width=OPTIONMENU_WIDTH)

        w2_global_value_option_menu = StringVar()
        w2_global_value_option_menu.set('')
        w2_global_label = Label(window2, text="¿Tiene Global?", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_global_label.grid(column=0, row=9, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_global_input = OptionMenu(window2, w2_global_value_option_menu, *QUESTION_MENU)
        w2_global_input.grid(column=1, row=9, sticky='w')
        w2_global_input.config(width=OPTIONMENU_WIDTH)

        w2_agente_global_label = Label(window2, text="Agente del Global", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_agente_global_label.grid(column=2, row=9, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
        w2_agente_global_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_agente_global_input.grid(column=3, row=9, sticky='w')

        w2_impresora_label = Label(window2, text="Cuenta de Impresora", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_impresora_label.grid(column=0, row=10, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_impresora_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_impresora_input.grid(column=1, row=10, sticky='w')

        w2_pin_impresora_label = Label(window2, text="Pin de Impresora", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_pin_impresora_label.grid(column=2, row=10, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
        w2_pin_impresora_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_pin_impresora_input.grid(column=3, row=10, sticky='w')

        w2_no_break_value_option_menu = StringVar()
        w2_no_break_value_option_menu.set('')
        w2_no_break_label = Label(window2, text="¿Tiene No Break?", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_no_break_label.grid(column=0, row=11, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_no_break_input = OptionMenu(window2, w2_no_break_value_option_menu, *QUESTION_MENU)
        w2_no_break_input.grid(column=1, row=11, sticky='w')
        w2_no_break_input.config(width=OPTIONMENU_WIDTH)

        w2_num_extension_label = Label(window2, text="Número de Extensión", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_num_extension_label.grid(column=2, row=11, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
        w2_num_extension_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_num_extension_input.grid(column=3, row=11, sticky='w')

        w2_nombre_extension_label = Label(window2, text="Nombre de la Extensión", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_nombre_extension_label.grid(column=0, row=12, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
        w2_nombre_extension_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_nombre_extension_input.grid(column=1, row=12, sticky='w')

        w2_observaciones_label = Label(window2, text="Observaciones", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
        w2_observaciones_label.grid(column=2, row=12, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
        w2_observaciones_input = Entry(window2, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
        w2_observaciones_input.grid(column=3, row=12, sticky='w')

        insert_values()

        w2_submit_btn = Button(window2, text="Guardar", command=w2_update_record_section, bg=SAVE_BTN_COLOR, fg=FG_COLOR, font=FONT_BTN_TUPLE, width=SUBMIT_BTN_WIDTH)
        w2_submit_btn.grid(column=1, row=13, columnspan=2, sticky='s', pady=PADY_GRID)

        w2_add_observations_btn = Button(window2, text="Ampliar Campo", command=w2_add_observations, bg=OBSERVATIONS_BTN_COLOR, fg=FG_COLOR, width=SUBMIT_BTN_WIDTH)
        w2_add_observations_btn.grid(column=3, row=13, sticky='w', pady=PADY_GRID)

        def on_close():
            window2.destroy()
            update_record_button.config(state=NORMAL)
            delete_record_button.config(state=NORMAL)
            view_observations_button.config(state=NORMAL)

        window2.protocol("WM_DELETE_WINDOW", on_close)

        # INICIO: HACER QUE LA TECLA ENTER FUNCIONE PARA LA VENTANA 2
        w2_input_list = [
            w2_nombre_equipo_input,
            w2_modelo_input,
            w2_marca_monitor_input,
            w2_num_serie_input,
            w2_num_inventario_input,
            w2_caracteristicas_input,
            w2_usuario_input,
            w2_ip_input,
            w2_agente_global_input,
            w2_impresora_input,
            w2_pin_impresora_input,
            w2_num_extension_input,
            w2_nombre_extension_input,
            w2_observaciones_input,
            w2_submit_btn
        ]

        for w2_input_name in w2_input_list:
            w2_input_name.bind('<Return>', (lambda event: w2_update_record_section()))
        # FIN: HACER QUE LA TECLA ENTER FUNCIONE PARA LA VENTANA 2

    else:
        please_select_record()
##################  FIN VENTANA 2 - AGREGAR REGISTRO EN BASE DE DATOS #####################

title_label = Label(first_frame, text="Base de Datos", bg=BG_COLOR, fg=FG_COLOR, pady=PADY_TITLE, font=FONT_TITLE_TUPLE)
title_label.pack(expand=True, fill=X)

delete_record_button = Button(first_frame, text="Eliminar Registro Seleccionado", command=delete_record, bg=DELETE_BTN_COLOR, fg=FG_COLOR, font=FONT_BTN_TUPLE, width=25)
delete_record_button.pack(pady=10)

update_record_button = Button(first_frame, text="Actualizar Registro Seleccionado", command=selected_record_section, bg=SAVE_BTN_COLOR, fg=FG_COLOR, font=FONT_BTN_TUPLE, width=25)
update_record_button.pack(pady=10)

view_observations_button = Button(first_frame, text="Ver Observaciones del Registro", command=view_observations, bg=OBSERVATIONS_BTN_COLOR, fg=FG_COLOR, font=FONT_BTN_TUPLE, width=25)
view_observations_button.pack(pady=10)

scroll=Scrollbar(first_frame, orient='horizontal')
scroll.pack(side=BOTTOM, fill='x')

scrollbar_v = Scrollbar(first_frame)
scrollbar_v.pack(side=RIGHT, fill='y')

sort_by_list = [
    sort_by_sede,
    sort_by_area,
    sort_by_tipo_equipo,
    sort_by_nombre_equipo,
    sort_by_modelo,
    sort_by_tiene_monitor,
    sort_by_marca_monitor,
    sort_by_num_serie,
    sort_by_num_inventario,
    sort_by_caracteristicas_equipo,
    sort_by_usuario,
    sort_by_ip,
    sort_by_metodo_conexion,
    sort_by_bitdefender,
    sort_by_tiene_global,
    sort_by_agente_global,
    sort_by_cuenta_impresora,
    sort_by_pin_impresora,
    sort_by_no_break,
    sort_by_num_extension,
    sort_by_nombre_extension,
    sort_by_observaciones
]

text_heading_list = [
    "Sede",
    "Área",
    "Equipo",
    "Nombre del Equipo",
    "Modelo",
    "¿Tiene monitor?",
    "Marca del Monitor",
    "No. de Serie",
    "No. de Inventario",
    "Características del Equipo",
    "Usuario",
    "IP",
    "Metodo de Conexión",
    "¿Tiene Bitdefender?",
    "¿Tiene Global?",
    "Agente del Global",
    "Cuenta de Impresora",
    "Pin de Impresora",
    "¿Tiene No Break?",
    "Número de Extensión",
    "Nombre de la Extensión",
    "Observaciones",
]

table_columns_list = [
    "sede",
    "area",
    "tipo_equipo",
    "nombre_equipo",
    "modelo",
    "tiene_monitor",
    "marca_monitor",
    "num_serie",
    "num_inventario",
    "caracteristicas_equipo",
    "usuario",
    "ip",
    "metodo_conexion",
    "bitdefender",
    "tiene_global",
    "agente_global",
    "cuenta_impresora",
    "pin_impresora",
    "no_break",
    "num_extension",
    "nombre_extension",
    "observaciones"
]

table = ttk.Treeview(first_frame, xscrollcommand=scroll.set, yscrollcommand=scrollbar_v.set, columns=(table_columns_list))

table.heading("#0", text="ID", command=sort_by_id)
for i in range(len(text_heading_list)):
    table.heading(table_columns_list[i], text=text_heading_list[i], command=sort_by_list[i])

# INICIO: ASIGNANDO TAMAÑO A LAS COLUMNAS
table_heading_names = [
    'sede', 
    'area', 
    'tipo_equipo', 
    'nombre_equipo', 
    'tiene_monitor', 
    'marca_monitor', 
    'num_serie', 
    'num_inventario',
    'usuario', 
    'metodo_conexion', 
    'bitdefender', 
    'tiene_global', 
    'agente_global', 
    'cuenta_impresora', 
    'pin_impresora',
    'pin_impresora', 
    'no_break', 
    'num_extension', 
    'nombre_extension', 
    'observaciones'
]

table_heading_small_names = ['#0', 'ip']

table_heading_large_names = ['modelo', 'caracteristicas_equipo']

for heading_name in table_heading_names:
    table.column(heading_name, width=200, minwidth=200)

for heading_name in table_heading_small_names:
    table.column(heading_name, width=100, minwidth=80)

for heading_name in table_heading_large_names:
    table.column(heading_name, width=300, minwidth=300)
# FIN: ASIGNANDO TAMAÑO A LAS COLUMNAS

table.pack(expand=True, fill=Y)

scroll.config(command=table.xview)
scrollbar_v.config(command=table.yview)

show_records()
####################################  FIN DE LA PESTAÑA 1 - BASE DE DATOS #######################################

####################################  INICIO DE LA PESTAÑA 2 - AÑADIR REGISTROS #######################################
def add_observations():
    add_observations_window = Toplevel()
    add_observations_window.title("Añadir Observaciones")
    add_observations_window.minsize(height=250, width=400)
    add_observations_window.maxsize(height=250, width=400)
    add_observations_window.iconbitmap(IMAGE_APP_URL)
    
    add_observations_input = Text(add_observations_window)
    add_observations_input.pack()
    add_observations_input.insert(END, observaciones_input.get())
    observaciones_input.delete(0, END)

    submit_btn.config(state=DISABLED)
    observaciones_input.config(state=DISABLED)

    def on_close():
        submit_btn.config(state=NORMAL)
        observaciones_input.config(state=NORMAL)
        observaciones_input.insert(0, add_observations_input.get('1.0', 'end-1c'))
        add_observations_window.destroy()
    add_observations_window.protocol("WM_DELETE_WINDOW", on_close)


def add_record_section():

    def add_record():
        conexion = get_connection()
        with conexion.cursor() as cursor:
            sql_insert = '''INSERT INTO {} (
                sede,
                area,
                tipo_equipo,
                nombre_equipo,
                modelo,
                tiene_monitor,
                marca_monitor,
                num_serie,
                num_inventario,
                caracteristicas_equipo,
                usuario,
                ip,
                metodo_conexion,
                bitdefender,
                tiene_global, 
                agente_global, 
                cuenta_impresora,
                pin_impresora,
                no_break,
                num_extension,
                nombre_extension,
                observaciones
                ) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');'''.format(
                    TABLE_NAME, 
                    *got_values
                    )
            # print(sql_insert)
            cursor.execute(sql_insert)
            conexion.commit()
            conexion.close()
        items = table.get_children()
        if len(items) >= 1:
            for item in items:
                table.delete(item)
        show_records()

        fields_to_clean = [
            nombre_equipo_input, 
            modelo_input,
            marca_monitor_input, 
            num_serie_input,
            num_inventario_input,
            caracteristicas_input,
            usuario_input,
            ip_input,
            agente_global_input,
            impresora_input,
            pin_impresora_input,
            num_extension_input,
            nombre_extension_input,
            observaciones_input
            ]

        for field in fields_to_clean:
            field.delete(0, END)


    got_values = [
        sede_value_option_menu.get(),
        area_value_option_menu.get(),
        equipo_value_option_menu.get(),
        nombre_equipo_input.get().upper(),
        modelo_input.get(),
        tiene_monitor_value_option_menu.get(),
        marca_monitor_input.get(),
        num_serie_input.get(),
        num_inventario_input.get(),
        caracteristicas_input.get(),
        usuario_input.get(),
        ip_input.get(),
        conexion_value_option_menu.get(),
        bitdefender_value_option_menu.get(),
        global_value_option_menu.get(),
        agente_global_input.get(),
        impresora_input.get(),
        pin_impresora_input.get(),
        no_break_value_option_menu.get(),
        num_extension_input.get(),
        nombre_extension_input.get(),
        observaciones_input.get()
    ]
    is_field_empty = False
    for value in got_values:
        if len(value) == 0:
            is_field_empty = True

    # INCIO: LIMITANDO CARACTERES DE LA PESTAÑA 2
    five_character = [
        tiene_monitor_value_option_menu.get(),
        bitdefender_value_option_menu.get(),
        global_value_option_menu.get(),
        no_break_value_option_menu.get(),
        num_extension_input.get()
        ]
    
    twenty_character = [
        sede_value_option_menu.get(),
        area_value_option_menu.get(),
        equipo_value_option_menu.get(),
        nombre_equipo_input.get(),
        marca_monitor_input.get(),
        num_serie_input.get(),
        num_inventario_input.get(),
        ip_input.get(),
        conexion_value_option_menu.get(),
        agente_global_input.get(),
        impresora_input.get(),
    ]
    
    fifty_character = [
        modelo_input.get(),
        caracteristicas_input.get(),
        usuario_input.get(),
        nombre_extension_input.get()
    ]

    are_too_much_chars_5 = character_limiter(5, *five_character)
    are_too_much_chars_20 = character_limiter(20, *twenty_character)
    are_too_much_chars_50 = character_limiter(50, *fifty_character)
    are_too_much_chars_250 = character_limiter(250, observaciones_input.get())
    # FIN: LIMITANDO CARACTERES DE LA PESTAÑA 2

    nombre_equipo = pc_names_founder(nombre_equipo_input.get().upper())
    ip_equipo = ip_founder((ip_input.get()))

    if are_too_much_chars_5 or are_too_much_chars_20 or are_too_much_chars_50 or are_too_much_chars_250:
        messagebox.showerror(title='Error', message='Uno o más campos exeden el número de caractéres permitidos. Pulsa el botón de ayuda que está en la pestaña de "Añadir Registro" para conocer más acerca de este error.')
    elif nombre_equipo and len(nombre_equipo_input.get()) > 0:
        messagebox.showerror(title='Duplicación en el Nombre del Equipo', message='Este nombre de equipo ya está en uso. Intente con otro.')
    elif ip_equipo and len(ip_input.get()) > 0:
        messagebox.showerror(title='Duplicación en la IP', message='Esta IP ya está en uso. Intente con otra.')
    else:
        if is_field_empty:
            confirm = messagebox.askokcancel(title="Advertencia", message="Uno o más campos están vacíos. ¿Deseas continuar?")
            if confirm:
                add_record()
                update_successful_message()
        else:
            add_record()
            update_successful_message()

def _help():
    help_window = Toplevel()
    help_window.title('Ventana de Ayuda')
    help_window.minsize(width=688, height=275)
    help_window.maxsize(width=688, height=275)
    help_window.iconbitmap(IMAGE_APP_URL)

    chars_allowed_title = Label(help_window, text='Limite de Caracteres Permitidos', font=FONT_TITLE_TUPLE)
    chars_allowed_title.grid(column=0, row=0, columnspan=2, sticky='nsew')

    info_list = ttk.Treeview(help_window, columns='Tamaño')
    info_list.column('#0', anchor=CENTER)
    info_list.column('Tamaño', anchor=CENTER)
    info_list.heading('#0', text='Campo / Entrada')
    info_list.heading('Tamaño', text='Límite de Caracteres')
    for key_field in field_dictionary: 
        info_list.insert('', END, text=key_field, values=field_dictionary[key_field])
    info_list.grid(column=0, row=1, columnspan=2, rowspan=2, sticky='nsew')
    
    help_window.mainloop()
    
field_dictionary = {
    'Sede': 20,
    'Área': 20,
    'Tipo de Equipo': 20,
    'Nombre de Equipo': 20,
    'Modelo': 50,
    'Tiene Monitor': 5,
    'Marca del Monitor': 20,
    'No. de Serie': 20,
    'No. de Inventario': 20,
    'Caracteristicas del Equipo': 50,
    'Usuario': 50,
    'IP': 20,
    'Método de Conexión': 20,
    'Bitdefender': 5,
    'Tiene Global': 5,
    'Agente Global': 20,
    'Cuenta de Impresora': 20,
    'Pin de Impresora': 5,
    'Tiene No Break': 5,
    'Número de Extensión': 5,
    'Nombre de la Extensión': 50,
    'Observaciones': 250
}

title_label = Label(second_frame, text="Añadir Registro", bg=BG_COLOR,  fg=FG_COLOR, font=FONT_TITLE_TUPLE)
title_label.grid(column=0, row=0, columnspan=4, sticky='nsew', pady=PADY_TITLE)

sede_value_option_menu = StringVar()
sede_value_option_menu.set(SEDE_MENU[0])
sede_label = Label(second_frame, text="Sede", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
sede_label.grid(column=0, row=2, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
sede_input = OptionMenu(second_frame, sede_value_option_menu, *SEDE_MENU)
sede_input.grid(column=1, row=2, sticky='w', pady=PADY_GRID)
sede_input.config(width=OPTIONMENU_WIDTH)

area_value_option_menu = StringVar()
area_value_option_menu.set(AREA_MENU[0])
area_label = Label(second_frame, text="Area", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
area_label.grid(column=2, row=2, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
area_input = OptionMenu(second_frame, area_value_option_menu, *AREA_MENU)
area_input.grid(column=3, row=2, sticky='w', pady=PADY_GRID)
area_input.config(width=OPTIONMENU_WIDTH)

equipo_value_option_menu = StringVar()
equipo_value_option_menu.set(TIPO_EQUIPO_MENU[0])
equipo_label = Label(second_frame, text="Equipo", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
equipo_label.grid(column=0, row=3, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
equipo_input = OptionMenu(second_frame, equipo_value_option_menu, *TIPO_EQUIPO_MENU)
equipo_input.grid(column=1, row=3, sticky='w')
equipo_input.config(width=OPTIONMENU_WIDTH)

nombre_equipo_label = Label(second_frame, text="Nombre del Equipo", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
nombre_equipo_label.grid(column=2, row=3, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
nombre_equipo_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
nombre_equipo_input.grid(column=3, row=3, sticky='w')

modelo_label = Label(second_frame, text="Modelo", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
modelo_label.grid(column=0, row=4, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
modelo_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
modelo_input.grid(column=1, row=4, sticky='w')

tiene_monitor_value_option_menu = StringVar()
tiene_monitor_value_option_menu.set(QUESTION_MENU[0])
tiene_monitor_label = Label(second_frame, text="¿Tiene Monitor?", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
tiene_monitor_label.grid(column=2, row=4, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
tiene_monitor_input = OptionMenu(second_frame, tiene_monitor_value_option_menu, *QUESTION_MENU)
tiene_monitor_input.grid(column=3, row=4, sticky='w')
tiene_monitor_input.config(width=OPTIONMENU_WIDTH)

marca_monitor_label = Label(second_frame, text="Marca del Monitor", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
marca_monitor_label.grid(column=0, row=5, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
marca_monitor_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
marca_monitor_input.grid(column=1, row=5, sticky='w')

num_serie_label = Label(second_frame, text="No. de Serie", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
num_serie_label.grid(column=2, row=5, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
num_serie_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
num_serie_input.grid(column=3, row=5, sticky='w')

num_inventario_label = Label(second_frame, text="No. de Inventario", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
num_inventario_label.grid(column=0, row=6, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
num_inventario_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
num_inventario_input.grid(column=1, row=6, sticky='w')

caracteristicas_label = Label(second_frame, text="Características de Equipo", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
caracteristicas_label.grid(column=2, row=6, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
caracteristicas_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
caracteristicas_input.grid(column=3, row=6, sticky='w')

usuario_label = Label(second_frame, text="Usuario", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
usuario_label.grid(column=0, row=7, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
usuario_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
usuario_input.grid(column=1, row=7, sticky='w')

ip_label = Label(second_frame, text="IP", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
ip_label.grid(column=2, row=7, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
ip_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
ip_input.grid(column=3, row=7, sticky='w')

conexion_value_option_menu = StringVar()
conexion_value_option_menu.set(METODO_CONEXION_MENU[0])
conexion_label = Label(second_frame, text="Método de Conexión", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
conexion_label.grid(column=0, row=8, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
conexion_input = OptionMenu(second_frame, conexion_value_option_menu, *METODO_CONEXION_MENU)
conexion_input.grid(column=1, row=8, sticky='w')
conexion_input.config(width=OPTIONMENU_WIDTH)

bitdefender_value_option_menu = StringVar()
bitdefender_value_option_menu.set(QUESTION_MENU[0])
bitdefender_label = Label(second_frame, text="¿Tiene Bitdefender?", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
bitdefender_label.grid(column=2, row=8, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
bitdefender_input = OptionMenu(second_frame, bitdefender_value_option_menu, *QUESTION_MENU)
bitdefender_input.grid(column=3, row=8, sticky='w')
bitdefender_input.config(width=OPTIONMENU_WIDTH)

global_value_option_menu = StringVar()
global_value_option_menu.set(QUESTION_MENU[0])
global_label = Label(second_frame, text="¿Tiene Global?", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
global_label.grid(column=0, row=9, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
global_input = OptionMenu(second_frame, global_value_option_menu, *QUESTION_MENU)
global_input.grid(column=1, row=9, sticky='w')
global_input.config(width=OPTIONMENU_WIDTH)

agente_global_label = Label(second_frame, text="Agente del Global", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
agente_global_label.grid(column=2, row=9, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
agente_global_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
agente_global_input.grid(column=3, row=9, sticky='w')

impresora_label = Label(second_frame, text="Cuenta de Impresora", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
impresora_label.grid(column=0, row=10, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
impresora_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
impresora_input.grid(column=1, row=10, sticky='w')

pin_impresora_label = Label(second_frame, text="Pin de Impresora", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
pin_impresora_label.grid(column=2, row=10, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
pin_impresora_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
pin_impresora_input.grid(column=3, row=10, sticky='w')

no_break_value_option_menu = StringVar()
no_break_value_option_menu.set(QUESTION_MENU[0])
no_break_label = Label(second_frame, text="¿Tiene No Break?", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
no_break_label.grid(column=0, row=11, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
no_break_input = OptionMenu(second_frame, no_break_value_option_menu, *QUESTION_MENU)
no_break_input.grid(column=1, row=11, sticky='w')
no_break_input.config(width=OPTIONMENU_WIDTH)

num_extension_label = Label(second_frame, text="Número de Extensión", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
num_extension_label.grid(column=2, row=11, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
num_extension_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
num_extension_input.grid(column=3, row=11, sticky='w')

nombre_extension_label = Label(second_frame, text="Nombre de la Extensión", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
nombre_extension_label.grid(column=0, row=12, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
nombre_extension_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
nombre_extension_input.grid(column=1, row=12, sticky='w')

observaciones_label = Label(second_frame, text="Observaciones", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
observaciones_label.grid(column=2, row=12, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
observaciones_input = Entry(second_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
observaciones_input.grid(column=3, row=12, sticky='w')

help_btn = Button(second_frame, text="Ayuda", command=_help, bg='#F55050', fg=FG_COLOR, width=SUBMIT_BTN_WIDTH)
help_btn.grid(column=0, row=13, sticky='e', pady=PADY_GRID)

submit_btn = Button(second_frame, text="Guardar", command=add_record_section, bg=SAVE_BTN_COLOR, fg=FG_COLOR, width=SUBMIT_BTN_WIDTH)
submit_btn.grid(column=1, row=13, columnspan=2, sticky='s', pady=PADY_GRID)

add_observations_btn = Button(second_frame, text="Ampliar Campo", command=add_observations, bg=OBSERVATIONS_BTN_COLOR, fg=FG_COLOR, width=SUBMIT_BTN_WIDTH)
add_observations_btn.grid(column=3, row=13, sticky='w', pady=PADY_GRID)

# INICIO: HACER QUE LA TECLA ENTER FUNCIONE PARA LA PESTAÑA 2
input_list = [
    nombre_equipo_input,
    modelo_input,
    marca_monitor_input,
    num_serie_input,
    num_inventario_input,
    caracteristicas_input,
    usuario_input,
    ip_input,
    agente_global_input,
    impresora_input,
    pin_impresora_input,
    num_extension_input,
    nombre_extension_input,
    observaciones_input,
    submit_btn
    ]

for input_name in input_list:
    input_name.bind('<Return>', (lambda event: add_record_section()))
# FIN: HACER QUE LA TECLA ENTER FUNCIONE PARA LA PESTAÑA 2

####################################  FIN DE LA PESTAÑA 2 - AÑADIR REGISTROS #######################################

####################################  INICIO DE LA PESTAÑA 3 - BUSCAR / EDITAR #######################################
def disable_t3_fields():
    t3_sede_input.config(state=DISABLED)
    t3_area_input.config(state=DISABLED)
    t3_equipo_input.config(state=DISABLED)
    t3_nombre_equipo_input.config(state=DISABLED)
    t3_modelo_input.config(state=DISABLED)
    t3_tiene_monitor_input.config(state=DISABLED)
    t3_marca_monitor_input.config(state=DISABLED)
    t3_num_serie_input.config(state=DISABLED)
    t3_num_inventario_input.config(state=DISABLED)
    t3_caracteristicas_input.config(state=DISABLED)
    t3_usuario_input.config(state=DISABLED)
    t3_ip_input.config(state=DISABLED)
    t3_conexion_input.config(state=DISABLED)
    t3_bitdefender_input.config(state=DISABLED)
    t3_global_input.config(state=DISABLED)
    t3_agente_global_input.config(state=DISABLED)
    t3_impresora_input.config(state=DISABLED)
    t3_pin_impresora_input.config(state=DISABLED)
    t3_no_break_input.config(state=DISABLED)
    t3_num_extension_input.config(state=DISABLED)
    t3_nombre_extension_input.config(state=DISABLED)
    t3_observaciones_input.config(state=DISABLED)
    t3_submit_btn.config(state=DISABLED)
    t3_add_observations_btn.config(state=DISABLED)

def enable_t3_fields():
    t3_sede_input.config(state=NORMAL)
    t3_area_input.config(state=NORMAL)
    t3_equipo_input.config(state=NORMAL)
    t3_nombre_equipo_input.config(state=NORMAL)
    t3_modelo_input.config(state=NORMAL)
    t3_tiene_monitor_input.config(state=NORMAL)
    t3_marca_monitor_input.config(state=NORMAL)
    t3_num_serie_input.config(state=NORMAL)
    t3_num_inventario_input.config(state=NORMAL)
    t3_caracteristicas_input.config(state=NORMAL)
    t3_usuario_input.config(state=NORMAL)
    t3_ip_input.config(state=NORMAL)
    t3_conexion_input.config(state=NORMAL)
    t3_bitdefender_input.config(state=NORMAL)
    t3_global_input.config(state=NORMAL)
    t3_agente_global_input.config(state=NORMAL)
    t3_impresora_input.config(state=NORMAL)
    t3_pin_impresora_input.config(state=NORMAL)
    t3_no_break_input.config(state=NORMAL)
    t3_num_extension_input.config(state=NORMAL)
    t3_nombre_extension_input.config(state=NORMAL)
    t3_observaciones_input.config(state=NORMAL)
    t3_submit_btn.config(state=NORMAL)
    t3_add_observations_btn.config(state=NORMAL)
    


def t3_clean_fields():
    disable_id.config(state=NORMAL)
    disable_id.delete(0, END)
    disable_id.config(state=DISABLED)
    t3_nombre_equipo_input.delete(0, END)
    t3_modelo_input.delete(0, END)
    t3_marca_monitor_input.delete(0, END)
    t3_num_serie_input.delete(0, END)
    t3_num_inventario_input.delete(0, END)
    t3_caracteristicas_input.delete(0, END)
    t3_usuario_input.delete(0, END)
    t3_ip_input.delete(0, END)
    t3_agente_global_input.delete(0, END)
    t3_impresora_input.delete(0, END)
    t3_pin_impresora_input.delete(0, END)
    t3_num_extension_input.delete(0, END)
    t3_caracteristicas_input.delete(0, END)
    t3_nombre_extension_input.delete(0, END)
    t3_observaciones_input.delete(0, END)
    disable_t3_fields()


def t3_all_fields_cleaned():
    id_entry.delete(0, END)
    search_by_name_input.delete(0, END)
    t3_clean_fields()

########### AGREGAR VALORES ###########
def get_t3_len_values():
    len_nombre_equipo = len(t3_nombre_equipo_input.get())
    len_modelo = len(t3_modelo_input.get())
    len_marca_monitor = len(t3_marca_monitor_input.get())
    len_num_serie = len(t3_num_extension_input.get())
    len_num_inventario = len(t3_num_inventario_input.get())
    len_caracteristicas = len(t3_caracteristicas_input.get())
    len_usuario = len(t3_usuario_input.get())
    len_ip = len(t3_ip_input.get())
    len_agente_global = len(t3_agente_global_input.get())
    len_impresora = len(t3_impresora_input.get())
    len_pin_impresora = len(t3_pin_impresora_input.get())
    len_num_extension = len(t3_num_extension_input.get())
    len_nombre_extension = len(t3_nombre_extension_input.get())
    len_observaciones = len(t3_observaciones_input.get())
    return [
        len_nombre_equipo, 
        len_modelo, 
        len_marca_monitor,
        len_num_serie,
        len_num_inventario,
        len_caracteristicas,
        len_usuario,
        len_ip,
        len_agente_global,
        len_impresora,
        len_pin_impresora,
        len_num_extension,
        len_nombre_extension,
        len_observaciones
    ]

########### AGREGAR VALORES ###########
def put_data_in_fields(fetch):
    sede_index_founded = (SEDE_MENU.index(fetch[1]))
    t3_sede_value_option_menu.set(SEDE_MENU[sede_index_founded])
    t3_sede_input.config(state=NORMAL)

    area_index_founded = (AREA_MENU.index(fetch[2]))
    t3_area_value_option_menu.set(AREA_MENU[area_index_founded])
    t3_area_input.config(state=NORMAL)

    equipo_index_founded = (TIPO_EQUIPO_MENU.index(fetch[3]))
    t3_equipo_value_option_menu.set(TIPO_EQUIPO_MENU[equipo_index_founded])
    t3_equipo_input.config(state=NORMAL)

    t3_nombre_equipo_input.insert(0, fetch[4])
    t3_modelo_input.insert(0, fetch[5])

    tiene_monitor_index_founded = (QUESTION_MENU.index(fetch[6]))
    t3_tiene_monitor_value_option_menu.set(QUESTION_MENU[tiene_monitor_index_founded])
    t3_tiene_monitor_input.config(state=NORMAL)

    t3_marca_monitor_input.insert(0, fetch[7])
    t3_num_serie_input.insert(0, fetch[8])
    t3_num_inventario_input.insert(0, fetch[9])
    t3_caracteristicas_input.insert(0, fetch[10])
    t3_usuario_input.insert(0, fetch[11])
    t3_ip_input.insert(0, fetch[12])

    conexion_index_founded = (METODO_CONEXION_MENU.index(fetch[13]))
    t3_conexion_value_option_menu.set(METODO_CONEXION_MENU[conexion_index_founded])
    t3_conexion_input.config(state=NORMAL)

    bitdefender_index_founded = (QUESTION_MENU.index(fetch[14]))
    t3_bitdefender_value_option_menu.set(QUESTION_MENU[bitdefender_index_founded])
    t3_bitdefender_input.config(state=NORMAL)

    global_index_founded = (QUESTION_MENU.index(fetch[15]))
    t3_global_value_option_menu.set(QUESTION_MENU[global_index_founded])
    t3_global_input.config(state=NORMAL)

    t3_agente_global_input.insert(0, fetch[16])
    t3_impresora_input.insert(0, fetch[17])
    t3_pin_impresora_input.insert(0, fetch[18])

    no_break_index_founded = (QUESTION_MENU.index(fetch[19]))
    t3_no_break_value_option_menu.set(QUESTION_MENU[no_break_index_founded])
    t3_no_break_input.config(state=NORMAL)

    t3_num_extension_input.insert(0, fetch[20])
    t3_nombre_extension_input.insert(0, fetch[21])
    t3_observaciones_input.insert(0, fetch[22])

    return [t3_nombre_equipo_input.get(), t3_ip_input.get()]


def get_id():
    conexion = get_connection()
    with conexion.cursor() as cursor:
        sql_insert = '''SELECT id FROM {} WHERE nombre_equipo='{}';'''.format(TABLE_NAME, search_by_name_input.get())
        # print(sql_insert)
        cursor.execute(sql_insert)
        datos = cursor.fetchone()
        conexion.close()
        return datos


def get_id_list():
    items = table.get_children()
    id_list = []
    for index in range(0, len(items)):
        id = table.item(items[index])
        id_list.append(str(id['text']))
    return id_list

def get_name():
    items = table.get_children()
    name_list = []
    for item in items:
        name_list.append(table.item(item)['values'][3].upper())
    return name_list


def search_record_by_id():
    id_lists = get_id_list()
    requested_id = id_entry.get()
    if requested_id in id_lists:
        t3_clean_fields()
        conexion = get_connection()
        with conexion.cursor() as cursor:
            sql_insert = '''SELECT * FROM {} WHERE id='{}';'''.format(TABLE_NAME, requested_id)
            # print(sql_insert)
            cursor.execute(sql_insert)
            info_fetch = cursor.fetchone()
            conexion.commit()
            conexion.close()
        enable_t3_fields()
        global t3_nombre_equipo_search_by_id
        t3_nombre_equipo_search_by_id = put_data_in_fields(info_fetch)
        search_by_name_input.delete(0, END)
    else:
        messagebox.showerror(title="Error", message='ID no encontrado.')
        t3_clean_fields()
        search_by_name_input.delete(0, END)


def search_record_by_name():
        t3_clean_fields()
        id_entry.delete(0, END)
        name_list = get_name()
        if search_by_name_input.get().upper() in name_list:
            requested_name = search_by_name_input.get()
            conexion = get_connection()
            with conexion.cursor() as cursor:
                sql_insert = '''SELECT * FROM {} WHERE nombre_equipo='{}';'''.format(TABLE_NAME, requested_name.upper())
                # print(sql_insert)
                cursor.execute(sql_insert)
                info_fetch = cursor.fetchone()
                conexion.commit()
                conexion.close()        
            disable_id.config(state=NORMAL)
            disable_id.delete(0, END)
            disable_id.insert(0, f'ID: {info_fetch[0]}')
            disable_id.config(state=DISABLED)
            enable_t3_fields()
            global t3_nombre_equipo_search_by_name
            t3_nombre_equipo_search_by_name = put_data_in_fields(info_fetch)
        else:
            messagebox.showerror(title="Error", message='Nombre no encontrado.')

def t3_add_observations():
    t3_add_observations_window = Toplevel()
    t3_add_observations_window.title("Editar Observaciones")
    t3_add_observations_window.minsize(height=250, width=400)
    t3_add_observations_window.maxsize(height=250, width=400)
    t3_add_observations_window.iconbitmap(IMAGE_APP_URL)
    
    t3_add_observations_input = Text(t3_add_observations_window)
    t3_add_observations_input.pack()
    t3_add_observations_input.insert(END, t3_observaciones_input.get())
    t3_observaciones_input.delete(0, END)

    t3_submit_btn.config(state=DISABLED)
    t3_observaciones_input.config(state=DISABLED)

    def on_close_edit_observations_w():
        t3_submit_btn.config(state=NORMAL)
        t3_observaciones_input.config(state=NORMAL)
        t3_observaciones_input.insert(0, t3_add_observations_input.get('1.0', 'end-1c'))
        t3_add_observations_window.destroy()
    t3_add_observations_window.protocol("WM_DELETE_WINDOW", on_close_edit_observations_w)


def t3_update_record_section():

    def update_record(input):
        conexion = get_connection()
        with conexion.cursor() as cursor:
            sql_insert = '''UPDATE {} 
            SET 
                sede='{}',
                area='{}',
                tipo_equipo='{}',
                nombre_equipo='{}',
                modelo='{}',
                tiene_monitor='{}',
                marca_monitor='{}',
                num_serie='{}',
                num_inventario='{}',
                caracteristicas_equipo='{}',
                usuario='{}',
                ip='{}',
                metodo_conexion='{}',
                bitdefender='{}',
                tiene_global='{}',
                agente_global='{}',
                cuenta_impresora='{}',
                pin_impresora='{}',
                no_break='{}',
                num_extension='{}',
                nombre_extension='{}',
                observaciones='{}'
            WHERE id='{}';'''.format(
                TABLE_NAME,
                t3_sede_value_option_menu.get(),
                t3_area_value_option_menu.get(),
                t3_equipo_value_option_menu.get(),
                t3_nombre_equipo_input.get().upper(),
                t3_modelo_input.get(),
                t3_tiene_monitor_value_option_menu.get(),
                t3_marca_monitor_input.get(),
                t3_num_serie_input.get(),
                t3_num_inventario_input.get(),
                t3_caracteristicas_input.get(),
                t3_usuario_input.get(),
                t3_ip_input.get(),
                t3_conexion_value_option_menu.get(),
                t3_bitdefender_value_option_menu.get(),
                t3_global_value_option_menu.get(),
                t3_agente_global_input.get(),
                t3_impresora_input.get(),
                t3_pin_impresora_input.get(),
                t3_no_break_value_option_menu.get(),
                t3_num_extension_input.get(),
                t3_nombre_extension_input.get(),
                t3_observaciones_input.get(),
                input)
            # print(sql_insert)
            cursor.execute(sql_insert)
            conexion.commit()
            conexion.close()
            get_children = table.get_children()
            for children in get_children:
                table.delete(children)
            show_records()
            t3_all_fields_cleaned()

    t3_id_value = id_entry.get()
    name_list = get_name()

    # INCIO: LIMITANDO CARACTERES DE LA PESTAÑA 3
    t3_five_character = [
        t3_tiene_monitor_value_option_menu.get(),
        t3_bitdefender_value_option_menu.get(),
        t3_global_value_option_menu.get(),
        t3_no_break_value_option_menu.get(),
        t3_num_extension_input.get()
    ]
    
    t3_twenty_character = [
        t3_sede_value_option_menu.get(),
        t3_area_value_option_menu.get(),
        t3_equipo_value_option_menu.get(),
        t3_nombre_equipo_input.get(),
        t3_marca_monitor_input.get(),
        t3_num_serie_input.get(),
        t3_num_inventario_input.get(),
        t3_ip_input.get(),
        t3_conexion_value_option_menu.get(),
        t3_agente_global_input.get(),
        t3_impresora_input.get(),
    ]
    
    t3_fifty_character = [
        t3_modelo_input.get(),
        t3_caracteristicas_input.get(),
        t3_usuario_input.get(),
        t3_nombre_extension_input.get()
    ]

    are_too_much_chars_5 = character_limiter(5, *t3_five_character)
    are_too_much_chars_20 = character_limiter(20, *t3_twenty_character)
    are_too_much_chars_50 = character_limiter(50, *t3_fifty_character)
    are_too_much_chars_250 = character_limiter(250, t3_observaciones_input.get())
    # FIN: LIMITANDO CARACTERES DE LA PESTAÑA 3

    try:
        id_lists = get_id_list()
        if are_too_much_chars_5 or are_too_much_chars_20 or are_too_much_chars_50 or are_too_much_chars_250:
            messagebox.showerror(title='Error', message='Uno o más campos exceden el número de caractéres permitidos. Pulsa el botón de ayuda que está en la pestaña de "Añadir Registro" para conocer más acerca de este error.')
        elif t3_id_value in id_lists:
            t3_repeated_name_search_by_id = pc_names_founder_edit(t3_nombre_equipo_search_by_id[0], t3_nombre_equipo_input.get().upper())
            t3_repeated_ip = ip_founder_edit(t3_nombre_equipo_search_by_id[1], t3_ip_input.get())
            if t3_repeated_name_search_by_id and len(t3_nombre_equipo_input.get()) > 0:
                messagebox.showerror(title='Duplicación en el Nombre del Equipo', message='Este nombre de equipo ya está en uso. Intente con otro.')
            elif t3_repeated_ip and len(t3_ip_input.get()) > 0:
                messagebox.showerror(title='Duplicación en la IP', message='Esta IP ya está en uso. Intente con otra.')
            else:
                update_record(t3_id_value)
                update_successful_message()
        elif search_by_name_input.get().upper() in name_list and len(search_by_name_input.get()) >= 1:
            t3_repeated_name_search_by_name = pc_names_founder_edit(t3_nombre_equipo_search_by_name[0], t3_nombre_equipo_input.get().upper())
            t3_repeated_ip_search_by_name = ip_founder_edit(t3_nombre_equipo_search_by_name[1], t3_ip_input.get())
            if t3_repeated_name_search_by_name and len(t3_nombre_equipo_input.get()) > 0:
                messagebox.showerror(title='Duplicación en el Nombre del Equipo', message='Este nombre de equipo ya está en uso. Intente con otro.')
            elif t3_repeated_ip_search_by_name and len(t3_ip_input.get()) > 0:
                messagebox.showerror(title='Duplicación en la IP', message='Esta IP ya está en uso. Intente con otra.')
            else:
                got_id = get_id()
                update_record(got_id[0])
                update_successful_message()
    except Exception:
        messagebox.showerror(title='Error', message='Se ha producido un error')




title_label = Label(third_frame, text="Buscar / Editar Registro", bg=BG_COLOR,  fg=FG_COLOR, font=FONT_TITLE_TUPLE)
title_label.grid(column=0, row=0, columnspan=4, sticky='nsew', pady=PADY_TITLE)

id_label = Label(third_frame, text="Por ID", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
id_label.grid(column=0, row=1, columnspan=2, sticky='s')
id_entry = Entry(third_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=2)
id_entry.grid(column=0, row=2, columnspan=2, sticky='s')
id_search_btn = Button(third_frame, text="Buscar", command=search_record_by_id, bg=SEARCH_BTN_COLOR, fg=FG_COLOR, width=7)
id_search_btn.grid(column=0, row=3, columnspan=2, sticky='s', pady=2)
id_entry.bind("<Return>", (lambda event: search_record_by_id()))
id_search_btn.bind("<Return>", (lambda event: search_record_by_id()))

search_by_name_label = Label(third_frame, text="Por Nombre del Equipo", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
search_by_name_label.grid(column=2, row=1, columnspan=2, sticky='s')
search_by_name_input = Entry(third_frame, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=2)
search_by_name_input.grid(column=2, row=2, columnspan=2, sticky='s')
search_by_name_btn = Button(third_frame, text="Buscar", command=search_record_by_name, bg=SEARCH_BTN_COLOR, fg=FG_COLOR, width=7)
search_by_name_btn.grid(column=2, row=3, columnspan=2, sticky='s', pady=2)
search_by_name_input.bind("<Return>", (lambda event: search_record_by_name()))
search_by_name_btn.bind("<Return>", (lambda event: search_record_by_name()))

disable_id = Entry(third_frame)
disable_id.grid(column=1, row=4, columnspan=2, sticky='s')

t3_sede_value_option_menu = StringVar()
t3_sede_value_option_menu.set('')
t3_sede_label = Label(third_frame, text="Sede", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_sede_label.grid(column=0, row=5, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_sede_input = OptionMenu(third_frame, t3_sede_value_option_menu, *SEDE_MENU)
t3_sede_input.grid(column=1, row=5, sticky='w', pady=PADY_GRID)
t3_sede_input.config(state=DISABLED, width=OPTIONMENU_WIDTH)

t3_area_value_option_menu = StringVar()
t3_area_value_option_menu.set('')
t3_area_label = Label(third_frame, text="Area", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_area_label.grid(column=2, row=5, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_area_input = OptionMenu(third_frame, t3_area_value_option_menu, *AREA_MENU)
t3_area_input.grid(column=3, row=5, sticky='w', pady=PADY_GRID)
t3_area_input.config(state=DISABLED, width=OPTIONMENU_WIDTH)

t3_equipo_value_option_menu = StringVar()
t3_equipo_value_option_menu.set('')
t3_equipo_label = Label(third_frame, text="Equipo", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_equipo_label.grid(column=0, row=6, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_equipo_input = OptionMenu(third_frame, t3_equipo_value_option_menu, *TIPO_EQUIPO_MENU)
t3_equipo_input.grid(column=1, row=6, sticky='w')
t3_equipo_input.config(state=DISABLED, width=OPTIONMENU_WIDTH)

t3_nombre_equipo_label = Label(third_frame, text="Nombre del Equipo", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_nombre_equipo_label.grid(column=2, row=6, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_nombre_equipo_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_nombre_equipo_input.grid(column=3, row=6, sticky='w')

t3_modelo_label = Label(third_frame, text="Modelo", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_modelo_label.grid(column=0, row=7, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_modelo_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_modelo_input.grid(column=1, row=7, sticky='w')

t3_tiene_monitor_value_option_menu = StringVar()
t3_tiene_monitor_value_option_menu.set('')
t3_tiene_monitor_label = Label(third_frame, text="¿Tiene Monitor?", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_tiene_monitor_label.grid(column=2, row=7, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_tiene_monitor_input = OptionMenu(third_frame, t3_tiene_monitor_value_option_menu, *QUESTION_MENU)
t3_tiene_monitor_input.grid(column=3, row=7, sticky='w')
t3_tiene_monitor_input.config(width=OPTIONMENU_WIDTH)

t3_marca_monitor_label = Label(third_frame, text="Marca del Monitor", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_marca_monitor_label.grid(column=0, row=8, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_marca_monitor_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_marca_monitor_input.grid(column=1, row=8, sticky='w')

t3_num_serie_label = Label(third_frame, text="No. de Serie", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_num_serie_label.grid(column=2, row=8, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_num_serie_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_num_serie_input.grid(column=3, row=8, sticky='w')

t3_num_inventario_label = Label(third_frame, text="No. de Inventario", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_num_inventario_label.grid(column=0, row=9, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_num_inventario_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_num_inventario_input.grid(column=1, row=9, sticky='w')

t3_caracteristicas_label = Label(third_frame, text="Características de Equipo", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_caracteristicas_label.grid(column=2, row=9, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
t3_caracteristicas_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_caracteristicas_input.grid(column=3, row=9, sticky='w')

t3_usuario_label = Label(third_frame, text="Usuario", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_usuario_label.grid(column=0, row=10, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_usuario_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_usuario_input.grid(column=1, row=10, sticky='w')

t3_ip_label = Label(third_frame, text="IP", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_ip_label.grid(column=2, row=10, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
t3_ip_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_ip_input.grid(column=3, row=10, sticky='w')

t3_conexion_value_option_menu = StringVar()
t3_conexion_value_option_menu.set('')
t3_conexion_label = Label(third_frame, text="Método de Conexión", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_conexion_label.grid(column=0, row=11, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_conexion_input = OptionMenu(third_frame, t3_conexion_value_option_menu, *METODO_CONEXION_MENU)
t3_conexion_input.grid(column=1, row=11, sticky='w')
t3_conexion_input.config(state=DISABLED, width=OPTIONMENU_WIDTH)

t3_bitdefender_value_option_menu = StringVar()
t3_bitdefender_value_option_menu.set('')
t3_bitdefender_label = Label(third_frame, text="¿Tiene Bitdefender?", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_bitdefender_label.grid(column=2, row=11, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
t3_bitdefender_input = OptionMenu(third_frame, t3_bitdefender_value_option_menu, *QUESTION_MENU)
t3_bitdefender_input.grid(column=3, row=11, sticky='w')
t3_bitdefender_input.config(state=DISABLED, width=OPTIONMENU_WIDTH)

t3_global_value_option_menu = StringVar()
t3_global_value_option_menu.set('')
t3_global_label = Label(third_frame, text="¿Tiene Global?", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_global_label.grid(column=0, row=12, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_global_input = OptionMenu(third_frame, t3_global_value_option_menu, *QUESTION_MENU)
t3_global_input.grid(column=1, row=12, sticky='w')
t3_global_input.config(state=DISABLED, width=OPTIONMENU_WIDTH)

t3_agente_global_label = Label(third_frame, text="Agente del Global", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_agente_global_label.grid(column=2, row=12, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
t3_agente_global_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_agente_global_input.grid(column=3, row=12, sticky='w')

t3_impresora_label = Label(third_frame, text="Cuenta de Impresora", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_impresora_label.grid(column=0, row=13, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_impresora_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_impresora_input.grid(column=1, row=13, sticky='w')

t3_pin_impresora_label = Label(third_frame, text="Pin de Impresora", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_pin_impresora_label.grid(column=2, row=13, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
t3_pin_impresora_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_pin_impresora_input.grid(column=3, row=13, sticky='w')

t3_no_break_value_option_menu = StringVar()
t3_no_break_value_option_menu.set('')
t3_no_break_label = Label(third_frame, text="¿Tiene No Break?", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_no_break_label.grid(column=0, row=14, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_no_break_input = OptionMenu(third_frame, t3_no_break_value_option_menu, *QUESTION_MENU)
t3_no_break_input.grid(column=1, row=14, sticky='w')
t3_no_break_input.config(state=DISABLED, width=OPTIONMENU_WIDTH)

t3_num_extension_label = Label(third_frame, text="Número de Extensión", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_num_extension_label.grid(column=2, row=14, sticky='e',  pady=PADY_GRID, padx=PADX_GRID)
t3_num_extension_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_num_extension_input.grid(column=3, row=14, sticky='w')

t3_nombre_extension_label = Label(third_frame, text="Nombre de la Extensión", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_nombre_extension_label.grid(column=0, row=15, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_nombre_extension_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_nombre_extension_input.grid(column=1, row=15, sticky='w')

t3_observaciones_label = Label(third_frame, text="Observaciones", bg=BG_COLOR, fg=FG_COLOR, font=FONT_TUPLE)
t3_observaciones_label.grid(column=2, row=15, sticky='e', pady=PADY_GRID, padx=PADX_GRID)
t3_observaciones_input = Entry(third_frame, state=DISABLED, highlightcolor=LINE_ENTRY_COLOR, highlightthickness=LINE, width=ENTRY_WIDTH)
t3_observaciones_input.grid(column=3, row=15, sticky='w')

clean_button = Button(third_frame, text="Limpiar campos", command=t3_all_fields_cleaned, bg=DELETE_BTN_COLOR, fg=FG_COLOR, font=FONT_BTN_TUPLE, width=SUBMIT_BTN_WIDTH)
clean_button.grid(column=0, row=16, sticky='e', pady=PADY_GRID)

t3_submit_btn = Button(third_frame, text="Guardar", command=t3_update_record_section, state=DISABLED, bg=SAVE_BTN_COLOR, fg=FG_COLOR, font=FONT_BTN_TUPLE, width=SUBMIT_BTN_WIDTH)
t3_submit_btn.grid(column=1, columnspan=2, row=16, sticky='s', pady=PADY_GRID)

t3_add_observations_btn = Button(third_frame, text="Ampliar Campo", command=t3_add_observations, state=DISABLED, bg=OBSERVATIONS_BTN_COLOR, fg=FG_COLOR, width=SUBMIT_BTN_WIDTH)
t3_add_observations_btn.grid(column=3, row=16, sticky='w', pady=PADY_GRID)

# INICIO: HACER QUE LA TECLA ENTER FUNCIONE PARA LA PESTAÑA 3
t3_input_list = [
    t3_nombre_equipo_input,
    t3_modelo_input,
    t3_marca_monitor_input,
    t3_num_serie_input,
    t3_num_inventario_input,
    t3_caracteristicas_input,
    t3_usuario_input,
    t3_ip_input,
    t3_agente_global_input,
    t3_impresora_input,
    t3_pin_impresora_input,
    t3_num_extension_input,
    t3_nombre_extension_input,
    t3_observaciones_input,
    t3_add_observations_btn
]

for t3_input_name in t3_input_list:
    t3_input_name.bind('<Return>', (lambda event: t3_update_record_section()))
# INICIO: HACER QUE LA TECLA ENTER FUNCIONE PARA LA PESTAÑA 3

####################################  FIN DE LA PESTAÑA 3 - BUSCAR / EDITAR #######################################

##################### AÑADIENDO LAS PESTAÑAS AL NOTEBOOK #####################
tabs.add(first_frame, text="Base de Datos")
tabs.add(second_frame, text="Añadir Registro")
tabs.add(third_frame, text="Buscar Registros")
tabs.grid(column=0, row=0, sticky="nsew")

##################### ESTILOS #####################
style = ttk.Style()
style.theme_use("alt")
style.configure('Treeview.Heading', background='#F2DEBA', foreground="black", font=(FONT_STYLE_TREEVIEW, 11, "bold"))
style.configure('Treeview', foreground="black", font=(FONT_STYLE_TREEVIEW, 11, "italic"))
style.map('Treeview', background=[('selected', '#4A6984')])


window.mainloop()
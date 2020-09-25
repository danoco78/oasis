screen_helper = """
ScreenManager:
    ScreenHome:
    ScreenOperadoresTelco:
    ScreenCallesCabecera:


<ScreenHome>:
    name: 'scr_home'
    
    Image:
        source: 'img/logoCelsia.png'
        pos_hint: {'center_x':0.5, 'center_y':0.8}
        size: self.size
    
    MDLabel:
        text: "OASIS"
        color: 213, 117, 200, 1
        halign: "center"
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        font_style: "H4"
    
    
    MDTextField:
        id: scrh_txt_usaername
        hint_text: "Enter Username"
        helper_text: "or click on forgot username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.4}
        size_hint_x:None
        width:300
    
    MDTextField:
        id: scrh_txt_password
        hint_text: "Enter Password"
        helper_text: "or click on forgot Password"
        helper_text_mode: "on_focus"
        icon_right: "key-variant"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        size_hint_x:None
        width:300
        password: True

    MDRectangleFlatButton:
        text: 'Ingresar'
        pos_hint: {'center_x':0.5, 'center_y':0.1}
        on_release: validar_acceso()
        
<ScreenOperadoresTelco>:
    name: 'scr_operadoresTelco'
    MDLabel:
        text: 'Selecciona los operadores presentes en este barrio'
        halign: 'center'

    MDRectangleFlatButton:
        text: 'Home'
        pos_hint: {'center_x':0.2, 'center_y':0.05}
        on_press: root.manager.current = 'scr_home'

    MDRectangleFlatButton:
        text: 'perfiles'
        pos_hint: {'center_x':0.8, 'center_y':0.05}
        on_press: root.manager.current = 'upload'


<ScreenCallesCabecera>
    name: 'scr_calleCabecera'
    MDLabel:
        text: 'carga de perfiles'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'home'
        pos_hint: {'center_x':0.5, 'center_y':0.05}
        on_press: root.manager.current = 'scr_home'
"""
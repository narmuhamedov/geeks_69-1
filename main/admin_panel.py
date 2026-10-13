JAZZMIN_SETTINGS = {
    "site_title": "GEEKS-69-1",
    "site_header": "GEEKS-69-1",
    "site_brand": "GEEKS-69-1",
    "site_logo": 'admin/logo.png',
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Добро пожаловать в ПУ сайта",
    "copyright": "GEEKS-69-1",

    "search_model": ["auth.User", "auth.Group"],
    "user_avatar": None,

    "topmenu_links": [
        {"name": "Главная", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Отсылка", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.User"},
        {"app": "books"},
    ],

    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    "custom_links": {
        "books": [{
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": False,

    # ⬇️ ВАЖНО: подключаем свой CSS с жёлтым акцентом
    "custom_css": "css/admin_yellow.css",
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,   # выключил, чтобы случайно не сбить тему

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "language_chooser": False,
}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-warning",       # жёлтый бренд
    "accent": "accent-warning",              # жёлтый акцент
    "navbar": "navbar-dark navbar-warning",  # жёлтый навбар
    "no_navbar_border": True,
    "navbar_fixed": True,                    # зафиксировали навбар
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,                   # сайдбар фиксирован
    "sidebar": "sidebar-dark-warning",       # чёрный сайдбар с жёлтым
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "darkly",                       # тёмная базовая тема
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary":   "btn-warning",
        "secondary": "btn-outline-warning",
        "info":      "btn-info",
        "warning":   "btn-warning",
        "danger":    "btn-danger",
        "success":   "btn-success",
    },
    "actions_sticky_top": True,
}
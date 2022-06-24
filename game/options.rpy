init -1 python hide:

    config.developer = True

    config.screen_width = 1920
    config.screen_height = 1080

    config.window_title = u"Rogue-Like Chonky Mod"

    config.name = "Rogue-Like Chonky Mod"
    config.version = "0.3a"

    config.gl2 = True
    config.cache_surfaces = True
    config.image_cache_size_mb = 2048

    theme.tv(
        widget = "#6A7183",
        widget_hover = "#1A2B47",
        widget_text = "#C9C9CB",
        widget_selected = "#E3E3E4",
        disabled = "#ADB9CC",
        disabled_text = "#DFBA14",
        label = "#39435E",
        frame = "#ADB9CC",
        mm_root = "images/titleimage.jpg",
        gm_root = "images/menuimage.jpg",
        rounded_window = False)

    style.window.background = Frame("images/chatbox.png", 12, 12)

    style.window.left_margin = 6
    style.window.right_margin = 6
    style.window.top_margin = 6
    style.window.bottom_margin = 6

    style.window.left_padding = 25
    style.window.right_padding = 25
    style.window.top_padding = 25
    style.window.bottom_padding = 25
    style.window.xminimum = 5
    style.window.xmaximum = 500
    style.window.yminimum = 5

    style.say_who_window.background = Frame("images/Nametag.png", 20,20) #namebox.png
    style.say_who_window.xalign = 0.05
    style.say_who_window.yalign = -100
    style.say_who_window.xminimum = 50

    style.say_who_window.left_padding = 10
    style.say_who_window.right_padding = 10
    style.say_who_window.top_padding = 10
    style.say_who_window.bottom_padding = 10

    style.say_balloon = Style(style.default)
    style.say_balloon.background = Frame("images/Wordballoon.png", 50, 50)
    style.say_balloon.left_padding = 25
    style.say_balloon.right_padding = 25
    style.say_balloon.top_padding = 25
    style.say_balloon.bottom_padding = 25
    style.say_balloon.yminimum = 0
    style.say_balloon.xminimum = 100
    style.say_balloon.xmaximum = 450
    style.say_balloon.font = "ltromatic.ttf"

    style.textbox = Style(style.default)
    style.textbox.background = Frame("images/chatbox.png", 12, 12)
    style.textbox.padding = (25, 25)
    style.textbox.xminimum = 100
    style.textbox.xmaximum = 450

    style.default.font = "dungeon.ttf"
    style.default.size = 18

    config.has_sound = False
    config.has_music = False
    config.has_voice = False

    config.help = "README.html"

    config.enter_transition = None
    config.exit_transition = None
    config.intra_transition = None
    config.main_game_transition = None
    config.game_main_transition = None
    config.end_splash_transition = None
    config.end_game_transition = None
    config.after_load_transition = None
    config.window_show_transition = None
    config.window_hide_transition = None
    config.adv_nvl_transition = dissolve
    config.nvl_adv_transition = dissolve
    config.enter_yesno_transition = None
    config.exit_yesno_transition = None
    config.enter_replay_transition = None
    config.exit_replay_transition = None
    config.say_attribute_transition = None

python early:

    config.save_directory = "Rogue-Like Chonky Mod"

init -1 python hide:

    config.default_fullscreen = False

    config.default_text_cps = 0

    config.default_afm_time = 10

    config.skip_delay = 75

init python:

    build.directory_name = "Rogue-Like-Chonky-Mod"

    build.executable_name = "Rogue-Like Chonky Mod"

    build.include_update = False

    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("**/script Remove from Launch.*", None)

    build.classify("**.png", "archive")
    build.classify("**.jpg", "archive")
    build.classify("**.rpy", "archive")
    build.classify("**.rpyc", "archive")
    build.classify("**.TTF", "archive")

    build.documentation("*.html")
    build.documentation("*.txt")

    config.rollback_length = 500

    config.layers = ["background", "master", "black", "transient", "screens", "overlay"]

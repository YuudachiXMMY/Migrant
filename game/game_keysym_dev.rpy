init offset = -999

define config.pad_bindings = {
    "pad_leftshoulder_press" : [ ],
    "pad_lefttrigger_pos" : [ ],
    "pad_back_press" : [ ],

    "pad_guide_press" : [ ],
    "pad_start_press" : [ ],

    "pad_y_press" : [ ],

    "pad_rightshoulder_press" : [ ],

    "pad_righttrigger_pos" : [ ],
    "pad_a_press" : [ ],
    "pad_b_press" : [ ],

    "pad_dpleft_press" : [ ],
    "pad_leftx_neg" : [ ],
    "pad_rightx_neg" : [ ],

    "pad_dpright_press" : [ ],
    "pad_leftx_pos" : [ ],
    "pad_rightx_pos" : [ ],

    "pad_dpup_press" : [ ],
    "pad_lefty_neg" :  [ ],
    "pad_righty_neg" : [ ],

    "pad_dpdown_press" : [ ],
    "pad_lefty_pos" : [ ],
    "pad_righty_pos" : [ ],
}

# renpy.clear_keymap_cache()
# Clears the keymap cache. This allows changes to config.keymap to take effect without restarting Ren'Py.

# Keymap for Release
define keymap_release = dict(

    # Bindings present almost everywhere, unless explicitly
    # disabled.
    rollback = [ ],
    screenshot = [ ],
    toggle_afm = [ ],
    toggle_fullscreen = [ ],
    game_menu = [ ],
    history_menu = [ 'mousedown_4' ],
    hide_windows = [ 'K_ESCAPE', 'mousedown_2' ],
    launch_editor = [ ],
    dump_styles = [ ],
    reload_game = [ ],
    inspector = [ ],
    full_inspector = [ ],
    developer = [ ],
    quit = [ ],
    iconify = [ ],
    help = [ ],
    choose_renderer = [ ],
    progress_screen = [ ],
    # Accessibility.
    self_voicing = [ ],
    clipboard_voicing = [ ],
    debug_voicing = [ ],
    accessibility = [ ],

    # DIY
    quit_menu = [ 'K_ESCAPE', 'mousedown_3' ],
    auto_dialogue = [ ],

    # Say.
    rollforward = [ 'mousedown_5', 'K_RETURN', 'repeat_K_RETURN' ],
    dismiss = [ 'mousedown_5', 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SPACE', 'K_KP_SPACE' ],
    dismiss_unfocused = [ ],

    # Pause.
    dismiss_hard_pause = [ ],

    # Focus.
    focus_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    focus_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    focus_up = [ 'K_UP', 'repeat_K_UP' ],
    focus_down = [ 'K_DOWN', 'repeat_K_DOWN' ],

    # Button.
    button_ignore = [ 'mousedown_1' ],
    button_select = [ 'mouseup_1' ],
    button_alternate = [ ],
    button_alternate_ignore = [ ],

    # Input.
    input_backspace = [ ],
    input_enter = [ ],
    input_left = [ ],
    input_right = [ ],
    input_up = [ ],
    input_down = [ ],
    input_delete = [ ],
    input_home = [ ],
    input_end = [ ],
    input_copy = [ ],
    input_paste = [ ],

    # Viewport.
    viewport_leftarrow = [ 'K_LEFT', 'repeat_K_LEFT' ],
    viewport_rightarrow = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    viewport_uparrow = [ 'K_UP', 'repeat_K_UP' ],
    viewport_downarrow = [ 'K_DOWN', 'repeat_K_DOWN' ],
    viewport_wheelup = [ 'mousedown_4' ],
    viewport_wheeldown = [ 'mousedown_5' ],
    viewport_drag_start = [ 'mousedown_1' ],
    viewport_drag_end = [ 'mouseup_1' ],

    # These keys control skipping.
    skip = [ 'K_LCTRL', 'K_RCTRL' ],
    stop_skipping = [ ],
    toggle_skip = [ ],
    fast_skip = [ ],

    # Bar.
    bar_activate = [ 'mousedown_1' ],
    bar_deactivate = [ 'mouseup_1' ],
    bar_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    bar_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    bar_up = [ 'K_UP', 'repeat_K_UP' ],
    bar_down = [ 'K_DOWN', 'repeat_K_DOWN' ],

    # 右键菜单
    right_click_menu= [ 'mousedown_3' ],

    # Delete a save.
    save_delete = [ 'mouseup_3', 'mousedown_3', 'K_DELETE' ],

    # Draggable.
    drag_activate = [ 'mousedown_1' ],
    drag_deactivate = [ 'mouseup_1' ],

    # Debug console.
    console = [ ],
    console_older = [ 'K_UP', 'repeat_K_UP' ],
    console_newer = [ 'K_DOWN', 'repeat_K_DOWN'],

    # Ignored (kept for backwards compatibility).
    toggle_music = [ ],
    viewport_up = [ 'mousedown_4' ],
    viewport_down = [ 'mousedown_5' ],

    # Profile commands.
    profile_once = [ ],
    memory_profile = [ ],


    )

# Keymap for Ending Chapter
define keymap_end = dict(

    # Bindings present almost everywhere, unless explicitly
    # disabled.
    rollback = [ ],
    screenshot = [ ],
    toggle_afm = [ ],
    toggle_fullscreen = [ ],
    game_menu = [ ],
    history_menu = [ ],
    hide_windows = [ ],
    launch_editor = [ ],
    dump_styles = [ ],
    reload_game = [ ],
    inspector = [ ],
    full_inspector = [ ],
    developer = [ ],
    quit = [ ],
    iconify = [ ],
    help = [ ],
    choose_renderer = [ ],
    progress_screen = [ ],
    # Accessibility.
    self_voicing = [ ],
    clipboard_voicing = [ ],
    debug_voicing = [ ],

    # DIY
    quit_menu = [ ],
    quit_hist = [ ],
    auto_dialogue = [ ],

    # Say.
    rollforward = [ ],
    dismiss = [ ],
    dismiss_unfocused = [ ],

    # Pause.
    dismiss_hard_pause = [ ],

    # Focus.
    focus_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    focus_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    focus_up = [ 'K_UP', 'repeat_K_UP' ],
    focus_down = [ 'K_DOWN', 'repeat_K_DOWN' ],

    # Button.
    button_ignore = [ 'mousedown_1' ],
    button_select = [ 'mouseup_1' ],
    button_alternate = [ ],
    button_alternate_ignore = [ ],

    # Input.
    input_backspace = [ ],
    input_enter = [ ],
    input_left = [ ],
    input_right = [ ],
    input_up = [ ],
    input_down = [ ],
    input_delete = [ ],
    input_home = [ ],
    input_end = [ ],
    input_copy = [ ],
    input_paste = [ ],

    # Viewport.
    viewport_leftarrow = [ 'K_LEFT', 'repeat_K_LEFT' ],
    viewport_rightarrow = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    viewport_uparrow = [ 'K_UP', 'repeat_K_UP' ],
    viewport_downarrow = [ 'K_DOWN', 'repeat_K_DOWN' ],
    viewport_wheelup = [ 'mousedown_4' ],
    viewport_wheeldown = [ 'mousedown_5' ],
    viewport_drag_start = [ 'mousedown_1' ],
    viewport_drag_end = [ 'mouseup_1' ],

    # These keys control skipping.
    skip = [ ],
    stop_skipping = [ ],
    toggle_skip = [ ],
    fast_skip = [ ],

    # Bar.
    bar_activate = [ 'mousedown_1' ],
    bar_deactivate = [ 'mouseup_1' ],
    bar_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    bar_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    bar_up = [ 'K_UP', 'repeat_K_UP' ],
    bar_down = [ 'K_DOWN', 'repeat_K_DOWN' ],

    # 右键菜单
    right_click_menu= [ ],

    # Delete a save.
    save_delete = [ 'mouseup_3', 'mousedown_3', 'K_DELETE' ],

    # Draggable.
    drag_activate = [ 'mousedown_1' ],
    drag_deactivate = [ 'mouseup_1' ],

    # Debug console.
    console = [ ],
    console_older = [ 'K_UP', 'repeat_K_UP' ],
    console_newer = [ 'K_DOWN', 'repeat_K_DOWN'],

    # Ignored (kept for backwards compatibility).
    toggle_music = [ ],
    viewport_up = [ 'mousedown_4' ],
    viewport_down = [ 'mousedown_5' ],

    # Profile commands.
    profile_once = [ ],
    memory_profile = [ ],


    )

# Keymap in use
define config.keymap = keymap_release #keymap_debug|keymap_release

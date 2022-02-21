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

define config.keymap = dict(

    # Bindings present almost everywhere, unless explicitly
    # disabled.
    rollback = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK' ],
    screenshot = [ ],
    toggle_afm = [ ],
    toggle_fullscreen = [ ],
    game_menu = [ ],
<<<<<<< HEAD
    history_menu = [ 'mousedown_2' ],
    hide_windows = [ 'K_SPACE' ],
=======
    history_menu = [ 'mousedown_4' ],
    hide_windows = [ 'K_ESCAPE', 'mousedown_2' ],
>>>>>>> b9f7f07370a7075f5e7d253ad805edc56018b202
    launch_editor = [ ],
    dump_styles = [ ],
    reload_game = [ 'R' ],
    inspector = [ 'I' ],
    full_inspector = [ 'alt_I' ],
    developer = [ 'd'],
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
    quit_menu = [ 'K_ESCAPE', 'mousedown_3' ],
    quit_hist = [ 'K_ESCAPE', 'mousedown_3' ],

    # Say.
<<<<<<< HEAD
    rollforward = [ 'mousedown_5', 'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ],
=======
    rollforward = [ 'mousedown_5', 'K_PAGEDOWN', 'repeat_K_PAGEDOWN', 'K_SPACE' ],
>>>>>>> b9f7f07370a7075f5e7d253ad805edc56018b202
    dismiss = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
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
    button_select = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
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
    bar_activate = [ 'mousedown_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    bar_deactivate = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    bar_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    bar_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    bar_up = [ 'K_UP', 'repeat_K_UP' ],
    bar_down = [ 'K_DOWN', 'repeat_K_DOWN' ],

    # 右键菜单
<<<<<<< HEAD
    right_click_menu= [ 'mousedown_3' ],

    # Delete a save.
    save_delete = [ 'mouseup_3', 'mousedown_3', 'K_DELETE' ],
=======
    right_click_menu= [ 'mouseup_3' ],

    # Delete a save.
    save_delete = [ 'mousedown_3', 'K_DELETE' ],
>>>>>>> b9f7f07370a7075f5e7d253ad805edc56018b202

    # Draggable.
    drag_activate = [ 'mousedown_1' ],
    drag_deactivate = [ 'mouseup_1' ],

    # Debug console.
    console = [ ],
    console_older = [ 'K_UP', 'repeat_K_UP' ],
    console_newer = [ 'K_DOWN', 'repeat_K_DOWN'],

    # Ignored (kept for backwards compatibility).
    toggle_music = [ 'm' ],
    viewport_up = [ 'mousedown_4' ],
    viewport_down = [ 'mousedown_5' ],

    # Profile commands.
    profile_once = [ ],
    memory_profile = [ ],


    )
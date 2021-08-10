init offset = -2

image bg_cover:
    "gui/bg_cover.png"

image black_bg:
    alpha 0.7
    "gui/black.png"

image white_bg:
    "gui/white.png"

## 主界面 ######################################################################
##
image main_bg:
    "gui/main/bg.png"

image main_logo:
    "gui/main/logo.png"

image start_idle:
    "gui/main/开始.png"

image start_hover:
    "gui/main/开始_2.png"

image load_idle:
    "gui/main/读档.png"

image load_hover:
    "gui/main/读档_2.png"

image setting_idle:
    "gui/main/设置.png"

image setting_hover:
    "gui/main/设置_2.png"

image extraContent_idle:
    "gui/main/附加内容.png"

image extraContent_hover:
    "gui/main/附加内容_2.png"

image staff_idle:
    "gui/main/制作人员.png"

image staff_hover:
    "gui/main/制作人员_2.png"

image exit_idle:
    "gui/main/退出.png"

image exit_hover:
    "gui/main/退出_2.png"

image blank_idle:
    "gui/blank.png"

image blank_hover:
    "gui/blank.png"

# 制作组logo
image KID_Fans_Club_logo:
    "gui/LOGO-BLUE.png"
    zoom 0.68

# 引擎logo
image RenPy_logo:
    "gui/renpy.png"
    zoom 3.9168

## 存档 ######################################################################
##
image sl_bg:
    "gui/sl/bg.png"

image sl_close_idle:
    "gui/sl/关闭.png"

image sl_page_previous_idle:
    "gui/sl/翻页-左.png"

image sl_page_next_idle:
    "gui/sl/翻页-右.png"

image sl_load_btn_idle:
    "gui/sl/读档-未选择.png"

image sl_save_btn_idle:
    "gui/sl/存档-未选择.png"

image sl_load_btn_untoggled:
    "gui/sl/读档-选中.png"

image sl_save_btn_untoggled:
    "gui/sl/存档-选中.png"

image sl_slot_bg:
    "gui/sl/挡位底板.png"

image sl_slot_bg_hover:
    align(0.5, 0.5)
    "gui/sl/选中.png"

image sl_slot_page_background:
    zoom 0.9
    "gui/sl/页面底框.png"

image sl_delete_idle:
    "gui/sl/右键-删除-常态.png"

image sl_delete_hover:
    "gui/sl/右键-删除-选择.png"

## 存档位数字

## 确认窗口 ######################################################################
##
image confirm_bg:
    align(0.5, 0.5)
    "gui/confirm/弹窗背板.png"

image confirm_btn_idle:
    "gui/confirm/按钮底-未选.png"

image confirm_btn_hover:
    "gui/confirm/按钮底-选择.png"

## 主界面 设置 ######################################################################
##
image setting_bg:
    align(0.5, 0.5)
    "gui/setting/bg.png"

image setting_close_idle:
    "gui/setting/关闭.png"

#* 打勾按钮
image setting_click_idle:
    Composite(
        (42, 38),
        (0, 0), "gui/setting/选项框.png")

image setting_toggled_btn_idle:
    "setting_click_selected_idle"

image setting_click_selected_idle:
    Composite(
        (42, 38),
        (0, 0), "gui/setting/选项框.png",
        (0, 0), "gui/setting/勾.png")

image setting_click_selected_hover:
    "setting_click_selected_idle"
#* ##

## 文本设置
image setting_text_title:
    "gui/setting/文本设置title.png"

image setting_slider_3_idle:
    "gui/setting/滚轴-三点.png"

image setting_slider_3_btn_idle:
    "gui/setting/选中.png"

## 显示设置
image setting_graphics_title:
    "gui/setting/显示设置title.png"

image setting_graphics_bg:
    "gui/setting/分辨率框.png"

image setting_graphics_btn_idle:
    "gui/setting/下拉.png"

image setting_graphics_btn_hover:
    "setting_graphics_btn_idle"

## 音乐设置
image setting_sound_title:
    "gui/setting/音乐设置title.png"

image setting_slider_2_idle:
    "gui/setting/滚轴-两点.png"

image setting_slider_2_btn_idle:
    "gui/setting/滚轴点.png"

## 制作人员
image staffs_bg:
    "gui/staffs/bg.jpg"

image staffs_return_btn_idle:
    "gui/staffs/return.png"

image staffs_play_btn_idle:
    "gui/staffs/play.png"

image staffs_play_btn_hover:
    "staffs_play_btn_idle"

image staffs_replay_btn_idle:
    "gui/staffs/replay.png"

image staffs_replay_btn_hover:
    "staffs_replay_btn_idle"

## 右键菜单 ######################################################################
##
image r_menu_background:
    "gui/r_menu/右键菜单底板.png"

image r_menu_save_idle:
    "gui/r_menu/存档_idle.png"

image r_menu_save_hover:
    "gui/r_menu/存档_hover.png"

image r_menu_load_idle:
    "gui/r_menu/读档_idle.png"

image r_menu_load_hover:
    "gui/r_menu/读档_hover.png"

image r_menu_history_idle:
    "gui/r_menu/文本回放_idle.png"

image r_menu_history_hover:
    "gui/r_menu/文本回放_hover.png"

image r_menu_setting_idle:
    "gui/r_menu/设置_idle.png"

image r_menu_setting_hover:
    "gui/r_menu/设置_hover.png"

image r_menu_mainmenu_idle:
    "gui/r_menu/返回标题_idle.png"

image r_menu_mainmenu_hover:
    "gui/r_menu/返回标题_hover.png"

image r_menu_exit_idle:
    "gui/r_menu/退出游戏_idle.png"

image r_menu_exit_hover:
    "gui/r_menu/退出游戏_hover.png"




## 对话框 ######################################################################
##
image dia_replay_idle:
    "gui/dialogue/回放.png"

image dia_replay_hover:
    "gui/dialogue/回放-选中.png"

image dia_qucksave_idle:
    "gui/dialogue/快速存档.png"

image dia_qucksave_hover:
    "gui/dialogue/快速存档-选中.png"

## 快速条 ######################################################################
##
image quick_bg:
    "gui/quick/系统条底板.png"

image quick_system_idle:
    "gui/quick/系统-设置.png"

image quick_system_hover:
    "gui/quick/系统-设置.png"

image quick_hidedia_idle:
    "gui/quick/系统条-隐藏常态.png"

image quick_hidedia_hover:
    "gui/quick/系统条-隐藏选中.png"

image quick_hidedia_selected_idle:
    "gui/quick/系统条-隐藏常态.png"

image quick_hidedia_selected_hover:
    "gui/quick/系统条-隐藏选中.png"

image quick_autoplay_idle:
    "gui/quick/系统-播放-未开启.png"

image quick_autoplay_hover:
    "gui/quick/系统-播放-开启.png"

image quick_autoplay_selected_idle:
    "gui/quick/系统-播放-开启.png"

image quick_autoplay_selected_hover:
    "gui/quick/系统-播放-开启.png"

image quick_skip_idle:
    "gui/quick/系统条-快进-未开启.png"

image quick_skip_hover:
    "gui/quick/系统条-快进-开启.png"

image quick_quicksave_idle:
    "gui/quick/系统条-存档常态.png"

image quick_quicksave_hover:
    "gui/quick/系统条-存档选中.png"

image quick_quickload_idle:
    "gui/quick/系统条-读档常态.png"

image quick_quickload_hover:
    "gui/quick/系统条-读档选中.png"

image quick_mainmenu_idle:
    "gui/quick/系统条-home常态.png"

image quick_mainmenu_hover:
    "gui/quick/系统条-home选中.png"


## 主界面 设置 ######################################################################
##
image gallery_bg:
    "gui/gallery/bg.jpg"

image gallery_music_play_btn_idle:
    "gui/gallery/play.png"

image gallery_music_play_btn_hover:
    "gallery_music_play_btn_idle"

image gallery_return_btn_idle:
    "gui/gallery/返回.png"

image gallery_return_btn_hover:
    "gallery_return_btn_idle"

image gallery_page_prev_btn_idle:
    "gui/gallery/上一页.png"

image gallery_page_prev_btn_hover:
    "gallery_page_prev_btn_idle"

image gallery_page_next_btn_idle:
    "gui/gallery/下一页.png"

image gallery_page_next_btn_hover:
    "gallery_page_next_btn_idle"

image gallery_music_prev_btn_idle:
    "gui/gallery/上一首.png"

image gallery_music_prev_btn_hover:
    "gallery_music_prev_btn_idle"

image gallery_music_next_btn_idle:
    "gui/gallery/下一首.png"

image gallery_music_next_btn_hover:
    "gallery_music_next_btn_idle"

## 历史界面 ######################################################################
##
image history_return_btn_idle:
    "gui/history/返回.png"

image history_return_btn_hover:
    "history_return_btn_idle"

image history_voiceReplay_btn_idle:
    "gui/history/语音.png"

image history_voiceReplay_hover:
    "history_voiceReplay_btn_idle"
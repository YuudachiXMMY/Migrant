image bg_cover:
    "gui/bg_cover.png"

## 主界面 ######################################################################
##
image main_bg:
    "gui/main/bg.png"

image main_logo:
    "gui/main/logo.png"

image start_idle:
    "gui/main/开始.png"

image load_idle:
    "gui/main/读档.png"

image setting_idle:
    "gui/main/设置.png"

image extraContent_idle:
    "gui/main/附加内容.png"

image staff_idle:
    "gui/main/制作人员.png"

image exit_idle:
    "gui/main/退出.png"

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

## 画面设置
image setting_graphics_title:
    "gui/setting/画面设置title.png"

image setting_graphics_bg:
    "gui/setting/分辨率框.png"

image setting_graphics_btn_idle:
    "gui/setting/下拉.png"

## 音乐设置
image setting_sound_title:
    "gui/setting/音乐设置title.png"

image setting_text_title:
    "gui/setting/文本设置title.png"

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

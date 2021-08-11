﻿################################################################################
## 初始化
################################################################################

init offset = -1

default first_menu = True
define config.gl_resize = False

default volume_total = 1.0
default volume_music = config.default_music_volume
default volume_voice = config.default_voice_volume
default volume_sound = config.default_sfx_volume

# define config.auto_voice = "voice/{id}.ogg"


################################################################################
## Main
################################################################################
# default persistent.text_speed = 100
# default persistent.auto_forward = 100

default persistent.setting_resolution = [2560, 1440]

transform main_bg_ani:
    alpha 0.0
    linear 3.0 alpha 1.0

transform main_logo_ani:
    xalign 0.5 ypos 0.2 alpha 0.0
    pause 3.5
    linear 3.0 alpha 1.0

define config.main_menu_music = 'audio/music/themepiano.ogg'

image ctc_icon:
    yalign 0.6 alpha 1.0
    "gui/继续对话.png"
    linear 1.5 alpha 0.5
    pause 0.1
    linear 1.5 alpha 1.0
    pause 1
    repeat

image ctc_pause_icon:
    "ctc_icon"

################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内屏幕
################################################################################


## Say 屏幕 ######################################################################
##
## Say 屏幕用于向玩家显示对话。它需要两个参数，“who”和“what”，分别是叙述人的名称
## 和所叙述的内容。（如果没有名称，参数“who”可以是“None”。）
##
## 此屏幕必须创建一个 id 为“what”的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为“who”和 id 为“window”的可视控件来应用样式属性。
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    fixed:
        imagebutton:
            xalign 0.875 yalign 0.85
            auto "dia_qucksave_%s"
            action ShowMenu("save")

        imagebutton:
            xalign 0.875 yalign 0.92
            auto "dia_replay_%s"
            action ShowMenu('history')

    ## 如果有侧边图像，会将其显示在文本之上。请不要在手机界面下显示这个，因为没
    ## 有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5 yoffset -10

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 26


## 右键菜单 ########################################################################
##

screen r_menu():
    zorder 101
    modal True

    imagebutton:
        auto "blank_%s"
        action Hide("r_menu")

    frame:
        #TODO
        # if renpy.get_mouse_pos()[0] > (2560-296) and renpy.get_mouse_pos()[1] > (1440-419):
        #     xpos (2560-296) ypos (1440-419)
        # elif renpy.get_mouse_pos()[0] > (2560-296):
        #     xpos (2560-296) ypos renpy.get_mouse_pos()[1]
        xpos renpy.get_mouse_pos()[0] ypos renpy.get_mouse_pos()[1]

        if renpy.get_mouse_pos()[0] > (2560-296) and renpy.get_mouse_pos()[1] > (1440-419):
            xanchor 1.0 yanchor 1.0
        elif renpy.get_mouse_pos()[0] > (2560-296):
            xanchor 1.0
        elif renpy.get_mouse_pos()[1] > (1440-419):
            yanchor 1.0
        else:
            xanchor 0.0 yanchor 0.0

        xysize(296, 419)
        background "r_menu_background"

        vbox:
            xalign 0.5 yalign 0.5
            spacing 2

            #存档
            imagebutton:
                auto "r_menu_save_%s"
                action Hide("r_menu"), ShowMenu("save")

            #读档
            imagebutton:
                auto "r_menu_load_%s"
                action Hide("r_menu"), ShowMenu("load")

            #文本回放
            imagebutton:
                auto "r_menu_history_%s"
                action Hide("r_menu", transition=None), ShowMenu("history")

            #设置
            imagebutton:
                auto "r_menu_setting_%s"
                action Hide("r_menu"), ShowMenu("settings")

            #返回标题
            imagebutton:
                auto "r_menu_mainmenu_%s"
                action Hide("r_menu"), MainMenu()

            #退出游戏
            imagebutton:
                auto "r_menu_exit_%s"
                action Quit(confirm=True)




## 输入屏幕 ########################################################################
##
## 此屏幕用于显示 renpy.input。“prompt”参数用于传递文本提示。
##
## 此屏幕必须创建一个 id 为“input”的输入可视控件来接受各种输入参数。
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择屏幕 ########################################################################
##
## 此屏幕用于显示由“menu”语句生成的游戏内选项。参数“items”是一个对象列表，每个对
## 象都有标题和操作字段。
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## 若为True，菜单内的叙述会使用旁白 (narrator) 角色。否则，叙述会显示为菜单内的
## 文字说明。
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 540
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    yalign 0.5
    properties gui.button_text_properties("choice_button")


## 快捷菜单屏幕 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():

    ## 确保该菜单出现在其他屏幕之上，
    zorder 100

    if quick_menu:

        window:
            xsize 561 ysize 65
            align(1.0, 1.0)
            background "quick_bg"

            imagebutton:
                yalign 0.5 xalign 0.03
                auto "quick_system_%s"
                action Show("settings", dissolve)

            imagebutton:
                yalign 0.5 xalign 0.18
                auto "quick_hidedia_%s"
                action HideInterface()

            imagebutton:
                yalign 0.5 xalign 0.34
                auto "quick_autoplay_%s"
                action Preference("auto-forward", "toggle")

            imagebutton:
                yalign 0.5 xalign 0.48
                auto "quick_skip_%s"
                action Skip() alternate Skip(fast=False, confirm=True)

            imagebutton:
                yalign 0.5 xalign 0.63
                auto "quick_quicksave_%s"
                action QuickSave(message=u'已快速保存', newest=True)

            imagebutton:
                yalign 0.5 xalign 0.78
                auto "quick_quickload_%s"
                action QuickLoad()

            imagebutton:
                yalign 0.5 xalign 0.97
                auto "quick_mainmenu_%s"
                action MainMenu()

        if not renpy.get_screen("save") or not renpy.get_screen("load"):
            key "right_click_menu" action Show("r_menu")



## 此代码确保只要玩家没有明确隐藏界面，就会在游戏中显示“quick_menu”屏幕。
init python:
    config.overlay_screens.append("quick_menu")

define quick_menu = True


################################################################################
## 标题和游戏菜单屏幕
################################################################################

## 导航屏幕 ########################################################################
##
## 该屏幕包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("开始游戏") action Start()

        else:

            textbutton _("历史") action ShowMenu("history")

            textbutton _("保存") action ShowMenu("save")

        textbutton _("读取游戏") action ShowMenu("load")

        textbutton _("设置") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("结束回放") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("标题界面") action MainMenu()

        textbutton _("关于") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## “帮助”对移动设备来说并非必须或相关。
            textbutton _("帮助") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("退出") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## 标题菜单屏幕 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## 此代码可确保替换掉任何其他菜单屏幕。
    tag menu

    if main_menu:
        add "main_bg" at main_bg_ani
        # timer 0.01 action Show("main_ui", Dissolve(2.0))
        # use main_ui

# screen main_ui():
#     zorder 101

    if main_menu:

        if first_menu:
            add "main_logo" at main_logo_ani
        else:
            add "main_logo" xalign 0.5 ypos 0.2

        grid 2 1:
            xalign 0.5 yalign 0.77
            xspacing 120
            imagebutton:
                xalign 0.32
                if first_menu:
                    at transform:
                        alpha 0.0
                        pause 8.6
                        linear 2.0 alpha 1.0
                auto "start_%s"
                action [SetVariable("first_menu", False),
                        Start()]

            imagebutton:
                xalign 0.68
                if first_menu:
                    at transform:
                        alpha 0.0
                        pause 8.8
                        linear 2.0 alpha 1.0
                auto  "load_%s"
                action [SetVariable("first_menu", False),
                        ShowMenu("load")]

        grid 4 1:
            xalign 0.5 yalign 0.9
            xspacing 160
            imagebutton:
                if first_menu:
                    at transform:
                        alpha 0.0
                        pause 9.0
                        linear 2.0 alpha 1.0
                auto "setting_%s"
                action [SetVariable("first_menu", False),
                        Show("settings", dissolve)]
            imagebutton:
                if first_menu:
                    at transform:
                        alpha 0.0
                        pause 9.2
                        linear 2.0 alpha 1.0
                auto "extraContent_%s"
                action [SetVariable("first_menu", False),
                        NullAction()]
            imagebutton:
                if first_menu:
                    at transform:
                        alpha 0.0
                        pause 9.4
                        linear 2.0 alpha 1.0
                auto "staff_%s"
                action [SetVariable("first_menu", False),
                        ShowMenu("staffs")]
            imagebutton:
                if first_menu:
                    at transform:
                        alpha 0.0
                        pause 9.6
                        linear 2.0 alpha 1.0
                auto "exit_%s"
                action [SetVariable("first_menu", True),
                        Quit(confirm=main_menu)]
                        # Quit(confirm=not main_menu)]


## 设置屏幕 ######################################################################
##
##

screen settings():

    modal True

    # style_prefix "setting_text"

    fixed:
        add "bg_cover"
        add "setting_bg"

        imagebutton:
            xalign 0.83 yalign 0.21
            auto "setting_close_%s"
            action Hide("settings", dissolve), Return()

        #文本设置
        fixed:
            add "setting_text_title" xalign 0.225 yalign 0.29

            vbox:
                style_prefix "text_setting"
                xalign 0.375 yalign 0.37
                spacing 45
                hbox:
                    spacing 140
                    label _("慢")
                    label _("快")
                    label _("瞬间")

                hbox:
                    spacing 140
                    label _("慢")
                    label _("快")
                    label _("瞬间")

            hbox:
                style_prefix "text_setting"
                xalign 0.3 yalign 0.4
                spacing 80
                vbox:
                    spacing 50
                    label _("文字显示速度")
                    label _("自动播放速度")
                    label _("快 进 设 定")

                vbox:
                    yoffset 20
                    spacing 50
                    bar value Preference("text speed")
                    bar value Preference("auto-forward time"):
                        yoffset 10
                    hbox:
                        yoffset 5
                        spacing 20
                        imagebutton:
                            auto "setting_click_%s"
                            action Preference("skip", "seen")
                        label _("仅限已读")
                        imagebutton:
                            auto "setting_click_%s"
                            action Preference("skip", "all")
                        label _("全部")

            # # 设置速度的三个档 禁用
            # fixed:
            #     if store.Preference("text speed").get_adjustment().value <= 50:
            #         timer 0.2 action Preference("text speed", 1)
            #     elif store.Preference("text speed").get_adjustment().value > 150:
            #         timer 0.2 action Preference("text speed", 200)
            #     else:
            #         timer 0.2 action Preference("text speed", 100)
            #     if store.Preference("auto-forward time").get_adjustment().value <= 7.5:
            #         timer 0.2 action Preference("auto-forward time", 0)
            #     elif store.Preference("auto-forward time").get_adjustment().value > 22.5:
            #         timer 0.2 action Preference("auto-forward time", 30)
            #     else:
            #         timer 0.2 action Preference("auto-forward time", 15)
            # ################################################################

        #画面设置
        fixed:
            add "setting_graphics_title" xalign 0.565 yalign 0.29

            hbox:
                style_prefix "graphics_setting"
                xalign 0.62 yalign 0.4
                spacing 50

                vbox:
                    spacing 50
                    label _("分辨率")
                    label _("全  屏")

                vbox:
                    spacing 25
                    yoffset -5
                    frame:
                        background "setting_graphics_bg"
                        button:
                            xysize(38, 38)
                            xpos 405 yalign 0.5
                            idle_background None
                            hover_background None
                            # idle_background "setting_graphics_btn_idle"
                            # hover_background "setting_graphics_btn_hover"
                            text "2560x1440":
                                font "站酷高端黑修订版1.13.ttf"
                                size 25
                                align(0.5, 0.5)
                                xoffset -220
                            at transform:
                                yoffset -8
                            action NullAction()

                    hbox:
                        spacing 50
                        hbox:
                            spacing 10
                            imagebutton:
                                auto "setting_click_%s"
                                action Preference("display", "fullscreen")
                            label _("是"):
                                style_prefix "mute_setting"
                        hbox:
                            spacing 10
                            imagebutton:
                                auto "setting_click_%s"
                                action Preference("display",  "any window")
                            label _("否"):
                                style_prefix "mute_setting"

        #音乐设置
        fixed:
            add "setting_sound_title" xalign 0.225 yalign 0.57

            vbox:
                style_prefix "text_setting"
                xalign 0.3825 yalign 0.37
                spacing 45
                hbox:
                    spacing 125
                    label _("Min")
                    label _("Max")

                hbox:
                    spacing 125
                    label _("Min")
                    label _("Max")

            hbox:
                style_prefix "sound_setting"
                xalign 0.32 yalign 0.7
                xoffset -20
                spacing 60

                vbox:
                    spacing 70
                    label _("全局音量")
                    label _("音乐音量")

                vbox:
                    yoffset 3
                    spacing 72
                    # bar value Preference("music volume")
                    # bar value Preference("music volume"):
                    #     yoffset 10
                    bar value VariableValue("volume_total", 1.0, action=[Preference("music volume", (volume_total*volume_music)), Preference("voice volume", (volume_total*volume_voice)), Preference("sound volume", (volume_total*volume_sound))])
                    bar value VariableValue("volume_music", 1.0, action=Preference("music volume", volume_total*volume_music)):
                        yoffset 10

                vbox:
                    xoffset -30
                    spacing 60
                    hbox:
                        spacing 10
                        imagebutton:
                            if volume_total > 0.0:
                                auto "setting_click_%s"
                                action SetVariable("volume_total", 0.0), SetVariable("volume_music", 0.0), SetVariable("volume_voice", 0.0), SetVariable("volume_sound", 0.0), Preference("music mute", "enable"), Preference("voice mute", "enable"), Preference("sound mute", "enable")
                            else:
                                auto "setting_toggled_btn_%s"
                                action SetVariable("volume_total", 1.0), SetVariable("volume_music", config.default_music_volume), SetVariable("volume_voice", config.default_voice_volume), SetVariable("volume_sound", config.default_sfx_volume), Preference("music mute", "disable"), Preference("voice mute", "disable"), Preference("sound mute", "disable")
                        label _("静音"):
                            style_prefix "mute_setting"
                    hbox:
                        spacing 10
                        imagebutton:
                            if volume_music > 0.0:
                                auto "setting_click_%s"
                                action SetVariable("volume_music", 0.0), Preference("music mute", "enable")
                            else:
                                auto "setting_toggled_btn_%s"
                                action SetVariable("volume_music", config.default_music_volume), Preference("music mute", "disable")
                        label _("静音"):
                            style_prefix "mute_setting"

            hbox:
                style_prefix "sound_setting"
                xalign 0.72 yalign 0.7
                xoffset -20
                spacing 60

                vbox:
                    spacing 70
                    label _("语音音量")
                    label _("音效音量")

                vbox:
                    yoffset 7
                    spacing 72
                    # bar value Preference("voice volume")
                    # bar value Preference("sound volume"):
                    #     yoffset 10
                    bar value VariableValue("volume_voice", 1.0, action=Preference("voice volume", (volume_total*volume_voice)))
                    bar value VariableValue("volume_sound", 1.0, action=Preference("sound volume", (volume_total*volume_sound))):
                        yoffset 10

                vbox:
                    xoffset -30
                    spacing 60
                    hbox:
                        spacing 10
                        imagebutton:
                            if volume_voice > 0.0:
                                auto "setting_click_%s"
                                action SetVariable("volume_voice", 0.0), Preference("voice mute", "enable")
                            else:
                                auto "setting_toggled_btn_%s"
                                action SetVariable("volume_voice", config.default_voice_volume), Preference("voice mute", "disable")
                        label _("静音"):
                            style_prefix "mute_setting"
                    hbox:
                        spacing 10
                        imagebutton:
                            if volume_sound > 0.0:
                                auto "setting_click_%s"
                                action SetVariable("volume_sound", 0.0), Preference("sound mute", "enable")
                            else:
                                auto "setting_toggled_btn_%s"
                                action SetVariable("volume_sound", config.default_sfx_volume), Preference("sound mute", "disable")
                        label _("静音"):
                            style_prefix "mute_setting"

            ## 音量低于5%自动设置为静音
            # fixed:
            #     if store.MixerValue("music").get_adjustment().value <= 0.05:
            #         $store.MixerValue("music").get_adjustment().value = 0
            #         timer 0.01 action Preference("music mute", "enable")
            #     if store.MixerValue("voice").get_adjustment().value <= 0.05:
            #         $store.MixerValue("voice").get_adjustment().value = 0
            #         timer 0.01 action Preference("voice mute", "enable")
            #     if store.MixerValue("sfx").get_adjustment().value <= 0.05:
            #         $store.MixerValue("sfx").get_adjustment().value = 0
            #         timer 0.01 action Preference("sound mute", "enable")
            ################################################################

style text_setting_slider:
    bar_vertical False
    xsize 355 ysize 19
    base_bar "setting_slider_3_idle"
    thumb "setting_slider_3_btn_idle"

style text_setting_label_text:
    font "经典中圆简.ttf"
    size 26
    color "#343434"

style sound_setting_slider is text_setting_slider:
    xsize 294
    base_bar "setting_slider_2_idle"
    thumb "setting_slider_2_btn_idle"

style sound_setting_label_text is text_setting_label_text

style mute_setting_label_text is sound_setting_label_text:
    bold True

style graphics_setting is text_setting

style graphics_setting_label_text is text_setting_label_text

style sound_setting_bar:
    xysize(294, 19)
    base_bar "setting_slider_2_idle"
    thumb "setting_slider_2_btn_idle"


## 制作人员 ######################################################################
##

screen staffs():

    tag menu

    style_prefix "staffs"

    add "staffs_bg"

    imagebutton:
        yalign 0.02
        auto "staffs_return_btn_%s"
        action Return()

    imagebutton:
        xalign 0.85 yalign 0.542
        auto "staffs_play_btn_%s"
        action NullAction()

    vbox:
        xalign 0.565 yalign 0.60
        spacing 37
        #监督
        frame:
            label _("苍蓝的风")
        #剧本
        frame:
            label _("苍蓝的风")
        #剧本协力
        frame:
            label _("小雨潇潇、木之")
        #CG
        frame:
            label _("九九一木")
        #立绘
        frame:
            label _("九九一木、水树迷")
        #场景
        frame:
            label _("三水猫酱")
        #音乐
        frame:
            label _("麋鹿、灵溪镇的清珏")
        #配音
        frame:
            label _("酒儿")
        #UI
        frame:
            label _("拾九子")
        #程序
        frame:
            label _("芯玫墨韵、远征的苦行僧")

style staffs_label_text:
    font "经典中圆简.ttf"
    size 32
    color "#343434"

style staffs_frame:
    xalign 0.5
    background None

## 游戏菜单屏幕 ######################################################################
##
## 此屏幕列出了游戏菜单的基本共同结构。此屏幕需使用屏幕标题（title）调用，并显示
## 背景、标题和导航菜单。
##
## “scroll”参数可以是“None”，也可以是“viewport”或“vpgrid”。当此屏幕与一个或多个
## 子菜单同时使用时，这些子菜单将被转移（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 60
    top_padding 240

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 560
    yfill True

style game_menu_content_frame:
    left_margin 80
    right_margin 40
    top_margin 20

style game_menu_viewport:
    xsize 1840

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 20

style game_menu_label:
    xpos 100
    ysize 240

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -60


## 关于屏幕 ########################################################################
##
## 此屏幕提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 这个屏幕没有什么特别之处，因此它也是如何制作自定义屏幕的一个例子。

screen about():

    tag menu

    ## 此“use”语句将包含“game_menu”屏幕到此处。子级“vbox”将包含在“game_menu”屏幕
    ## 的“viewport”内。
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")

            ## “gui.about”通常在 options.rpy 中设置。
            if gui.about:
                text "[gui.about!t]\n"

            text _("基于 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## 此变量在 options.rpy 中重新定义，来添加文本到关于屏幕。
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 读取和保存屏幕 #####################################################################
##
## 这些屏幕负责允许玩家保存游戏并将其重新读取。由于它们几乎完全一样，因此它们都
## 是以第三方屏幕“file_slots”来实现的。
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("保存"))


screen load():

    tag menu

    use file_slots(_("读取游戏"))


screen file_slots(title):

    fixed:

        if main_menu:
            add "main_bg"

        add "bg_cover"

        if renpy.get_screen("load"):
            if not main_menu:
                imagebutton:
                    auto "sl_save_btn_%s"
                    xalign 0.25 yalign 0.09
                    action ShowMenu("save")
            # else:
            #     add "sl_save_btn_idle" xalign 0.25 yalign 0.09
            add "sl_bg" align(0.5, 0.5)
            add "sl_load_btn_untoggled" xalign 0.22 yalign 0.08
        elif renpy.get_screen("save"):
            imagebutton:
                auto "sl_load_btn_%s"
                xalign 0.22 yalign 0.09
                action ShowMenu("load")
            add "sl_bg" align(0.5, 0.5)
            add "sl_save_btn_untoggled" xalign 0.25 yalign 0.08

        imagebutton:
            xalign 0.47 yalign 0.845
            auto "sl_page_previous_%s"
            action FilePagePrevious(auto=False, quick=False)

        add "sl_slot_page_background" xalign 0.5 yalign 0.845 yoffset 5
        if FilePageName() == "10":
            text _(FilePageName()):
                xalign 0.5 yalign 0.845
                style "sl_page"
        else:
            text _(str(0) + FilePageName()):
                xalign 0.5 yalign 0.845
                style "sl_page"

        imagebutton:
            xalign 0.53 yalign 0.845
            auto "sl_page_next_%s"
            action FilePageNext(max=10, auto=False, quick=False)

        imagebutton:
            xalign 0.825 yalign 0.15
            auto "sl_close_%s"
            action Return()

        grid 3 3:
            style_prefix "slot"
            align(0.5, 0.5)
            xspacing 50
            yspacing 70

            for i in range (1, 10):
                button:
                    idle_background "sl_slot_bg"
                    hover_background "sl_slot_bg_hover"
                    action FileAction(i)
                    add "sl_slot_bg" align(0.5,0.5)
                    add FileScreenshot(i) align(0.5,0.5) size(461, 251)
                    # text FileTime(i, format=_("{#file_time}%Y年%B%d日  %H:%M"), empty=_("")):
                    #     color "#fff" xalign 0.5 ypos 240 size 30
                    # text FileSaveName(i)
                    key "save_delete" action FileDelete(i)


style slot_button:
    xsize 461 ysize 251

style sl_page is text

style sl_page_text:
    xalign 0.5 yalign 0.845
    size 42
    font "站酷高端黑修订版1.13.ttf"
    color "#15153c"


## 设置屏幕 ########################################################################
##
## 设置屏幕允许玩家配置游戏以更好地适应自己。
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("设置"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("显示")
                        textbutton _("窗口") action Preference("display", "window")
                        textbutton _("全屏") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("回退控制区")
                    textbutton _("禁用") action Preference("rollback side", "disable")
                    textbutton _("左侧") action Preference("rollback side", "left")
                    textbutton _("右侧") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("快进")
                    textbutton _("未读文本") action Preference("skip", "toggle")
                    textbutton _("选项后继续") action Preference("after choices", "toggle")
                    textbutton _("忽略转场") action InvertSelected(Preference("transitions", "toggle"))

                ## 可以在此处添加类型为“radio_pref”或“check_pref”的其他“vbox”，
                ## 以添加其他创建者定义的首选项设置。

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("文字速度")

                    bar value Preference("text speed")

                    label _("自动前进时间")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("音乐音量")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("音效音量")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("语音音量")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

# style slider_label is pref_label
# style slider_label_text is pref_label_text

# style slider_slider is gui_slider
# style slider_button is gui_button
# style slider_button_text is gui_button_text
# style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 4

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 450

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")




## 历史屏幕 ########################################################################
##
## 这是一个向玩家显示对话历史的屏幕。虽然此屏幕没有任何特殊之处，但它必须访问储
## 存在“_history_list”中的对话历史记录。
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## 避免预缓存此屏幕，因为它可能非常大。
    predict False

    add "black_bg"

    use history_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:
                bottom_margin 50

                ## 此代码可确保如果“history_height”为“None”的话仍可正常显示条
                ## 目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        substitute False
                        style "history_name"

                        ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述
                        ## 人文本中。
                        # if "color" in h.who_args:
                        #     text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                if h.who:
                    text what:
                        substitute False
                        font "经典中圆简.ttf"
                        color "#ffffff"
                else:
                    text "{i}" + what + "{/i}":
                        substitute False
                        font "经典中圆简.ttf"
                        color "#a7a7a7"

                if h.voice.filename != None:

                    imagebutton:
                        xalign 0.93
                        auto "history_voiceReplay_btn_%s"
                        action Play("voice", h.voice.filename)

        if not _history_list:
            label _("对话历史记录为空。")


## 此代码决定了允许在历史记录屏幕上显示哪些标签。
define gui.history_allow_tags = set()


style history_window is empty

style history_name is empty
style history_name_text is empty
style history_text is empty

style history_text is empty

style history_label is empty
style history_label_text is empty

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    size 48
    font "站酷高端黑修订版1.13.ttf"
    color "#989898"
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    line_spacing 15
    size 38
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
    size 48
    font "站酷高端黑修订版1.13.ttf"
    color "#989898"


## 历史菜单屏幕 ######################################################################
##

screen history_menu(title, scroll=None, yinitial=0.0):

    frame:
        align(0.5, 0.5)
        top_padding 220
        bottom_padding 220
        left_padding 220
        right_padding 220
        background None

        hbox:

            ## 导航部分的预留空间。
            # frame:
            #     style "game_menu_navigation_frame"

            frame:

                background None

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    imagebutton:
        yalign 0.05
        auto "history_return_btn_%s"
        action Return()


## 帮助屏幕 ########################################################################
##
## 提供有关键盘和鼠标映射信息的屏幕。它使用其它屏幕
## （“keyboard_help”，“mouse_help“和”gamepad_help“）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 30

            hbox:

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("推进对话但不选择选项。")

    hbox:
        label _("方向键")
        text _("导航界面。")

    hbox:
        label _("Esc")
        text _("访问游戏菜单。")

    hbox:
        label _("Ctrl")
        text _("按住时快进对话。")

    hbox:
        label _("Tab")
        text _("切换对话快进。")

    hbox:
        label _("Page Up")
        text _("回退至先前的对话。")

    hbox:
        label _("Page Down")
        text _("向前至之后的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截图。")

    hbox:
        label "V"
        text _("切换辅助{a=https://www.renpy.org/l/voicing}自动朗读{/a}。")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")

    hbox:
        label _("鼠标滚轮上\n点击回退控制区")
        text _("回退至先前的对话。")

    hbox:
        label _("鼠标滚轮下")
        text _("向前至之后的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至之后的对话。")


    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 16

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 500
    right_padding 40

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## 其他屏幕
################################################################################


## 确认屏幕 ########################################################################
##
## 当 Ren'Py 需要询问玩家是非问题时，会调用确认屏幕。
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此屏幕时，确保其他屏幕无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    # add "gui/overlay/confirm.png"

    frame:
        align(0.5, 0.5)
        background "confirm_bg"

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 60

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                # spacing 200
                spacing 30

                button:
                    xysize(182, 44)
                    idle_background "confirm_btn_idle"
                    hover_background "confirm_btn_hover"
                    action yes_action
                    text _("确定"):
                        style "confirm_yn"
                        idle_color "#343434"
                        hover_color "#ecb25b"
                        align(0.5, 0.5)
                # textbutton _("确定"):
                #     style "confirm_yn"
                #     action yes_action

                button:
                    xysize(182, 44)
                    idle_background "confirm_btn_idle"
                    hover_background "confirm_btn_hover"
                    action no_action
                    text _("取消"):
                        style "confirm_yn"
                        idle_color "#343434"
                        hover_color "#ecb25b"
                        align(0.5, 0.5)
                # textbutton _("取消"):
                #     style "confirm_yn"
                #     action no_action

            # hbox:
            #     xalign 0.5
            #     spacing 200


    ## 右键点击退出并答复“no”（取消）。
    key "game_menu" action no_action


style confirm_yn is confirm_prompt

style confirm_yn_text:
    font "站酷高端黑修订版1.13.ttf"
    idle_color "#343434"
    hover_color "#ecb25b"
    size 40

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    size 32
    color "#c9c4b6"
    font "经典中圆简.ttf"
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## 快进指示屏幕 ######################################################################
##
## “skip_indicator”屏幕用于指示快进正在进行中。
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    pass

    # zorder 100
    # style_prefix "skip"

    # frame:

    #     hbox:
    #         spacing 12

    #         text _("正在快进")

    #         text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
    #         text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
    #         text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“BLACK RIGHT-POINTING SMALL TRIANGLE”字形的字体。
    font "DejaVuSans.ttf"


## 通知屏幕 ########################################################################
##
## 通知屏幕用于向玩家显示消息。（例如，当游戏快速保存或已截屏时。）
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    color "#ffffff"
    font "经典中圆简.ttf"
    properties gui.text_properties("notify")


## NVL 模式屏幕 ####################################################################
##
## 此屏幕用于 NVL 模式的对话和菜单。
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## 在“vpgrid”或“vbox”中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 如果给定，则显示“menu”。 如果“config.narrator_menu”设置为“True”，
        ## 则“menu”可能显示不正确，如前述。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此代码控制一次可以显示的最大 NVL 模式条目数。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 900

## 由于鼠标可能不存在，我们将快捷菜单替换为更容易触摸且按钮更少更大的版本。
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("回退") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 680

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 800

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 1200

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from notifypy import Notify
import os, subprocess

mod = "mod4"
TERM = "kitty"
HOME = os.getenv("HOME")

colors = [
    # fg         bg         boarder
    [ "#aaaaaa", "#2d3036", "#2d3036" ],
    [ "#eeeeee", "#474c57", "#474c57" ]
]

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(["xsetroot", "-solid", "#1c1d21"])

@lazy.function
def notify_send(qtile, title, desc, icon, audio):
    n = Notify()
    n.title = title 
    n.message = desc
    n.icon = icon or f"{HOME}/.local/share/icons/wm/qtile.png"
    n.audio = audio or f"{HOME}/.audios/bell.wav"
    #FIX add the default selected media in notify_send to the paths
    n.send()

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

@lazy.function
def move_floating_window_left(qtile):
    #ADD write move_floating_window with arrow keys functions
    pass

@lazy.function
def move_floating_window_right(qtile):
    pass

@lazy.function
def move_floating_window_up(qtile):
    pass

@lazy.function
def move_floating_window_down(qtile):
    pass

keys = [
    #Key([mod], "h", lazy.layout.left()),
    #Key([mod], "l", lazy.layout.right()),
    #Key([mod], "j", lazy.layout.down()),
    #Key([mod], "k", lazy.layout.up()),

    Key([mod], "j", lazy.layout.next()),
    Key([mod], "k", lazy.layout.previous()),
    Key([mod], "h", lazy.layout.shrink_main()),
    Key([mod], "l", lazy.layout.grow_main()),
    #FIX floating windows are not included in the windows stack

    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod], "m", lazy.window.toggle_fullscreen()),
    Key([mod], "f", lazy.window.toggle_floating()),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    #Key([mod, "shift"], "j", lazy.layout.shrink()),
    #Key([mod, "shift"], "k", lazy.layout.grow()),

	#Key([mod, "shift"], 'j', lazy.layout.decrease_ratio()),
    #Key([mod, "shift"], 'k', lazy.layout.increase_ratio()),

    #Key([mod, "control"], "h", lazy.layout.grow_left()),
    #Key([mod, "control"], "l", lazy.layout.grow_right()),
    #Key([mod, "control"], "j", lazy.layout.grow_down()),
    #Key([mod, "control"], "k", lazy.layout.grow_up()),

    Key([mod, "shift"], "Return", lazy.spawn(TERM)),
    Key([mod], "p", lazy.spawn("dmenu_run -sb #d75f5f")),
    Key([mod], "b", lazy.spawn("qutebrowser")),

    Key([mod, "control"], "space", lazy.layout.flip()),
    Key([mod, "control"], "o", lazy.layout.maximize()),
    Key([mod], "n", lazy.layout.normalize()),

    Key([mod], "Return", lazy.layout.toggle_split()),
    Key([mod], "space", lazy.next_layout()),
    Key([mod, "shift"], "space", lazy.prev_layout()),
    Key([mod], "u", lazy.next_screen()),
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "semicolon", lazy.prev_screen()),
    Key([mod], "o", lazy.screen.next_group()),
    Key([mod, "shift"], "o", lazy.screen.prev_group()),

    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "shift", "control"], "q", lazy.shutdown()),
    #Key([mod], "p", lazy.spawncmd()),

    Key([mod], 'equal',
        lazy.spawn('pactl set-sink-volume 0 +10%')),
    Key([mod, "control"], 'equal',
        lazy.spawn('pactl set-sink-volume 0 -10%')),
    Key([mod, "shift"], 'equal',
        lazy.spawn('pactl set-sink-mute 0 toggle')), 

    #Key([], 'XF86AudioRaiseVolume', lazy.spawn('pulseaudio-ctl up 5')),
    #Key([], 'XF86AudioLowerVolume', lazy.spawn('pulseaudio-ctl down 5')),
    #Key([], 'XF86AudioMute', lazy.spawn('pulseaudio-ctl set 1')), 

    #ADD <Print>
    #Key([], "Print", 
    #    lazy.spawn("scrot -l style=solid,width=2,colors=red -s"),
    #    notify_send("Screenshot", icon=f"{HOME}/.icons/screenshot.png")),

    #ADD function/binding : control stack num
                
    Key([mod], "Left", move_floating_window_left()), 
    Key([mod], "Right", move_floating_window_right()), 
    Key([mod], "Up", move_floating_window_up()), 
    Key([mod], "Down", move_floating_window_down()) 
]

groups = [Group(
    name=i,
    layout="monadtall",
    label=i
) for i in "123456789"]
grpsBindings = [
    "ampersand", "eacute", "quotedbl", 
    "apostrophe", "parenleft", "minus",
    "egrave", "underscore", "ccedilla"]

for grp, key in zip(groups, grpsBindings):
    keys.extend([
       Key([mod], key, lazy.group[grp.name].toscreen()),
       Key([mod, "shift"], key, 
          lazy.window.togroup(grp.name, switch_group=True))
    ])

layout_defaults = {
    "border_width" : 2,
    "border_normal" : colors[0][2],
    "border_focus" : colors[1][2],
    "margin" : 14,
}

layouts = [
    layout.MonadTall(
        **layout_defaults,
        ratio=0.6,
        change_ratio=0.05,
        new_client_position="top"
    ),
    #layout.Columns(
    #    **layout_defaults,
    #    border_focus_stack="#d75f5f",
    #    num_stack=2
    #),
    #layout.Max(),
    #layout.Floating(**layout_defaults),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(**layout_defaults),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = {
    "font" : "FiraCode Nerd",
    "fontsize" : 10,
    "foreground" : colors[0][0],
    "background" : colors[0][1],
    "padding" : 5,
}

def init_bar():
    return [
         widget.Spacer(length=10),
         widget.CurrentLayout(),
         widget.GroupBox(
             highlight_method='block',
             rounded=False,
             inactive=colors[0][0],
             active=colors[1][0],
             other_current_screen_border="#d75f5f",
             other_screen_border="#5a606e",
             this_current_screen_border="#d75f5f",
             this_screen_border="#5a606e",
             urgent_alert_method="line",
             urgent_border="#ff0000",
             #hide_unused=True,
             padding_x=10,
             margin_x=0
         ),
         widget.Prompt(),
         widget.WindowName(
             for_current_screen=True,
             empty_group_string="Desktop"
         ),
         widget.Systray(
            icon_size=16
         ),
         widget.Clock(
              format="%a %d %b at %k:%M"
         ),
         widget.Spacer(length=10)
    ]

screens = [
    Screen( top=bar.Bar(widgets=init_bar(), size=20),
    ),
    Screen(
        top=bar.Bar(widgets=init_bar(), size=20),
    )
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button1", lazy.window.bring_to_front()),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="TelegramDesktop"),
        Match(wm_class="arandr"),
    ],
    **layout_defaults
)

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

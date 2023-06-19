import subprocess, os
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

######## VARIABLES #########

mod = "mod4"
terminal = "alacritty"

######## AUTOSTART #########

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

######## KEYBINDING #########

keys = [
    Key([mod, "shift"], "Return", 
        lazy.spawn(terminal), 
        desc="Launch terminal"
    ),

    Key([mod], "h", 
        lazy.layout.left(), 
        desc="Move focus to left"
    ),
    Key([mod], "l", 
        lazy.layout.right(), 
        desc="Move focus to right"
    ),
    Key([mod], "j", 
        lazy.layout.down(), 
        desc="Move focus down"
    ),
    Key([mod], "k", 
        lazy.layout.up(), 
        desc="Move focus up"
    ),
    Key([mod], "q", 
        lazy.window.kill(), 
        desc="Kill focused window"
    ),

    Key([mod], "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"
    ),
    Key([mod], "Return", 
        lazy.layout.toggle_split(), 
        desc="Toggle between split and unsplit sides of stack"
    ),

    Key([mod, "shift"], "h", 
        lazy.layout.shuffle_left(), 
        desc="Move window to the left"
    ),
    Key([mod, "shift"], "l", 
        lazy.layout.shuffle_right(), 
        desc="Move window to the right"
    ),
    Key([mod, "shift"], "j", 
        lazy.layout.shuffle_down(),
        desc="Move window down"
    ),
    Key([mod, "shift"], "k", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"
    ),

    Key([mod, "control"], "h", 
        lazy.layout.grow_left(), 
        desc="Grow window to the left"
    ),
    Key([mod, "control"], "l", 
        lazy.layout.grow_right(), 
        desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", 
        lazy.layout.grow_down(), 
        desc="Grow window down"
    ),
    Key([mod, "control"], "k", 
        lazy.layout.grow_up(), 
        desc="Grow window up"
    ),
    Key([mod], "n", 
        lazy.layout.normalize(),
        desc="Reset all window sizes"
    ),

    Key([mod, "control"], "r", 
        lazy.reload_config(), 
        desc="Reload the config"
    ),
    Key([mod, "control"], "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile"
    ),
]

######## GROUPS AND LAYOUT #########

groups = [Group(i, layout="columns") for i in "123456789"]
grpsAzertyKeys = ["ampersand","eacute","quotedbl","apostrophe","parenleft","minus", "egrave", "underscore", "ccedilla"]

for i, group in enumerate(groups, 0):
    keys.extend(
        [
            Key([mod], grpsAzertyKeys[i], 
                lazy.group[group.name].toscreen(toggle=False),
                desc=f"Switch to group {group.name}"
            ),
            Key([mod, "shift"], grpsAzertyKeys[i], 
                lazy.window.togroup(group.name), 
                desc=f"Move focused window to group {group.name}"
            )
        ]
    )

layout_theme = {
    "border_width": 3,
    "border_focus": "#474c57",
    "border_normal": "#2d3036"
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(),
    # layout.Floating(**layout_theme)
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

######## SCREENS, BAR AND WIDGET #########


widget_defaults = dict(
    foreground= "#eeeeee",
    background= "#2d3036",
    fontsize= 12,
    font= "sans",
    padding= 3,
)
extension_defaults = widget_defaults.copy()

screens = [
    #Screen(),
    Screen(
        bottom=bar.Bar(
            widgets=[
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p')
            ],
            size=24,
        )
    )
]

######## MOUSE & FLOATING #########
mouse = [
    Drag(
        [mod], "Button1", 
        lazy.window.set_position_floating(), 
        start=lazy.window.get_position()),
    Drag(
        [mod], "Button3", 
        lazy.window.set_size_floating(), 
        start=lazy.window.get_size()),
    Click(
        [mod], "Button2", 
        lazy.window.bring_to_front()),
]

############  OTHER  #############

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="pcmanfs"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

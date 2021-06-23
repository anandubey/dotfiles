
import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook, qtile
from libqtile.widget import Spacer

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')


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

myTerm = "alacritty" # My terminal of choice

keys = [



# SUPER + FUNCTION KEYS

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "p", lazy.spawn('dmenu_recency')),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "t", lazy.spawn('alacritty')),
    Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "b", lazy.spawn('google-chrome-stable')),
    Key([mod], "Escape", lazy.spawn('betterlockscreen -l dimblur')),
    Key([mod], "Return", lazy.spawn('alacritty')),
    Key([mod], "KP_Enter", lazy.spawn('alacritty')),
    Key([mod], "e", lazy.spawn('thunar')),
    Key([mod], "x", lazy.spawn('xkill')),

# SUPER + SHIFT KEYS

    Key([mod, "shift"], "Return", lazy.spawn('pcmanfm')),
    #Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
    Key([mod, "shift"], "d", lazy.spawn(home + '/.config/qtile/scripts/dmenu.sh')),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift"], "x", lazy.shutdown()),

# CONTROL + ALT KEYS

    Key(["mod1", "control"], "c", lazy.spawn('catfish')),
    Key(["mod1", "control"], "i", lazy.spawn('nitrogen')),
    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key(["mod1", "control"], "t", lazy.spawn('termite')),
    Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),
    Key(["mod1", "control"], "Return", lazy.spawn('termite')),

# ALT + ... KEYS


    # Key(["mod1"], "p", lazy.spawn('pamac-manager')),
    # Key(["mod1"], "f", lazy.spawn('firedragon')),
    # Key(["mod1"], "e", lazy.spawn('emacs')),
    # Key(["mod1"], "m", lazy.spawn('pcmanfm')),
    # Key(["mod1"], "w", lazy.spawn('garuda-welcome')),


# CONTROL + SHIFT KEYS

    # Key([mod2, "shift"], "Escape", lazy.spawn('lxtask')),


# SCREENSHOTS

    Key([], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
    Key([mod2], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
#    Key([mod2, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),

# MULTIMEDIA KEYS

# INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

#    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
#    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

         ### Treetab controls
    Key([mod, "control"], "k",
        lazy.layout.section_up(),
        desc='Move up a section in treetab'
        ),
    Key([mod, "control"], "j",
        lazy.layout.section_down(),
        desc='Move down a section in treetab'
        ),



# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    ]

groups = []

# FOR QWERTY KEYBOARDS
#group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
group_names = ["1", "2", "3", "4", "5",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]
group_labels = ["", "", "", "", "",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

#group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "treetab", "floating",]
group_layouts = ["bsp", "monadtall", "monadtall", "monadtall", "floating",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


# COLORS FOR THE BAR

def init_colors():
    return [["#2b2f37", "#2b2f37"], # color 0
            ["#1d2021", "#1d2021"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#d3869b", "#d3869b"], # color 3
            ["#646870", "#646870"], # color 4
            ["#ffffff", "#ffffff"], # color 5
            ["#fb4934", "#fb4934"], # color 6
            ["#8ec07c", "#8ec07c"], # color 7
            ["#fbf1c7", "#fbf1c7"], # color 8
            ["#d65d0e", "#d65d0e"], # color 9
            ["#88C0D0", "#88C0D0"], # color 10
            ["#adb1b9", "#adb1b9"], # color 11
            ["#fe8019", "#fe8019"]]# color 12

colors = init_colors()


def init_layout_theme():
    return {"margin":10,
            "border_width":2,
            "border_focus": colors[7][0],
            "border_normal": colors[4][0]
            }

layout_theme = init_layout_theme()


layouts = [
    layout.MonadTall(margin=12, border_width=2, border_focus=colors[7][0], border_normal=colors[4][0]),
    layout.MonadWide(margin=12, border_width=2, border_focus=colors[7][0], border_normal=colors[4][0]),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Columns(**layout_theme),
    #layout.Stack(**layout_theme),
    #layout.Tile(**layout_theme),
    #layout.TreeTab(
    #    sections=['FIRST', 'SECOND'],
    #    bg_color = '#141414',
    #    active_bg = '#0000ff',
    #    inactive_bg = '#1e90ff',
    #    padding_y =5,
    #    section_top =10,
    #    panel_width = 280),
    #layout.VerticalTile(**layout_theme),
    #layout.Zoomy(**layout_theme)
]



# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [

            #    widget.TextBox(
            #        font = 'Material Design Icons',
            #            text = '',
            #            background = colors[1],
            #            foreground = colors[0],
            #            fontsize = 18,
            #            ),
		widget.CurrentLayoutIcon(
			custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
			foreground = colors[2],
			background = colors[1],
			padding = 0,
			scale = 0.5
		),
		widget.CurrentLayout(
			font = "JetBrainsMono Nerd Font Bold",
			fontsize = 12,
			foreground = colors[2],
			background = colors[1]
		),
        widget.Sep(
			linewidth = 0,
			padding = 10,
			foreground = colors[1],
			background = colors[1]
		),
		widget.GroupBox(
			font="FontAwesome",
			hide_unused=  True,
			fontsize = 26,
			margin_y = 2,
			margin_x = 10,
			padding_y = 6,
			padding_x = 4,
			borderwidth = 0,
			disable_drag = False,
			active = colors[11],
			inactive = colors[4],
			rounded = False,
			highlight_method = "text",
			this_current_screen_border = colors[8],
			foreground = colors[4],
			background = colors[0],
			urgent_alert_method = 'border',
		),
                # widget.TextBox(
                #    font = 'Material Design Icons',
                #        text = '',
                #        background = colors[1],
                #        foreground = colors[0],
                #        padding = 0,
                #        fontsize = 18,
                #        ),

              
		widget.Sep(
			linewidth = 0,
			padding = 10,
			foreground = colors[1],
			background = colors[1]
		),
		widget.Spacer(
			length=bar.STRETCH,
		),
		widget.WindowName(font="JetBrainsMono Nerd Font",
			fontsize = 14,
			foreground = colors[5],
			background = colors[1],
			empty_group_string = 'p5ypher',
			max_chars = 40,
		),
		widget.Spacer(
			length=bar.STRETCH,
		),


                # widget.BatteryIcon(
                #     battery = 0,
                #       theme_path="/home/p5ypher/.config/qtile/icons/battery_icons_horiz",
                #       update_interval = 30,
                #       background = colors[9]
                #       ),
                # battery option 2  from Qtile
            #    widget.Battery(
            #             font="Noto Sans",
            #             update_interval = 10,
            #             fontsize = 12,
            #             foreground = colors[5],
            #             background = colors[9],
            #             ),


		widget.Sep(
			linewidth = 0,
			padding = 10,
			foreground = colors[0],
			background = colors[1]
		),

		widget.CheckUpdates(
			font = 'JetBrainsMono Nerd Font Bold',
			fontsize = 14,
			update_interval = 1,
			distro = 'Arch_checkupdates',
			display_format = "{updates} Updates",
			foreground = colors[5],
			mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
			background = colors[1],
		),
		widget.Sep(
			linewidth = 0,
			padding = 10,
			foreground = colors[0],
			background = colors[1]
		),
		widget.TextBox(
			font="FontAwesome Bold",
			text="",
			foreground="#d19a66",
			background=colors[1],
			fontsize=26
		),
		widget.Sep(
			linewidth = 0,
			padding = 3,
			foreground = colors[0],
			background = colors[1]
		),

		widget.Memory(
			font="JetBrainsMono Nerd Font Bold",
			format = '{MemUsed} MB',
			update_interval = 1,
			fontsize = 14,
			foreground = colors[5],
			background = colors[1],
			mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
		),
		widget.Sep(
			linewidth = 0,
			padding = 10,
			foreground = colors[0],
			background = colors[1]
		),
		widget.TextBox(
			font="FontAwesome Bold",
			text=" ",
			foreground=colors[7],
			background=colors[0],
			padding = 2,
			fontsize=34
		),
		widget.Wlan(
					font = 'JetBrainsMono Nerd Font',
				fontsize = 14,
					interface="wlp3s0",
					disconnected_message = "No Internet",
					format = ' {essid}',
					update_interval = 3,
					foreground=colors[5],
					background=colors[0],
					padding = 0,
					),
		widget.Sep(
				linewidth = 0,
				padding = 10,
				foreground = colors[0],
				background = colors[0]
				),
		widget.Sep(
				linewidth = 0,
				padding = 10,
				foreground = colors[1],
				background = colors[1]
				),

		widget.TextBox(
				font="FontAwesome Bold",
				text=" ",
				foreground=colors[10],
				background=colors[1],
				padding = 0,
				fontsize=32
				),

		widget.Volume(
			font = 'JetBrainsMono Nerd Font Bold',
				fontsize = 14,
				foreground = colors[5],
				background = colors[1],
				padding = 5
				),


		widget.Sep(
				linewidth = 0,
				padding = 10,
				foreground = colors[1],
				background = colors[1]
				),
		widget.Sep(
				linewidth = 0,
				padding = 10,
				foreground = colors[0],
				background = colors[0]
				),
		widget.TextBox(
				font="FontAwesome Bold",
				text="  ",
				foreground=colors[8],
				background=colors[0],
				padding = 0,
				fontsize=26
				),

		widget.Clock(
				foreground = colors[5],
				background = colors[0],
				font = 'JetBrainsMono Nerd Font Bold',
				fontsize = 14,
				format="%Y-%m-%d"
				),
		widget.Sep(
				linewidth = 0,
				padding =5,
				foreground = colors[5],
				background = colors[0]
				),

		widget.TextBox(
				font="FontAwesome Bold",
				text="  ",
				foreground=colors[12],
				background=colors[0],
				padding = 0,
				fontsize=30
				),
		widget.Clock(
				foreground = colors[5],
				background = colors[0],
				font = 'JetBrainsMono Nerd Font Bold',
				fontsize = 14,
				format="%H:%M"
				),
		widget.Sep(
				linewidth = 0,
				padding = 10,
				foreground = colors[5],
				background = colors[0]
				),

		widget.Sep(
				linewidth = 0,
				padding = 10,
				foreground = colors[1],
				background = colors[1]
				),

		widget.Systray(
				background = colors[1],
				foreground = colors[1],
				icon_size=20,
				padding = 4
				),
		widget.Sep(
				linewidth = 0,
				padding = 10,
				foreground = colors[1],
				background = colors[1],
				),

              ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26, opacity=1)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26, opacity=1))]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    #########################################################
    ################ assgin apps to groups ##################
    #########################################################
    d["1"] = ["Alacritty", "Kitty", "Knosole", "Xfce4-terminal",
                "alacritty", "kitty", "konsole", "xfce4-terminal",]
    d["2"] = ["Navigator", "Firefox", "Chromium", "Google-chrome", "Brave", "Brave-browser",
                "navigator","firefox", "chromium", "google-chrome", "brave", "brave-browser",]
    d["3"] = [ "Atom", "Subl", "Geany", "Brackets", "Code-oss", "Codme", "TelegramDesktop", "Discord",
               "atom", "subl", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
    d["4"] = ["Nitrogen", "Feh", "Viewnior", "Arandr",
                "nitrogen", "feh", "viewnior", "arandr",]
    d["5"] = ["Gimp", "Pamac-manager", "Thunar",
                "gimp", "pamac-manager", "thunar"]
    # d["6"] = ["Vlc","vlc", "Mpv", "mpv" ]
    # d["7"] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
    #           "virtualbox manager", "virtualbox machine", "vmplayer", ]
    # d["8"] = ["pcmanfm", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
    #           "pcmanfm", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
    # d["9"] = ["Evolution", "Geary", "Mail", "Thunderbird",
    #           "evolution", "geary", "mail", "thunderbird" ]
    # d["0"] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
    #           "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
    ##########################################################
    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME



main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

#@hook.subscribe.startup
#def start_always():
#    # Set the cursor to something sane in X
#    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'Arandr'},
    {'wmclass': 'feh'},
    {'wmclass': '/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1'},
    {'wname': 'branchdialog'},
    {'wmclass': 'arcolinux-logout'},
    {'wname': 'Open File'},
    {'wname': 'pinentry'},
    {'wmclass': 'ssh-askpass'},
    {'wmclass': 'lxpolkit'},
    {'wmclass': 'Lxpolkit'},
    {'wmclass': 'yad'},
    {'wmclass': 'Yad'},


],  fullscreen_border_width = 0, border_width = 2)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"

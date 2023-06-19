config.load_autoconfig(False)

c.aliases = {
    'q': 'quit',
    'w': 'session-save',
    'wq': 'quit --save'
}

c.downloads.location.directory = '~/Garbage'

c.tabs.show = 'multiple'

c.url.default_page = 'file:///home/amen/.config/qutebrowser/landing_page.html' 
c.url.start_pages = ['file:///home/amen/.config/qutebrowser/landing_page.html'] 

c.url.searchengines = {
    'DEFAULT': 'https://www.google.com/search?q={}',
    'wk': 'https://en.wikipedia.org/wiki/{}',
    'gs': 'https://scholar.google.com/scholar?q={}',
    'dd': 'https://duckduckgo.com/?q={}',
    'pb': 'https://thepiratebay.org/search.php?q={}',
    'go': 'https://www.google.com/search?q={}',
    'yt': 'https://www.youtube.com/results?search_query={}',
    'aw': 'https://wiki.archlinux.org/?search={}',
    'pm': 'https://voidlinux.org/packages/?arch=x86_64&q={}',
}

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = ['#7f8388', '#7f8388', '#7f8388']

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#2d3036'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#2d3036'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#d3dae3'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = '#474c57'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = '#474c57'
#c.colors.completion.category.border.top = '#3f4147'

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = '#474c57'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = '#2d3036'

# Background color of the selected completion item.
# Type: QssColor
#c.colors.completion.item.selected.bg = '#3da2ff'
c.colors.completion.item.selected.bg = '#ecbe7b'

# Foreground color of the matched text in the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.match.fg = '#3da2ff'

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = '#3da2ff'

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = 'white'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#282c34'

# Background color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.bg = '#ff6c6b'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = '#282c34'

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = '#98be65'

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = '#282c34'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#474c57'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = 'white'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#474c57'

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = '#34426f'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#474c57'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = 'yellow'

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = '#2d3036'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#2d3036'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#2d3036'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#474c57'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#474c57'

# Background color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.bg = 'seagreen'

# Background color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.bg = 'darkseagreen'

# Background color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.bg = '#282c34'

# Background color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.bg = '#282c34'

# Default font families to use. Whenever "default_family" is used in a
# font setting, it's replaced with the fonts listed here. If set to an
# empty value, a system-specific monospace default is used.
# Type: List of Font, or Font
c.fonts.default_family = 'monospace'

# Default font size to use. Whenever "default_size" is used in a font
# setting, it's replaced with the size listed here. Valid values are
# either a float value with a "pt" suffix, or an integer value with a
# "px" suffix.
# Type: String
c.fonts.default_size = '14px'

# Font used in the completion widget.
# Type: Font
c.fonts.completion.entry = 'default_size default_family'

# Font used for the debugging console.
# Type: Font
c.fonts.debug_console = 'default_size default_family'

c.fonts.prompts = 'default_size default_family'

c.fonts.statusbar = 'default_size default_family'



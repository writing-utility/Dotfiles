local themes_path = require("gears.filesystem").get_themes_dir()
local media = "/home/amen/.theme"
local dpi = require("beautiful.xresources").apply_dpi

local theme = {}
theme.wallpaper = "#1c1d21" -- ~0%

theme.font = "Ubuntu 9"

theme.fg_normal  = "#7f8388"
theme.fg_focus   = "#d3dae3"
theme.fg_urgent  = "#eeeeee"
theme.bg_normal  = "#2d3036" -- ~7%
theme.bg_focus   = "#474c57" -- ~14%
theme.bg_urgent  = "#d75f5f"
theme.bg_systray = theme.bg_normal

theme.useless_gap   = dpi(5)
theme.border_width  = dpi(2)
theme.border_normal = "#2d3036"
theme.border_focus  = "#474c57" -- ~21%
theme.border_marked = "#d75f5f"

theme.tasklist_disable_icon = true

-- There are other variable sets
-- overriding the default one when
-- defined, the sets are:
-- [taglist|tasklist]_[bg|fg]_[focus|urgent|occupied|empty|volatile]
-- titlebar_[normal|focus]
-- tooltip_[font|opacity|fg_color|bg_color|border_width|border_color]
-- Example:
--theme.taglist_bg_focus = "#CC9393"
-- }}}

-- {{{ Widgets
-- You can add as many variables as
-- you wish and access them by using
-- beautiful.variable in your rc.lua
--theme.fg_widget        = "#AECF96"
--theme.fg_center_widget = "#88A175"
--theme.fg_end_widget    = "#FF5656"
--theme.bg_widget        = "#494B4F"
--theme.border_widget    = "#3F3F3F"
-- }}}

-- {{{ Mouse finder
theme.mouse_finder_color = "#CC9393"
-- mouse_finder_[timeout|animate_timeout|radius|factor]
-- }}}


-- {{{ Icons
-- {{{ Taglist
theme.taglist_squares_sel   = themes_path .. "default/taglist/squarefz.png"
theme.taglist_squares_unsel = themes_path .. "default/taglist/squarez.png"
--theme.taglist_squares_resize = "false"
-- }}}

-- {{{ Layout
theme.layout_tile       = themes_path .. "default/layouts/tile.png"
theme.layout_tileleft   = themes_path .. "default/layouts/tileleft.png"
theme.layout_tilebottom = themes_path .. "default/layouts/tilebottom.png"
theme.layout_tiletop    = themes_path .. "default/layouts/tiletop.png"
theme.layout_fairv      = themes_path .. "default/layouts/fairv.png"
theme.layout_fairh      = themes_path .. "default/layouts/fairh.png"
theme.layout_spiral     = themes_path .. "default/layouts/spiral.png"
theme.layout_dwindle    = themes_path .. "default/layouts/dwindle.png"
theme.layout_max        = themes_path .. "default/layouts/max.png"
theme.layout_fullscreen = themes_path .. "default/layouts/fullscreen.png"
theme.layout_magnifier  = themes_path .. "default/layouts/magnifier.png"
theme.layout_floating   = themes_path .. "default/layouts/floating.png"
theme.layout_cornernw   = themes_path .. "default/layouts/cornernw.png"
theme.layout_cornerne   = themes_path .. "default/layouts/cornerne.png"
theme.layout_cornersw   = themes_path .. "default/layouts/cornersw.png"
theme.layout_cornerse   = themes_path .. "default/layouts/cornerse.png"
-- }}}

return theme

-- vim: filetype=lua:expandtab:shiftwidth=4:tabstop=8:softtabstop=4:textwidth=80

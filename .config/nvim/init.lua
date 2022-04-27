require('packer-config')
require('options')
require('lualine-config')
require('bufferline-config')
require('nvim-tree-config')
require('treesitter-config')
require('autopair-config')
require('keybindings')
require('whichkey-config')
require('telescope-config')
require('lsp-config')
require('colorizer-config')
require('zen-config')
vim.cmd('colorscheme gruvbox-material')
vim.g.gruvbox_material_palette = "mix"
vim.g.gruvbox_material_background = "medium"
vim.g.gruvbox_material_enable_bold = 1
vim.g.gruvbox_material_sign_column_background = "none"


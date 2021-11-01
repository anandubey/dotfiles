require("bufferline").setup{}
vim.cmd[[
  nnoremap <C-TAB> :BufferLineCycleNext<CR>
  nnoremap <silent><S-TAB> :BufferLineCyclePrev<CR>
]]

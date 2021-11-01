-- Setup lspconfig.
local capabilities = require('cmp_nvim_lsp').update_capabilities(vim.lsp.protocol.make_client_capabilities())

require'lspconfig/configs'.ls_emmet = {
  default_config = {
    cmd = { 'ls_emmet', '--stdio' };
    filetypes = { 'html', 'css', 'scss' }; -- Add the languages you use, see language support
    root_dir = function(_)
      return vim.loop.cwd()
    end;
    settings = {};
  };
}

local system_name
if vim.fn.has("mac") == 1 then
  system_name = "macOS"
elseif vim.fn.has("unix") == 1 then
  system_name = "Linux"
elseif vim.fn.has('win32') == 1 then
  system_name = "Windows"
else
  print("Unsupported system for sumneko")
end


local runtime_path = vim.split(package.path, ';')
table.insert(runtime_path, "lua/?.lua")
table.insert(runtime_path, "lua/?/init.lua")

local langservers = {
  'ccls',
  'html',
  'cssls',
  'tsserver',
  'pylsp',
  'ls_emmet',
}

for _, server in ipairs(langservers) do
    require'lspconfig'[server].setup {
      capabilities = capabilities
    }
end


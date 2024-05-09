require "nvchad.mappings"

-- add yours here

local map = vim.keymap.set

map("v", "<C-c>", "y", {desc = "Copy"})
map("n", "<leader>f", "<cmd>Telescope<cr>", { desc = "Telescope Find files" })

map("n", "<A-h>", function()
  require("nvchad.term").new { pos = "sp", size = 0.3 }
end, { desc = "Terminal New horizontal term" })

map({ "n", "t" }, "<leader>h", function()
  require("nvchad.term").toggle { pos = "sp", id = "htoggleTerm", size = 0.3 }
end, { desc = "Terminal New horizontal term" })

map("n", ";", ":", { desc = "CMD enter command mode" })
map("i", "jk", "<ESC>")

-- map({ "n", "i", "v" }, "<C-s>", "<cmd> w <cr>")

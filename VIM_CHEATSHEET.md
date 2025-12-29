# 📝 Vim Cheat Sheet - Panduan Lengkap untuk Pemula

## 🚀 Dasar-dasar Vim

### Mode di Vim
Vim punya 3 mode utama:
1. **Normal Mode** (default) - untuk navigasi & perintah
2. **Insert Mode** - untuk menulis/edit text
3. **Visual Mode** - untuk select text

### Membuka & Keluar Vim
```bash
vim namafile.txt        # Buka file
vim +10 namafile.txt    # Buka di baris 10
:q                      # Quit (kalau belum edit)
:q!                     # Quit tanpa save (force)
:w                      # Save
:wq                     # Save & quit
:x                      # Save & quit (shortcut)
ZZ                      # Save & quit (di normal mode)
```

## ✏️ Mode Insert (Menulis Text)

### Masuk Insert Mode
```
i       # Insert sebelum cursor
I       # Insert di awal baris
a       # Append setelah cursor
A       # Append di akhir baris
o       # Open line baru di bawah
O       # Open line baru di atas
```

### Keluar Insert Mode
```
Esc     # Kembali ke Normal Mode
```

## 🎯 Navigasi (Normal Mode)

### Gerakan Dasar
```
h       # Kiri
j       # Bawah
k       # Atas
l       # Kanan

w       # Next word
b       # Previous word
e       # End of word

0       # Awal baris
^       # First non-blank character
$       # Akhir baris

gg      # Awal file
G       # Akhir file
:10     # Ke baris 10
10G     # Ke baris 10
```

### Scroll Screen
```
Ctrl+f  # Page down
Ctrl+b  # Page up
Ctrl+d  # Half page down
Ctrl+u  # Half page up
zz      # Center screen pada cursor
```

## ✂️ Edit Text (Normal Mode)

### Delete
```
x       # Delete character di cursor
X       # Delete character sebelum cursor
dd      # Delete line
dw      # Delete word
d$      # Delete sampai akhir baris
d0      # Delete sampai awal baris
5dd     # Delete 5 baris
```

### Copy & Paste
```
yy      # Yank (copy) line
yw      # Yank word
y$      # Yank sampai akhir baris
5yy     # Yank 5 baris

p       # Paste setelah cursor
P       # Paste sebelum cursor
```

### Undo & Redo
```
u       # Undo
Ctrl+r  # Redo
```

### Replace
```
r       # Replace 1 character
R       # Replace mode (overwrite)
cw      # Change word (delete & insert)
cc      # Change line
C       # Change sampai akhir baris
```

## 🔍 Search & Replace

### Search
```
/keyword        # Search forward
?keyword        # Search backward
n               # Next match
N               # Previous match
*               # Search word under cursor
```

### Replace
```
:s/old/new/         # Replace first occurrence in line
:s/old/new/g        # Replace all in line
:%s/old/new/g       # Replace all in file
:%s/old/new/gc      # Replace with confirmation
```

## 📋 Visual Mode (Select Text)

### Masuk Visual Mode
```
v       # Visual character mode
V       # Visual line mode
Ctrl+v  # Visual block mode
```

### Operations di Visual Mode
```
d       # Delete selected
y       # Yank (copy) selected
c       # Change selected
>       # Indent right
<       # Indent left
```

## 🎨 Praktis untuk Coding

### Indentation
```
>>      # Indent right
<<      # Indent left
5>>     # Indent 5 baris
```

### Comment Multiple Lines
```
1. Ctrl+v (visual block)
2. Pilih baris dengan j/k
3. Shift+I
4. Ketik #
5. Esc
```

### Uncomment Multiple Lines
```
1. Ctrl+v (visual block)
2. Pilih # dengan j/k
3. x (delete)
```

## 📂 Multiple Files

### Working with Buffers
```
:e file.txt         # Edit file baru
:bn                 # Next buffer
:bp                 # Previous buffer
:bd                 # Delete buffer (close)
:ls                 # List buffers
:b 2                # Switch ke buffer 2
```

### Split Windows
```
:split file.txt     # Horizontal split
:vsplit file.txt    # Vertical split
Ctrl+w w            # Switch window
Ctrl+w q            # Close window
Ctrl+w h/j/k/l      # Navigate windows
```

### Tabs
```
:tabnew file.txt    # New tab
:tabn               # Next tab
:tabp               # Previous tab
:tabclose           # Close tab
gt                  # Next tab (normal mode)
gT                  # Previous tab
```

## 🛠️ Advanced Tips

### Line Numbers
```
:set number         # Show line numbers
:set nonumber       # Hide line numbers
:set relativenumber # Relative line numbers
```

### Syntax Highlighting
```
:syntax on          # Enable syntax
:syntax off         # Disable syntax
```

### Copy dari Vim ke Clipboard
```
# Visual mode, select text
"+y                 # Copy to system clipboard
"+p                 # Paste from system clipboard
```

### Macros (Recording)
```
qa                  # Start recording to register 'a'
... perintah ...
q                   # Stop recording
@a                  # Play macro 'a'
5@a                 # Play macro 5x
```

## 🎯 Workflow untuk Project Ini

### 1. Setup File Structure
```bash
mkdir -p templates data
```

### 2. Create app.py
```bash
vim app.py
# Tekan i
# Paste kode
# Esc, :wq
```

### 3. Create Templates
```bash
# Template 1
vim templates/base.html
# i, paste, Esc, :wq

# Template 2
vim templates/index.html
# i, paste, Esc, :wq

# Dan seterusnya...
```

### 4. Edit Multiple Templates
```bash
# Buka semua sekaligus
vim templates/*.html

# Switch files:
:next       # Next file
:prev       # Previous file
:first      # First file
:last       # Last file
```

## 💡 Pro Tips

### Quick Save
```
# Di normal mode
:w<Enter>
# Atau
Shift+ZZ
```

### Jump to Definition (Python)
```
gd              # Go to definition
Ctrl+]          # Jump to tag (perlu ctags)
Ctrl+o          # Jump back
```

### Fast Editing
```
ciw             # Change inner word
ci"             # Change dalam quotes
dit             # Delete inner tag (HTML)
```

### Search Project-wide
```
:vimgrep /pattern/ **/*.py
:copen          # Open quickfix list
:cn             # Next result
:cp             # Previous result
```

## 🔧 .vimrc Configuration

Buat file `~/.vimrc` untuk config permanent:

```vim
" Basic Settings
set number              " Show line numbers
set relativenumber      " Relative line numbers
set tabstop=4           " Tab = 4 spaces
set shiftwidth=4        " Indent = 4 spaces
set expandtab           " Use spaces instead of tabs
set autoindent          " Auto indent
set smartindent         " Smart indent
set mouse=a             " Enable mouse
set clipboard=unnamedplus  " System clipboard

" Search Settings
set ignorecase          " Ignore case in search
set smartcase           " Case sensitive if uppercase
set hlsearch            " Highlight search
set incsearch           " Incremental search

" Visual
syntax on               " Syntax highlighting
set cursorline          " Highlight current line
set showmatch           " Show matching brackets

" Shortcuts
" Save with Ctrl+S
nnoremap <C-s> :w<CR>
inoremap <C-s> <Esc>:w<CR>a

" Quick quit
nnoremap <leader>q :q<CR>

" Remove highlight
nnoremap <leader><space> :nohlsearch<CR>
```

## 📚 Resources

- Vim Tutorial: `vimtutor` (jalankan di terminal)
- Interactive: https://vim-adventures.com/
- Cheatsheet: https://devhints.io/vim

## ⚡ Quick Reference

**Most Used Commands:**
```
i           Insert mode
Esc         Normal mode
:wq         Save & quit
dd          Delete line
yy          Copy line
p           Paste
u           Undo
/search     Search
:10         Go to line 10
```

---

**Practice makes perfect! Happy Vimming! 🎉**

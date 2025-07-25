# 🐲 Mole

**Mole** is a minimal Bash tool that dumps the content of an entire directory into a single text file.  
It’s perfect for sharing code with **ChatGPT** or other AI tools, without needing Git.

> 🔁 Alternative to [Gitingest](https://github.com/cyclotruc/gitingest) — but no Git, no setup, just files.

---

## 💡 Why use it?

- 🧠 AI-friendly: Share full codebase context in one go.
- ⚡ Fast: Ideal for debugging, refactoring, or support.
- 📦 Git-free: Works on any directory, no repo required.
- 🌍 Remote-ready: Run with a single command from anywhere.

---

## ⚙️ What it does

- Recursively scans a directory.
- Excludes files/directories via blacklist (like `.gitignore`).
- Outputs all file contents in a single structured file.

---

## 🌀 Remote usage

You can run **Mole** directly from GitHub with:

```bash
bash <(curl -s https://raw.githubusercontent.com/Zalaya/Mole/main/script.sh) [options] [root_directory]
```

> [!TIP]
> **Use Mole as a global command**
>
> Add this alias to your shell config (`~/.bashrc`, `~/.zshrc`) to call Mole from anywhere:
>
> ```bash
> alias mole='bash <(curl -s https://raw.githubusercontent.com/Zalaya/Mole/main/script.sh)'
> ```
>
> Then simply run:
>
> ```bash
> mole -o output.txt -b blacklist.txt ./root_directory
> ```

---

## 🖥️ Local usage

```bash
git clone https://github.com/Zalaya/Mole.git
cd Mole
chmod +x script.sh
./script.sh [options] [root_directory]
```

## 🔧 Options

```bash
./script.sh [OPTIONS] [ROOT_DIRECTORY]
```

| Short | Long             | Description                                               |
| ----- | ---------------- | --------------------------------------------------------- |
| `-o`  | `--output`       | Output file name (default: `output.txt`)                  |
| `-b`  | `--blacklist`    | Path to blacklist file (excludes files/directories)       |
| `-w`  | `--watch`        | Enable watch mode to regenerate output on any file change |
| `-h`  | `--help`         | Show usage help                                           |
|       | `ROOT_DIRECTORY` | Root directory to scan (default: current directory `"."`) |

---

## 🧾 Blacklist format

Just like `.gitignore`:

```txt
# Ignore directories
.git/
node_modules/
dist/

# Ignore files
.env
```

* One relative path per line.
* Supports directories or files.
* Comments with `#`.

---

## 🕒 Watch mode

Use `-w` or `--watch` to keep the output file updated in real time whenever something changes in the directory:

```bash
mole -o output.txt -b blacklist.txt -w .
````

## ✅ Requirements

### 🐍 Bash

* Bash (v4+).
* Tools: `find`, `sed`, `cat`.

Compatible with Linux, macOS, WSL, Git Bash on Windows.

---

## 📘 License

[GNU v3 License](https://github.com/Zalaya/Mole/blob/main/LICENSE) — © [Zalaya](https://github.com/Zalaya)

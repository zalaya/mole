# 🐲 Mole

**Mole** is a minimal Bash tool that dumps the content of an entire directory into a single text file.  
Perfect for sharing code with **ChatGPT** or other AI tools, without needing Git.

> 🔁 Alternative to [Gitingest](https://github.com/coderamp-labs/gitingest) — but no Git, no setup, just files.

---

## 💡 Why use it?

- 🧠 AI-friendly – Send your whole codebase to LLMs.
- ⚡ Fast – Minimal dependencies, pure Bash.
- 📦 Git-free – Works on any folder.
- 🌍 Remote-ready – Run from GitHub in one command.
- 🛡️ Blacklist support – Ignore files or dirs like `.gitignore`.
- 🔄 Watch mode – Auto-update output on changes.

---

## ⚙️ What it does

- Recursively scans a directory.
- Excludes files/directories via blacklist (like `.gitignore`).
- Outputs all file contents in a single structured file.

---

## 🌀 Remote usage

You can run **Mole** directly from GitHub with:

```bash
bash <(curl -s https://raw.githubusercontent.com/zalaya/mole/main/script.sh) [options] [root_directory]
```

---

## 🖥️ Local usage

```bash
git clone https://github.com/zalaya/mole.git
cd mole
chmod +x script.sh
./script.sh [options] [root_directory]
```

---

## 🌍 Global installation (recommended)

Install Mole as a system-wide command:

```bash
sudo curl -sL https://raw.githubusercontent.com/zalaya/mole/main/script.sh -o /usr/local/bin/mole
sudo chmod +x /usr/local/bin/mole
```

Then run:

```bash
mole [options] [root_directory]
```

---

## 🔧 Options

```bash
mole [OPTIONS] [ROOT_DIRECTORY]
```

| Short | Long             | Description                                               |
| ----- | ---------------- | --------------------------------------------------------- |
| `-o`  | `--output`       | Output file name (if not provided, prints to stdout)      |
| `-b`  | `--blacklist`    | Path to blacklist file (excludes files/directories)       |
| `-w`  | `--watch`        | Enable watch mode to regenerate output on any file change |
| `-i`  | `--interval`    | Watch polling interval in seconds (default: 5)             |
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

---

## 🕒 Watch mode

Keep the output updated in real time:

```bash
mole -o output.txt -b blacklist.txt -w .
```

---

## 🔥 Pipes & Advanced usage

With `stdout` support, Mole can be used in Unix pipelines:

```bash
# Count total lines of code
mole | wc -l

# Search for TODO comments
mole | grep "TODO"

# Output compressed archive
mole | gzip > project.txt.gz

# Compare two directories
diff <(mole dir1) <(mole dir2)
```

---

## ✅ Requirements

* **Bash** v4+
* Tools: `find`, `sed`, `stat`, `sha256sum`, `awk`

Compatible with Linux, macOS, WSL, Git Bash on Windows.

---

## 📘 License

[GNU v3 License](https://github.com/zalaya/mole/blob/main/LICENSE) — © [Zalaya](https://github.com/zalaya)

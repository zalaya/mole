# 🐲 Mole

**Mole** is a lightweight **Bash tool** that concatenates the entire content of a directory into a single text file.
Perfect for sharing projects with **ChatGPT** or other AI tools – **no Git required**.

> 🔁 A minimal alternative to [Gitingest](https://github.com/coderamp-labs/gitingest) — no repos, no setup, just files.

---

## 🚀 Features

* 🧠 **AI-friendly** – Send your full codebase to LLMs.
* ⚡ **Fast & minimal** – Pure Bash, no dependencies.
* 🛡️ **Blacklist support** – Ignore files and folders (`.gitignore` style).
* 🔄 **Watch mode** – Auto-updates output when files change.
* 🌍 **Remote or global usage** – Run directly from GitHub or install system-wide.

---

## 🌀 Quick usage (no install)

```bash
bash <(curl -s https://raw.githubusercontent.com/zalaya/mole/main/script.sh) [options] [directory]
```

---

## 🛠️ Global installation

```bash
sudo curl -sL https://raw.githubusercontent.com/zalaya/mole/main/script.sh -o /usr/local/bin/mole
sudo chmod +x /usr/local/bin/mole
```

Then run:

```bash
mole [options] [directory]
```

---

## ⚙️ Options

| Short | Long             | Description                                    |
| ----- | ---------------- | ---------------------------------------------- |
| `-o`  | `--output`       | Output file name (prints to stdout by default) |
| `-b`  | `--blacklist`    | File with ignore patterns                      |
| `-w`  | `--watch`        | Watch mode: regenerate on any file change      |
| `-i`  | `--interval`     | Polling interval in seconds (default: `5`)     |
| `-h`  | `--help`         | Show help message                              |
|       | `ROOT_DIRECTORY` | Directory to scan (default: `"."`)             |

---

## 🧾 Blacklist example

Works like `.gitignore`:

```txt
# Ignore directories
.git/
node_modules/

# Ignore files
.env
```

---

## 🔥 Examples

```bash
# Generate a concatenated file
mole -o output.txt .

# Live updates on changes
mole -w .

# Count total lines of code
mole | wc -l

# Find TODO comments
mole | grep "TODO"

# Compare two directories
diff <(mole dir1) <(mole dir2)
```

---

## ✅ Requirements

* **Bash** v4+
* Tools: `find`, `sed`, `stat`, `sha256sum`, `awk`
* Works on Linux, macOS, WSL, Git Bash (Windows)

---

## 📄 License

[GNU v3 License](https://github.com/zalaya/mole/blob/main/LICENSE) – © [Zalaya](https://github.com/zalaya)

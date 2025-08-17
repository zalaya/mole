# 🐲 Mole

**Mole** is a lightweight **Bash tool** that concatenates the entire content of a directory into a single text file.
Perfect for sharing projects with **ChatGPT** or other AI tools – **no Git required**.

---

## 🚀 Features

* 🧠 **AI-friendly** – Send your full codebase to LLMs.
* ⚡ **Fast & minimal** – Pure Bash, no dependencies.
* 🛡️ **Blacklist support** – Ignore files and folders with a custom pattern file.
* 🔄 **Watch mode** – Auto-updates output when files change.
* 🌍 **Remote or global usage** – Run directly from GitHub or install system-wide.
* 📝 **Text-only** – Binary files (e.g. images, PDFs) are skipped.

---

## 🌀 Quick usage

```bash
bash <(curl -s https://raw.githubusercontent.com/Zalaya/mole/v1.3.0/script.sh) [options] [directory]
```

---

## 🛠️ Global installation

```bash
sudo curl -sL https://raw.githubusercontent.com/Zalaya/mole/v1.3.0/script.sh -o /usr/local/bin/mole
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

## 🧾 Blacklist file example

```txt
# Ignored directories
.git/
node_modules/

# Ignored files
.env
```

## ✅ Requirements

* **Bash** v4+.  
* Tools: `find`, `sed`, `stat`, `sha256sum`, `awk`, `file`.
* Works on Linux, macOS, WSL, Git Bash (Windows).

---

## 📄 License

[GNUv3 License](https://github.com/Zalaya/mole/blob/main/LICENSE) – © [Zalaya](https://github.com/Zalaya)

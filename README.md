<p align="center">
  <img src="https://github.com/7h3-h4k3r/P067sc4NN36/blob/main/image/logo.png" alt="Banner Grabbing Tool" width="600"/>
</p>
---

```markdown
# 🛰️ BannerGrabbing Tool

```bash
       _          (`-. 
       \`----.    ) ^_`)
,__     \__   `\_/  ( `
 \_\      \__  `|   }
    \  .--' \__/    }    D3vOps : Sridharanitharan.B
     ))/   \__,<  /_/    Version : 0.1
     ((|  _/_/ `\ \_\_   Model : Banner Grabbing Tool 
      `\_____\  )__\
```

A lightweight and professional **banner grabbing** tool built in Python, designed for reconnaissance and ethical hacking. Extract banners from network services to identify running software and versions.

## 🔥 Features

- Connects to a specified IP and port to retrieve banners
- Easy CLI usage with flags: `--ip`, `--port`
- Clean terminal output with color and ASCII art
- Fast, minimal, and ideal for scripting

## ⚙️ Requirements

- Python 3.x
- `colorama` (for colored terminal output)

Install it with:

```bash
pip install colorama
```

## 📥 Installation

```bash
git clone https://github.com/7h3-h4k3r/BannerGrapping.git
cd BannerGrapping
```

## 🧪 Usage

```bash
python3 banner.py --ip <target-ip> --port <target-port>
```

### Example

```bash
python3 banner.py --ip 192.168.1.10 --port 80
```

### Output

```
[+] Connecting to 192.168.1.10:80
[+] Banner: HTTP/1.1 200 OK
Server: Apache/2.4.41 (Ubuntu)
...
```

## ⚠️ Disclaimer

This tool is intended **only for educational and authorized penetration testing**. Use on unauthorized systems is strictly prohibited and illegal.

## 👤 Author

- **Name:** Sridharanitharan.B
- **Role:** D3vOps / Cybersecurity Enthusiast
- **Version:** 0.1
- **Model:** Banner Grabbing Tool

---

```
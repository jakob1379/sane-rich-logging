# 🌟 Sane Rich Logging - Sparkling Logging Made Simple! 🚀

Welcome to **Sane Rich Logging**! ✨ A beautiful logging package that makes setting up robust and pretty logging in Python a breeze! With rich console output and flexible file handling, your logs will shine brighter than ever! ✨🔮

## 🎉 Features

- **Rich Logging Console Output** 🌈: Make your logs delightful with colorful, informative formatting.
- **Rotating File Logs** 🗂️: Keep your logs neat and tidy with built-in rotation.
- **Simple Integration** 🚀: Plug and play with minimal configuration.

## 🚀 Installation

Use your favorite tool to install the package

```bash
pip install sane-rich-logging
poetry install sane-rich-logging
uv add sane-rich-logging
```


## 💡 Usage

With **Sane Rich Logging**, setting up logging is easy-peasy! 🍋 Here is how to use it:

### Setting Up Logging

Just import the package and call `setup_logging()` to configure your logger:

```python
from sane_rich_logging import setup_logging

setup_logging()
```

### Running the Example

You can also run the package directly to see the magic in action! 🌠

```bash
python -m sane_rich_logging
```

![Example Output](assets/example.png)

The **console output** is visually pleasing, providing clear and colorful messages for each log level, while the **written log** is saved in a detailed format for easier debugging and tracking:

```
2024-11-22 11:38:00,187 [DEBUG] [__main__.py:11] - This is a debug message.
2024-11-22 11:38:00,190 [INFO] [__main__.py:12] - This is an info message.
2024-11-22 11:38:00,191 [WARNING] [__main__.py:13] - This is a warning message.
2024-11-22 11:38:00,192 [ERROR] [__main__.py:14] - This is an error message.
2024-11-22 11:38:00,193 [CRITICAL] [__main__.py:15] - This is a critical message.
```

✨ It's that simple to make your logging glimmer with **Sane Rich Logging**! 🎇

## ❤️ Contributions Welcome

Have ideas or want to help make **Sane Rich Logging** even shinier? Feel free to submit an issue or pull request! Contributions are more than welcome! 🌟

## 📄 License

This project is licensed under the MIT License. 📝

---

Enjoy logging, the **sparkling** way! 🪄✨

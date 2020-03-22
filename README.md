# File Sorter

The purpose of this program is to automatically sort a given directory. 

## Getting Started

These instructions should help you get a copy of this program up and running.

### Prerequisites

These prerequisites only apply if you are not using the standalone application.

- Python 3.6+

- The external packages `watchdog` and `toml`, which can be installed via the following in the command prompt:
  ```
  pip install watchdog
  pip install toml
  ```

### Changing folders and extensions

The extensions and their corresponding folders to be sorted into can be changed inside the `config.txt` config file. To add a new folder to sort into, you just apply the following template inside `config.txt`:
```
[folders]
...
FolderName = [
	'extension',
	'...'
]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for further details.

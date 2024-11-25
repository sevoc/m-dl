# Maxon App Downloader for macOS

## Requirements

To run the scripts on **macOS**, you'll need the following:

### Homebrew

[Homebrew](https://brew.sh/) is a popular package manager for macOS that allows you to easily install and manage software packages. If you don’t have Homebrew installed, follow the steps below.

#### How to Install Homebrew:

1. Open the **Terminal** application on your Mac.
2. Run the following command to install Homebrew:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. Follow the on-screen instructions to complete the installation.

Once Homebrew is installed, you can use it to install other required tools like `jq` and `curl`.

### Python 3.x

You’ll need **Python 3** to run the Python script. It’s usually pre-installed on macOS, but if you need to install or update it, you can use Homebrew:

```bash
brew install python
```

After Python is installed, you'll use **`pip3`** to install the required Python packages.

---

## Python Script: `download-maxon-apps.py`

### Requirements

To run the Python script on **macOS**, you’ll need the following:

- **Python 3.x** (You can install it with `brew install python` if not already installed)
- Required Python packages:
  - `requests` (for making HTTP requests)
  - `tqdm` (for showing a download progress bar)

You can install the required Python packages using `pip3`:

```bash
pip3 install requests tqdm
```

### Script Overview

The Python script interacts with Maxon’s API to list available applications, their versions, and download URLs. It offers the following functionality:
- Fetches a list of available applications and versions from the Maxon API.
- Allows the user to select an app and a version to download.
- Downloads the app using `requests`, showing a progress bar with `tqdm`.

### How to Run the Python Script

1. Clone the repository or download the `download-maxon-apps.py` script.
2. Install the necessary Python packages:
   ```bash
   pip3 install requests tqdm
   ```
3. Run the script:
   ```bash
   python3 download-maxon-apps.py
   ```
4. Follow the interactive prompts to select an app, choose a version, and download the app to your specified directory.

---

## Bash Script: `download-maxon-apps.sh`

### Requirements

The Bash script requires the following tools:

- **Bash shell**
- **`jq`** (for parsing JSON)
- **`curl`** (for downloading files)

You can install the required dependencies with the following commands using **Homebrew**:

```bash
brew install jq curl
```

### Script Overview

The Bash script works similarly to the Python script but is intended for users who prefer using a shell script. It offers the following functionality:
- Fetches the list of available applications and their versions from Maxon’s API using `curl`.
- Allows the user to select an app and version.
- Downloads the selected app using `curl`, showing a progress bar.

### How to Run the Bash Script

1. Clone the repository or download the `download-maxon-apps.sh` script.
2. Install the required dependencies:
   ```bash
   brew install jq curl
   ```
3. Make the script executable:
   ```bash
   chmod +x download-maxon-apps.sh
   ```
4. Run the script:
   ```bash
   ./download-maxon-apps.sh
   ```
5. Follow the interactive prompts to select an app, choose a version, and download the app to your specified directory.

---

## Responsible Usage

### Fair Use of Resources

Both the Python and Bash scripts make HTTP requests to Maxon’s API to retrieve information about available applications. While the scripts are designed to be efficient, it’s important to use them responsibly:
- **Avoid overloading the API**: Repeated, excessive requests to the Maxon API in a short time can overload their servers. Use the script responsibly and try to limit requests to what is necessary.
- **Respect rate limits**: If the API provides any rate-limiting functionality (e.g., limiting the number of requests per minute), ensure that you respect those limits.
- **Download responsibly**: Only download what you need. Refrain from bulk downloading of applications unless you have a legitimate need to do so.

### Privacy and Security

- **Data Privacy**: The scripts fetch information directly from the Maxon API and do not collect or store personal data. However, always be cautious when running scripts that access external services.
- **Secure Downloads**: Ensure that you are downloading software only from trusted sources. This script relies on the Maxon API for downloading applications, which is the official source. Always verify the source of the software to ensure it's legitimate.

### Ethical Considerations

- **Legal Compliance**: Ensure that you have the legal right to download and use the software you’re accessing through these scripts. These scripts are intended for personal or educational use and should not be used for downloading software in violation of any terms of service.
- **Intellectual Property**: Respect the intellectual property rights of the software developers. Download software only for legitimate purposes, and do not distribute it without proper authorization.

---

## Common Usage Notes

Both scripts allow the user to:
1. **Select multiple apps** from the list of available applications.
2. **Choose a version** of the selected app.
3. **Download the app** to a specified directory with a progress bar.
4. If any error occurs (e.g., network issues, missing dependencies), the scripts will display an error message and exit.

If you need to download apps multiple times, you can simply rerun the script and repeat the process.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

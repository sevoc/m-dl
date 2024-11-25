# Maxon App Downloader

This repository contains two scripts designed to download applications from Maxon’s API. One script is written in **Python**, and the other in **Bash**. Both scripts fetch a list of available applications and their versions, allow the user to select the desired app and version, and download the selected application to a specified directory.

## Python Script: `download-maxon-apps.py`

### Requirements

To run the Python script, you’ll need the following:

- **Python 3.x**
- Required Python packages:
  - `requests` (for making HTTP requests)
  - `tqdm` (for showing a download progress bar)

You can install the required packages using `pip`:

```bash
pip install requests tqdm
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
   pip install requests tqdm
   ```
3. Run the script:
   ```bash
   python download-maxon-apps.py
   ```
4. Follow the interactive prompts to select an app, choose a version, and download the app to your specified directory.

---

## Bash Script: `download-maxon-apps.sh`

### Requirements

The Bash script requires the following tools:

- **Bash shell**
- **`jq`** (for parsing JSON)
- **`curl`** (for downloading files)

You can install the required dependencies with the following commands:

```bash
sudo apt install jq curl
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
   sudo apt install jq curl
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

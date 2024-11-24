import json
import requests
import os
import sys
from tqdm import tqdm
from typing import Dict, List
from urllib.parse import unquote

# Configuration variables
MAXON_API_URL = "https://packages.maxon.net/query?type=installer&platform=macos&latestReleasesOnly=1"
DOWNLOAD_DIR = os.path.expanduser("~/Downloads/maxon-apps")  # Downloads directory

class MaxonDownloader:
    def __init__(self, download_dir: str):
        self.download_dir = os.path.abspath(download_dir)
        self.apps_data = self.load_json()

    def load_json(self) -> List[Dict]:
        """Load and parse the JSON from Maxon API."""
        try:
            response = requests.get(MAXON_API_URL)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data from Maxon API: {e}")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Error: Invalid JSON response from API")
            sys.exit(1)

    def get_download_url(self, name: str, version: str) -> str:
        """Get the actual download URL from the Maxon API."""
        info_url = f"https://packages.maxon.net/content?id={name}&platform=macos&v={version}"
        try:
            response = requests.get(info_url)
            response.raise_for_status()
            url_data = response.json()
            
            if url_data and isinstance(url_data, list) and len(url_data) > 0:
                download_url = url_data[0].get('download_url')
                if download_url:
                    return download_url
                
            raise ValueError("No download URL found in response")
            
        except (requests.RequestException, json.JSONDecodeError, ValueError) as e:
            print(f"Error getting download URL: {e}")
            sys.exit(1)

    def get_clean_filename(self, url: str) -> str:
        """Extract and clean the filename from the URL."""
        decoded_url = unquote(url)
        filename = decoded_url.split('/')[-1]
        filename = filename.split('?')[0]
        return filename

    def list_apps(self) -> Dict[int, Dict]:
        """List all available apps and return a mapping of selection number to app data."""
        print("\nAvailable apps:")
        apps_map = {}
        
        # Group apps by name to handle multiple versions
        apps_by_name = {}
        for app in self.apps_data:
            name = app.get('name', '')
            version = app.get('version', '')
            full_name = app.get('fullName', name)  # Use fullName if available
            
            if name not in apps_by_name:
                apps_by_name[name] = {
                    'versions': [],
                    'fullName': full_name
                }
            apps_by_name[name]['versions'].append({
                'name': name,
                'version': version,
                'fullName': full_name
            })

        # Display unique apps
        for idx, (name, data) in enumerate(apps_by_name.items(), 1):
            print(f"{idx}. {data['fullName']}")
            apps_map[idx] = {'name': name, 'versions': data['versions'], 'fullName': data['fullName']}

        return apps_map

    def select_version(self, versions: List[Dict]) -> Dict:
        """Let user select a specific version from the list."""
        print("\nAvailable versions:")
        for idx, version_data in enumerate(versions, 1):
            print(f"{idx}. {version_data['version']}")

        while True:
            try:
                choice = int(input("\nSelect version number: "))
                if 1 <= choice <= len(versions):
                    return versions[choice - 1]
                print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a number.")

    def download_file(self, url: str, destination: str):
        """Download a file with progress bar."""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            
            with open(destination, 'wb') as f:
                with tqdm(
                    total=total_size,
                    unit='iB',
                    unit_scale=True,
                    desc=os.path.basename(destination)
                ) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        size = f.write(chunk)
                        pbar.update(size)
            
            print(f"\nSuccessfully downloaded to {destination}")
            
        except requests.exceptions.RequestException as e:
            print(f"Error downloading file: {e}")
            sys.exit(1)

    def run(self):
        """Main execution flow."""
        while True:
            # List apps and get selection
            apps_map = self.list_apps()
            
            try:
                choice = int(input("\nSelect app number (or 0 to exit): "))
                if choice == 0:
                    break
                if choice not in apps_map:
                    print("Invalid selection. Please try again.")
                    continue
                
                # Get selected app data
                selected_app = apps_map[choice]
                
                # Select version
                version_data = self.select_version(selected_app['versions'])
                
                # Get the actual download URL from the API
                download_url = self.get_download_url(version_data['name'], version_data['version'])
                
                # Get clean filename
                filename = self.get_clean_filename(download_url)
                destination = os.path.join(self.download_dir, filename)
                
                # Confirm download
                print(f"\nPreparing to download:")
                print(f"App: {version_data['fullName']}")
                print(f"Version: {version_data['version']}")
                print(f"Filename: {filename}")
                print(f"Destination: {destination}")
                
#               if input("\nProceed with download? (y/n): ").lower() == 'y':
                self.download_file(download_url, destination)
                
#               if input("\nDownload another app? (y/n): ").lower() != 'y':
#                   break
                    
            except ValueError:
                print("Please enter a number.")

def main():
    downloader = MaxonDownloader(DOWNLOAD_DIR)
    downloader.run()

if __name__ == "__main__":
    main()
#!/bin/bash

# Configuration variables
MAXON_API_URL="https://packages.maxon.net/query?type=installer&platform=macos&latestReleasesOnly=1"
DOWNLOAD_DIR="$HOME/Downloads/maxon-apps"

# Check for required commands
if ! command -v jq &> /dev/null; then
    echo "Error: jq is required but not installed. Please install it first."
    exit 1
fi

if ! command -v curl &> /dev/null; then
    echo "Error: curl is required but not installed. Please install it first."
    exit 1
fi

# Create download directory if it doesn't exist
mkdir -p "$DOWNLOAD_DIR"

# Function to get download URL
get_download_url() {
    local name="$1"
    local version="$2"
    local info_url="https://packages.maxon.net/content?id=$name&platform=macos&v=$version"
    
    local download_url=$(curl -s "$info_url" | jq -r '.[0].download_url // empty')
    if [ -z "$download_url" ]; then
        echo "Error: Could not get download URL"
        exit 1
    fi
    echo "$download_url"
}

# Function to get clean filename from URL
get_clean_filename() {
    local url="$1"
    local filename=$(echo "$url" | sed -e 's/.*\///' -e 's/?.*//')
    echo "$filename"
}

# Function to validate number input
validate_number() {
    local num=$1
    local max=$2
    if [[ ! "$num" =~ ^[0-9]+$ ]] || [ "$num" -lt 1 ] || [ "$num" -gt "$max" ]; then
        return 1
    fi
    return 0
}

# Function to process single app download
process_app_download() {
    local app_name=$1
    local apps_json=$2
    
    # Get versions for selected app
    echo -e "\nAvailable versions for $app_name:"
    readarray -t versions < <(echo "$apps_json" | jq -r --arg name "$app_name" '.[] | select(.fullName == $name or .name == $name) | .version' | sort -V)
    
    for i in "${!versions[@]}"; do
        echo "$((i+1)). ${versions[$i]}"
    done
    
    # Get version selection
    while true; do
        echo -e "\nSelect version number for $app_name: "
        read -r version_choice
        
        if validate_number "$version_choice" "${#versions[@]}"; then
            break
        fi
        echo "Invalid version selection. Please try again."
    done
    
    selected_version="${versions[$((version_choice-1))]}"
    
    # Get the app name (identifier) for the selected app
    app_id=$(echo "$apps_json" | jq -r --arg fullname "$app_name" '.[] | select(.fullName == $fullname or .name == $fullname) | .name' | head -n1)
    
    # Get download URL
    download_url=$(get_download_url "$app_id" "$selected_version")
    filename=$(get_clean_filename "$download_url")
    destination="$DOWNLOAD_DIR/$filename"
    
    echo -e "\nPreparing to download:"
    echo "App: $app_name"
    echo "Version: $selected_version"
    echo "Filename: $filename"
    echo "Destination: $destination"
    
    # Download the file with progress bar
    echo -e "\nDownloading $app_name..."
    curl -# -L -o "$destination" "$download_url"
    
    if [ $? -eq 0 ]; then
        echo -e "\nDownload of $app_name completed successfully!"
    else
        echo -e "\nDownload of $app_name failed!"
    fi
}

# Main execution flow
while true; do
    # Get and parse the list of available apps
    echo -e "\nFetching available apps..."
    apps_json=$(curl -s "$MAXON_API_URL")
    
    if [ -z "$apps_json" ]; then
        echo "Error: Failed to fetch apps list"
        exit 1
    fi
    
    # Create a unique list of apps with their names
    echo -e "\nAvailable apps:"
    readarray -t app_names < <(echo "$apps_json" | jq -r '.[] | "\(.fullName // .name)"' | sort -u)
    
    # Display the list of apps
    for i in "${!app_names[@]}"; do
        echo "$((i+1)). ${app_names[$i]}"
    done
    
    # Get user selection - now supporting multiple selections
    echo -e "\nSelect app number(s) separated by spaces (or 0 to exit): "
    read -r -a choices
    
    # Check if user wants to exit
    if [[ "${choices[0]}" == "0" ]]; then
        break
    fi
    
    # Validate all selections before proceeding
    valid_selections=true
    selected_indices=()
    
    for choice in "${choices[@]}"; do
        if ! validate_number "$choice" "${#app_names[@]}"; then
            echo "Invalid selection: $choice"
            valid_selections=false
            break
        fi
        selected_indices+=($((choice-1)))
    done
    
    if [ "$valid_selections" = false ]; then
        continue
    fi
    
    # Process each selected app
    for index in "${selected_indices[@]}"; do
        selected_app="${app_names[$index]}"
        process_app_download "$selected_app" "$apps_json"
    done
    
    echo -e "\nAll selected downloads completed!"
    
    echo -e "\nWould you like to download more apps? (y/n): "
    read -r continue_choice
    if [[ ! "$continue_choice" =~ ^[Yy] ]]; then
        break
    fi
done

echo "Script finished."
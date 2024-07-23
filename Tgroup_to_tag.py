from tenable.io import TenableIO

# Tenable.io API credentials
access_key = "YOUR_ACCESS_KEY"
secret_key = "YOUR_SECRET_KEY"

# Create a Tenable.io instance
tnio = TenableIO(access_key=access_key, secret_key=secret_key)

# Retrieve all scans
scans = tnio.scans.list()

# Iterate through scans
for scan in scans:
    scan_id = scan["id"]
    scan_name = scan["name"]

    # Retrieve scan details
    scan_details = tnio.scans.details(scan_id)

    # Extract target groups
    target_groups = scan_details["targets"]["groups"]

    # Iterate through target groups
    for target_group in target_groups:
        target_group_name = target_group["name"]

        # Set tag name to target group name
        tag_name = target_group_name

        # Update scan targets and tags
        scan_details["targets"]["groups"] = []
        scan_details["targets"]["assets"] = [target_group_name]
        scan_details["tags"] = [tag_name]

        # Update the scan
        tnio.scans.update(scan_id, scan_details)

        print(f"Scan '{scan_name}' targets updated successfully with tag '{tag_name}'.")

print("All scans updated successfully.")
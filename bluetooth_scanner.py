import subprocess


def get_devices():

    command = [
        "powershell",
        "-Command",
        "Get-PnpDevice -Class Bluetooth | Select-Object FriendlyName | ConvertTo-Csv -NoTypeInformation"
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    lines = result.stdout.strip().splitlines()

    devices = []

    ignore = [
        "Microsoft Bluetooth Enumerator",
        "Microsoft Bluetooth LE Enumerator",
        "Bluetooth Device (RFCOMM Protocol TDI)",
        "Intel(R) Wireless Bluetooth(R)"
    ]

    for line in lines[1:]:

        name = line.replace('"', "").strip()

        if not name:
            continue

        if name in ignore:
            continue

        upper = name.upper()

        if "JBL" in upper:
            icon = "🔊"

        elif "FENDA" in upper:
            icon = "🔊"

        elif "SPEAKER" in upper:
            icon = "🔊"

        elif "HEADPHONE" in upper:
            icon = "🎧"

        elif "EARBUD" in upper:
            icon = "🎧"

        elif "MOUSE" in upper:
            icon = "🖱️"

        elif "PHONE" in upper:
            icon = "📱"

        elif "LAPTOP" in upper:
            icon = "💻"

        else:
            icon = "📡"

        devices.append(
            {
                "Icon": icon,
                "Name": name
            }
        )

    return devices
ALLOWED_CATEGORIES = {

    "Network": [
        "VPN",
        "WiFi",
        "LAN",
        "DNS",
        "Connectivity"
    ],

    "Hardware": [
        "Laptop",
        "Desktop",
        "Printer",
        "Monitor",
        "Peripheral"
    ],

    "Software": [
        "Installation",
        "Application Error",
        "Update",
        "Performance"
    ],

    "Email & Collaboration": [
        "Outlook",
        "Teams",
        "Email Delivery",
        "Calendar"
    ],

    "Access & Authentication": [
        "Password Reset",
        "Account Lockout",
        "Permissions",
        "MFA"
    ],

    "Security": [
        "Phishing",
        "Malware",
        "Unauthorized Access",
        "Security Alert"
    ],

    "Infrastructure": [
        "Server",
        "Storage",
        "Backup",
        "Virtual Machine"
    ],

    "Database": [
        "Connection Failure",
        "Query Issue",
        "Performance",
        "Data Access"
    ],

    "Cloud Services": [
        "Azure",
        "AWS",
        "Resource Access",
        "Deployment"
    ],

    "Service Request": [
        "New Account",
        "Software Request",
        "Hardware Request",
        "Access Request"
    ]
}


ALLOWED_PRIORITIES = [
    "High",
    "Medium",
    "Low"
]


def validate_classification(result):

    category = result.get("category", "").strip()
    subcategory = result.get("subcategory", "").strip()
    priority = result.get("priority", "").strip()

    if category not in ALLOWED_CATEGORIES:
        return False

    if subcategory not in ALLOWED_CATEGORIES[category]:
        return False

    if priority not in ALLOWED_PRIORITIES:
        return False

    return True
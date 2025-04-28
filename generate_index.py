import os
import json
import apkutils2

APK_FOLDER = 'software/apks'
OUTPUT_FILE = os.path.join(APK_FOLDER, 'apks_index.json')

apk_list = []

for file_name in os.listdir(APK_FOLDER):
    if file_name.endswith('.apk'):
        apk_path = os.path.join(APK_FOLDER, file_name)
        
        apk = apkutils2.APK(apk_path)  # <-- corrected
        
        manifest = apk.get_manifest()

        package_name = manifest['@package']
        version_code = int(manifest['@android:versionCode'])
        version_name = manifest['@android:versionName']

        apk_entry = {
            "fileName": file_name,
            "packageName": package_name,
            "versionCode": version_code,
            "versionName": version_name
        }
        apk_list.append(apk_entry)

with open(OUTPUT_FILE, 'w') as f:
    json.dump(apk_list, f, indent=4)

print(f"Generated {OUTPUT_FILE} with {len(apk_list)} entries.")
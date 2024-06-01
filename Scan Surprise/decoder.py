from pyzbar.pyzbar import decode
from PIL import Image
import os

def extract_qr_code_info(image_path):
    # Load the image
    image = Image.open(image_path)
    
    # Decode the QR code
    decoded_objects = decode(image)
    
    if not decoded_objects:
        return None
    
    # Extract the data from the decoded objects
    qr_data = []
    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        qr_data.append(data)
    
    return qr_data

# Example usage:
relative_path = r"home/ctf-player/drop-in/flag.png"

current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, relative_path)

qr_data = extract_qr_code_info(image_path)
if qr_data:
    print("QR Code Data:")
    for data in qr_data:
        print(data)
else:
    print("No QR code found in the image.")

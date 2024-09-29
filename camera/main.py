import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.clock import Clock

from pyzbar.pyzbar import decode
from PIL import Image as PilImage
import io

# Main layout class for the app
class QRPaymentApp(App):
    def build(self):
        # Use BoxLayout for vertical orientation
        self.layout = BoxLayout(orientation='vertical')
        
        # Create camera widget to capture QR code
        self.camera = Camera(play=True, resolution=(640, 480), size_hint=(1, 0.8))
        self.layout.add_widget(self.camera)
        
        # Label to show the payment status
        self.payment_status = Label(text="Scan the QR Code to Pay", size_hint=(1, 0.1))
        self.layout.add_widget(self.payment_status)
        
        # Add button to manually trigger scanning (simulate the scan)
        scan_button = Button(text="Simulate QR Scan", size_hint=(1, 0.1))
        scan_button.bind(on_press=self.simulate_scan)
        self.layout.add_widget(scan_button)
        
        # Schedule function to continuously check QR code from the camera feed
        Clock.schedule_interval(self.scan_qr_code, 1.0 / 30.0)  # Check every frame
        
        return self.layout
    
    # This function simulates QR code scanning by showing a success message
    def simulate_scan(self, instance):
        self.payment_status.text = "Payment Successful"

    # Function to decode the QR code from the camera
    def scan_qr_code(self, dt):
        # Get the image from the camera
        camera_texture = self.camera.texture
        if camera_texture:
            buf = camera_texture.pixels
            size = camera_texture.size
            pil_image = PilImage.frombytes(mode='RGBA', size=size, data=buf)
            
            # Decode the QR code
            decoded_objects = decode(pil_image)
            if decoded_objects:
                for obj in decoded_objects:
                    # Check if the QR code is scanned, then show the payment status
                    qr_data = obj.data.decode("utf-8")
                    print("QR Code Scanned: ", qr_data)  # To verify what's in the QR code
                    self.payment_status.text = "Payment Successful"
                    # Optionally, you can add more conditions or process based on `qr_data`
                    break

# Run the Kivy app
if __name__ == '__main__':
    QRPaymentApp().run()

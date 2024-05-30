import random
import string
import time
import cv2
import simpleaudio as sa


class Camera:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.camera = cv2.VideoCapture(camera_index)
        if not self.camera.isOpened():
            raise ValueError(f"Camera with index {camera_index} could not be opened.")
        print(f"Camera {camera_index} opened successfully.")

        # Load the audio file
        self.audio_file = sa.WaveObject.from_wave_file('utils/pic-time.wav')

    def take_picture(self):
        # Play the audio cue
        play_obj = self.audio_file.play()
        time.sleep(2.5)
        # Capture the picture
        ret, frame = self.camera.read()


        if not ret:
            raise RuntimeError("Failed to take picture.")
        return frame

    def save_picture(self, frame, filename):
        cv2.imwrite(filename, frame)
        print(f"Picture saved as {filename}")

    def release(self):
        self.camera.release()
        print(f"Camera {self.camera_index} released.")

    def generate_image_name(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')

        # Construct the image name
        image_name = f'images/img-{current_time}.jpg'

        return image_name

# Usage example
if __name__ == "__main__":
    cam = Camera()
    try:
        frame = cam.take_picture()
        cam.save_picture(frame, cam.generate_image_name())
    finally:
        cam.release()

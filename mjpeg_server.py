from picamera import PiCamera
from http.server import BaseHTTPRequestHandler, HTTPServer
import time


class MJPEGHandler(BaseHTTPRequestHandler):
    def do_GET (self):
        if self.path == '/stream.mjpg':
            self.send_response(200)  #--- Sending Server Response
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=frame')
            self.end_headers()
            with PiCamera() as camera:
                camera.resolution = (640, 480)
                camera.framerate = 30
                camera.start_recording(self.wfile, format='mjpeg')
                try:
                    while True:
                        camera.wait_recording(1)     #--- Stay recording
                except Exception:
                    camera.stop_recording()
                    raise
        else:
            self.send_error(404)    #--- Can't connect


if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), MJPEGHandler)
    print("MJPEG server running on http://0.0.0.0:8000/stream.mjpg")
    server.serve_forever()

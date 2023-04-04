import json

from flask import Flask, request
from flask import Response
from flask_api import status

from embeddings.Embedding import Embedding
from logger.logger import get_logger
from storage.Device import Device

logger = get_logger(__name__)


def create_app():
    app = Flask(__name__)
    embeddings = Embedding()

    @app.route('/scan')
    def scan():
        return embeddings.scan_devices()

    @app.route('/')
    def get_devices():
        devices = embeddings.get_devices()
        if devices.count == 0:
            return status.HTTP_404_NOT_FOUND
        return json.dumps([json.loads(str(d)) for d in devices])

    @app.route('/devices/<mac>', methods=['GET'])
    def get_device(mac: str):
        device = embeddings.get_device(mac)
        if device is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return json.loads(str(device))

    @app.route('/devices', methods=['POST'])
    def add_device():
        args = request.args
        mac = args.get('mac')
        device = embeddings.add_device(mac)
        if not isinstance(device, Device):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return json.loads(str(device))

    return app

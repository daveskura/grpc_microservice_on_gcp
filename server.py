"""
  Dave Skura
  
"""
import logging
import os
import grpc
import speaker_pb2
import speaker_pb2_grpc
from concurrent import futures
from typing import Text

_PORT = os.environ["PORT"]

class Speaker(speaker_pb2_grpc.SpeakerServicer):

	def Speak(self,request: speaker_pb2.InputData,context: grpc.ServicerContext) -> None:
		logging.info("Received request: %s", request)
		result = 'hello ' + request.data
		return speaker_pb2.OutputData(data=result)


def _serve(port: Text):
	bind_address = f"[::]:{port}"
	server = grpc.server(futures.ThreadPoolExecutor())
	speaker_pb2_grpc.add_SpeakerServicer_to_server(Speaker(), server)
	server.add_insecure_port(bind_address)
	server.start()
	logging.info("Listening on %s.", bind_address)
	server.wait_for_termination()


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)
	logging.info(" Starting ") # 
	_serve(_PORT)
import logging
import argparse
import functools

from typing import Text

import grpc

import speaker_pb2
import speaker_pb2_grpc

def run_local():
	with grpc.insecure_channel('localhost:5150') as channel:
			stub = speaker_pb2_grpc.SpeakerStub(channel)
			response = stub.Speak(speaker_pb2.InputData(data='this thing '))
			print(str(response.data))

def run_against_gcp():
	server_address='speaker-ioxqlcawxa-nn.a.run.app'
	with grpc.secure_channel(server_address,grpc.ssl_channel_credentials()) as channel:
			stub = speaker_pb2_grpc.SpeakerStub(channel)
			response = stub.Speak(speaker_pb2.InputData(data='this thing '))
			print(str(response.data))

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)
	logging.info(" Starting ") # 
	run_against_gcp()




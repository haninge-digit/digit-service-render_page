# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import render_page_pb2
import render_page_pb2_grpc

import weasyprint

class RenderPage(render_page_pb2_grpc.RenderPageServicer):

    def RenderPDF(self, request, context):
        pdf = weasyprint.HTML(string=request.html).write_pdf()
        return render_page_pb2.RenderReply(pdf=pdf)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    render_page_pb2_grpc.add_RenderPageServicer_to_server(RenderPage(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

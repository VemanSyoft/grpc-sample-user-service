import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_project.settings")

import django
django.setup()


from concurrent import futures
import grpc_config_pb2_grpc
import grpc_config_pb2
import grpc
from user_app.models import User


class UserServicer(grpc_config_pb2_grpc.UserServicer):
    def UserInfo(self, request, context):
        print("User service request called:")
        email = request.email
        print("email --->",email)
        user_service_reply = grpc_config_pb2.UserInfoReply()
        user_info = User.objects.get(email=email)
        print("user_info --->",user_info)
        user_service_reply.id = str(user_info.id)
        return user_service_reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_config_pb2_grpc.add_UserServicer_to_server(UserServicer(),server)
    server.add_insecure_port("localhost:1694")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

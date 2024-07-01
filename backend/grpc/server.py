import grpc
from concurrent import futures
import predict_pb2
import predict_pb2_grpc
import joblib

class CurrencyPredictionService(predict_pb2_grpc.CurrencyPredictionServiceServicer):
    def __init__(self):
        self.model = joblib.load('models/currency_prediction_model.pkl')

    def Predict(self, request, context):
        features = [[request.feature1, request.feature2, request.feature3, request.feature4, request.feature5, request.feature6, request.feature7]]
        prediction = self.model.predict(features)
        return predict_pb2.PredictResponse(predicted_value=prediction[0])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    predict_pb2_grpc.add_CurrencyPredictionServiceServicer_to_server(CurrencyPredictionService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

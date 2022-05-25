from signal import raise_signal
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from contestants.serializers import RegPurchaseSerializer,VerifyTransSerializer
from contestants.models import RegistrationPurchase
from paystackapi.paystack import Paystack
from django.conf import settings

class RegPurchView(GenericAPIView):
    serializer_class = RegPurchaseSerializer
    def post(self,request):
        serializer = RegPurchaseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyTransaction(GenericAPIView):
    serializer_class = VerifyTransSerializer

    def get_object(self,ref):
        try:
           return RegistrationPurchase.objects.get(ref=ref)
        except RegistrationPurchase.DoesNotExist:
            raise Http404

    def verifier(self,ref):
        try:
            trans = RegistrationPurchase.objects.get(ref=ref)
            trans.verified = True
            trans.save()
            return "Transaction was successfully Verified"
        except RegistrationPurchase.DoesNotExist:
            raise Http404

    def get(self,request, ref):
        amount = 500000
        serialiazer = self.serializer_class(self.get_object(ref))
        ref_no = serialiazer.data["ref"]
        paystack = Paystack(secret_key=settings.paystack_secret_key)
        response = paystack.transaction.verify(ref_no)
        reference_num = response['data']['reference']

        if response["status"]==True and response["message"]=='Verification successful' and response['data']['status'] == 'success' and response['data']['amount'] == amount:
            message = self.verifier(reference_num)
            return Response({"message":message},status=status.HTTP_200_OK)
        return Response({"message":"Invalid Transaction, transaction was not verified"}, status=status.HTTP_400_BAD_REQUEST)


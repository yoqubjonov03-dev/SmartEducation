from django.shortcuts import render
from openid.extensions.draft.pape5 import Response
from rest_framework.views import APIView, status
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Payments
from .serializers import PaymentsSerializer
from .permissions import IsAdminIsStaff

from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from users_app.models import Enrollments

import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY


class CreatePaymentIntent(APIView):


    def post(self, request, *args, **kwargs):
        payment_method = 'Card'
        stripe_token = request.data.get('stripe_token')
        enrollment_id = request.data.get('enrollment_id')

        try:
            enrollment = Enrollments.objects.get(id=enrollment_id)
        except Enrollments.DoesNotExist:
            return Response({'error': 'Enrolment not found'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            total_amount = enrollment.group_id.course_id.price
            charge = stripe.Charge.create(
                amount=int(total_amount),
                currency="usd",
                source=stripe_token,
            )
            Payments.objects.create(
                enrollment_id=enrollment,
                stripe_charge_id=charge['id'],
                amount=total_amount,
                payment_method=payment_method,

            )
            enrollment.is_paid = True
            enrollment.save()


            return Response({"status": "Payment successful"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [IsAdminIsStaff]

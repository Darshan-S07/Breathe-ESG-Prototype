import csv

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.generics import UpdateAPIView
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *
from .services import *


class UploadCSVView(APIView):

    def post(self, request):

        file = request.FILES['file']

        source_type = request.data.get('source_type')

        org_id = request.data.get('organization_id')

        organization = get_object_or_404(
            Organization,
            id=org_id
        )

        data_source = DataSource.objects.create(
            organization=organization,
            source_type=source_type,
            ingestion_method='FILE'
        )

        decoded_file = file.read().decode('utf-8').splitlines()

        reader = csv.DictReader(decoded_file)

        created_count = 0

        for row in reader:

            try:

                raw_record = RawRecord.objects.create(
                    data_source=data_source,
                    raw_payload=row
                )

                activity_type = row.get("activity_type").lower()

                quantity = float(row.get("quantity"))

                unit = row.get("unit")

                normalized_quantity, normalized_unit = normalize_unit(
                    quantity,
                    unit
                )

                scope = classify_scope(activity_type)

                factor, emissions = calculate_emissions(
                    activity_type,
                    normalized_quantity
                )

                suspicious = is_suspicious(
                    activity_type,
                    normalized_quantity
                )

                NormalizedRecord.objects.create(
                    raw_record=raw_record,
                    organization=organization,
                    category=scope,
                    activity_type=activity_type,
                    quantity=quantity,
                    unit=unit,
                    normalized_quantity=normalized_quantity,
                    normalized_unit=normalized_unit,
                    emission_factor=factor,
                    emissions_value=emissions,
                    suspicious_flag=suspicious
                )

                created_count += 1

            
            except Exception as e:

                print("ERROR:", e)
                print("ROW:", row)

                RawRecord.objects.create(
                    data_source=data_source,
                    raw_payload=row,
                    status='FAILED',
                    error_message=str(e)
                )

        return Response({
            "message": "Upload successful",
            "records_created": created_count
        })


class NormalizedRecordsView(ListAPIView):

    queryset = NormalizedRecord.objects.all()

    serializer_class = NormalizedRecordSerializer


class ApproveRecordView(UpdateAPIView):

    queryset = NormalizedRecord.objects.all()

    serializer_class = NormalizedRecordSerializer

    def patch(self, request, *args, **kwargs):

        instance = self.get_object()

        old_status = instance.status

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)

        updated_instance = serializer.save()

        AuditLog.objects.create(
            record=updated_instance,
            action="STATUS_CHANGED",
            old_value={"status": old_status},
            new_value={"status": updated_instance.status}
        )

        return Response(serializer.data)
class FailedRecordsView(ListAPIView):

    queryset = RawRecord.objects.filter(status='FAILED')

    serializer_class = RawRecordSerializer
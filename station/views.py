from .models import DataRecord, DataSource, AIQuery
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .tasks import process_file
from .services import AIService
import pandas as pd

class UploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response({"error": "No file provided"}, status=400)

        if file.size > 5 * 1024 * 1024:
            return Response({"error": "File too large"}, status=400)

        source = None

        try:
            source = DataSource.objects.create(
                name=file.name,
                file=file,
                owner=request.user,
                status="processing"
            )

            process_file.delay(source.id)

            return Response({
                "message": "File uploaded successfully, processing started",
                "source_id": source.id
            })

        except Exception as e:
            if source:
                source.status = "error"
                source.save()

            return Response({
                "error": str(e)
            }, status=500)
            

class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, source_id):
        question = request.data.get("question")

        if not question:
            return Response({"error": "Question is required"}, status=400)

        try:
            source = DataSource.objects.get(id=source_id, owner=request.user)
            record = source.records.order_by('-created_at').first()

            if not record:
                return Response({"error": "No data found"}, status=404)

            data = record.data

            analysis_obj = source.analyses.last()
            analysis_text = analysis_obj.result.get("analysis") if analysis_obj else None

            history = source.queries.order_by('-created_at')[:5][::-1]

            ai = AIService()
            answer = ai.chat(
                data=data,
                question=question,
                analysis=analysis_text,
                history=history
            )

            AIQuery.objects.create(
                source=source,
                question=question,
                answer=answer
            )

            return Response({
                "question": question,
                "answer": answer
            })

        except DataSource.DoesNotExist:
            return Response({"error": "DataSource not found"}, status=404)

        except Exception as e:
            return Response({"error": str(e)}, status=500)
from celery import shared_task
import pandas as pd
from .models import DataSource, DataRecord, AnalysisResult
from .services import AIService
import logging
logger = logging.getLogger(__name__)

@shared_task
def process_file(source_id):
    source = DataSource.objects.get(id=source_id)
    try:
        logger.info(f"Starting processing for Source ID: {source_id}")
        
        file = source.file
        file.seek(0)

        # تحسين: قراءة النص مباشرة إذا لم يكن CSV معقداً
        content = file.read().decode('utf-8')
        logger.info(f"File content read: {content[:50]}...")

        # إذا كنت تصر على Pandas لبيانات الشحن:
        # df = pd.read_csv(file) 
        # data = {"rows": df.to_dict(orient="records")}
        
        data = {"content": content} # تبسيط للتيست

        # AI Analysis
        ai = AIService()
        logger.info("Calling AIService (Ollama)...")
        result = ai.analyze(data)
        
        logger.info(f"AI Result received: {result}")

        AnalysisResult.objects.create(
            source=source,
            result={"analysis": result}
        )

        source.status = "ready"
        source.save()
        return f"Success: Analysis for {source_id} completed"

    except Exception as e:
        logger.error(f"Error in process_file: {str(e)}")
        source.status = "error"
        source.save()
        return f"Failed: {str(e)}"
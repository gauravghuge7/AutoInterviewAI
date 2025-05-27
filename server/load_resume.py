# load_resume.py
from utils.resume_processing import parse_resume
from utils.qdrant_utils import init_qdrant_collection, upload_resume_to_qdrant

resume_path = "public\Devashish_Resume_.pdf"

init_qdrant_collection()
text = parse_resume(resume_path)
metadata = {"name": "Devashish", "email": "mdevashish51@gmail.com"}
upload_resume_to_qdrant(text, metadata)
print("✅ Resume uploaded to Qdrant.")

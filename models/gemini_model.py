import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

# --- Validate API key early for a clear error message ---
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise EnvironmentError(
        "Missing GOOGLE_API_KEY in your .env file. "
    )

client = genai.Client(api_key=api_key)


def analyze_syllabus(file_path: str) -> str:

    # --- Step 1: Upload the file ---
    print(f"Uploading '{file_path}' to Google File API...")
    syllabus_file = client.files.upload(file=file_path)
    print(f"Upload complete. Remote file name: {syllabus_file.name}")

    # --- Step 2: Wait for processing (FIX: was 3-space indent before) ---
    print("Waiting for file to process", end="", flush=True)
    while syllabus_file.state.name == "PROCESSING":
        print(".", end="", flush=True)
        time.sleep(2)
        syllabus_file = client.files.get(name=syllabus_file.name)
    print()  # newline after the dots

    if syllabus_file.state.name == "FAILED":
        raise ValueError(
            f"Google File API failed to process '{file_path}'. "
            "Make sure it's a valid, non-corrupted PDF."
        )

    # --- Step 3: Analyze with Gemini ---
    print("Sending to Gemini for analysis...")

    prompt = """You are Bengal Syllabus GPT, an assistant that reads course syllabi.

From the uploaded syllabus, extract and clearly format the following:

1. IMPORTANT DATES & DEADLINES
   - List every exam, quiz, project, assignment, and deadline you can find
   - Format each as: [Date] — [Event/Assignment Name]

3. GRADING SCALE
   - List all grade categories and their weights (e.g. Exams 40%, HW 20%)

4. 📌 OTHER KEY POLICIES
   - late work, or any other notable rules

If any section is not found in the syllabus, write "Not found" for that section.
Be concise and structured."""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=[syllabus_file, prompt]
        )
        result = response.text

    except Exception as e:
        raise RuntimeError(f"Gemini API call failed: {e}") from e

    finally:
        # --- Step 4: Always clean up the remote file ---
        try:
            client.files.delete(name=syllabus_file.name)
            print(f"Remote file '{syllabus_file.name}' deleted from Google servers.")
        except Exception as cleanup_err:
            print(f"Warning: Could not delete remote file '{syllabus_file.name}': {cleanup_err}")

    return result
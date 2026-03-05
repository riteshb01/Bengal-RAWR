import os
from models.gemini_model import analyze_syllabus


def main():
    # Path to your test syllabus — put any PDF in the Files/ folder
    target_file = os.path.join("Files", "test.pdf")

    print("=" * 50)
    print("   Bengal Rawr — Syllabus Analyzer")
    print("=" * 50)

    # --- Check the file exists before doing anything ---
    if not os.path.exists(target_file):
        print(f"\n❌ Error: No file found at '{target_file}'")
        print("Fix: Make sure a 'Files' folder exists in your project root")
        print("     and place your syllabus PDF inside it named 'test.pdf'.")
        return

    print(f"\n✅ File found: {target_file}")
    file_size_kb = os.path.getsize(target_file) / 1024
    print(f"   Size: {file_size_kb:.1f} KB\n")

    # --- Run the analysis ---
    try:
        result = analyze_syllabus(target_file)

        print("\n" + "=" * 50)
        print("   Analysis Result")
        print("=" * 50)
        print(result)
        print("=" * 50)

    except EnvironmentError as e:
        # Missing API key — user needs to fix .env
        print(f"\n🔑 Configuration Error:\n   {e}")

    except ValueError as e:
        # File processing failed on Google's end
        print(f"\n📄 File Error:\n   {e}")

    except RuntimeError as e:
        # Gemini API call failed
        print(f"\n🤖 Gemini Error:\n   {e}")

    except Exception as e:
        # Catch-all for unexpected issues
        print(f"\n💥 Unexpected error: {e}")
        raise  # Re-raise so you see the full traceback during dev


if __name__ == "__main__":
    main()
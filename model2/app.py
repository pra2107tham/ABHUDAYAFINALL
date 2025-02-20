import os
import logging
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from data_initialization import initialize_data, load_vector_store, get_conversational_chain

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Logging
logging.basicConfig(filename="logs/app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)

# API Endpoint: Process and Store Text Files
@app.route("/process_texts", methods=["POST"])
def process_texts():
    try:
        if "files" not in request.files:
            return jsonify({"error": "No files uploaded"}), 400

        files = request.files.getlist("files")
        initialize_data(files)
        return jsonify({"message": "Text file processing completed successfully."})
    except Exception as e:
        logging.error("Error processing text files: %s", str(e))
        return jsonify({"error": str(e)}), 500

# API Endpoint: Query the vector store
@app.route("/query", methods=["POST"])
def query_text():
    try:
        question = request.form.get("question")
        if not question:
            return jsonify({"error": "No question provided"}), 400

        if not os.path.exists("faiss_index"):
            return jsonify({"error": "No processed text files found. Please upload and process texts first."}), 400

        vector_store = load_vector_store()
        qa_chain = get_conversational_chain()
        docs = vector_store.similarity_search(question)
        response = qa_chain({"input_documents": docs, "question": question}, return_only_outputs=True)

        return jsonify({"response": response["output_text"]})
    except Exception as e:
        logging.error("Error in querying: %s", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

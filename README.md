# TACH
Here I have used a local LLM to create a RAG based AI teaching assistance which is trained on high school physics lectures. To Run the AI assistance do install ollama to locally install the model llama3.2 you can change the model for better response.

## Here are the steps to create your own RAG based AI teaching assistance:

### 1. Prepare Videos
Install the code files, add your videos to the vid folder, and then run process_video.py to make the aud directory. (Make sure the videos have titles like Lecture{no}. You can modify the process_video.py and read_chunks.py files to surpass this requirement)

### 2. Process Audio and Create Embeddings
Now run the file stt.py. Make sure whisper is installed with `pip install whisper`. Then run the file read_chunks.py - this is a one-time process to make the embeddings. Install bge-m3 before running with the help of ollama.

### 3. Run the AI Assistant
Your RAG based AI assistance (TACH) is ready! You can ask questions through the terminal by running process_incoming.py and see the answers in response.txt.

## Note
This is an experimental demo. The use of local models and whisper increases the processing time. There will be further improvements to this model over time, so be patient and happy coding 🙂.

 📝 AI Text Summarizer  

This project is an **end-to-end AI text summarizer** that fine-tunes a **pretrained PEGASUS model (`google/pegasus-cnn_dailymail`)** on the **SAMSum** conversation dataset. The project follows a modular structure, allowing easy configuration and extension. It deploys a **FastAPI service**, enabling users to interact with the model via a REST API.  

## 🚀 Project Workflow  

This project follows a structured workflow:  

1. **Update configuration files** (`config.yaml`, `params.yaml`)  
2. **Define entity classes**  
3. **Configure the manager** (`src/config`)  
4. **Implement modular components**  
5. **Update the pipeline**  
6. **Train the model** (`main.py`)  
7. **Deploy the FastAPI service** (`app.py`)  

## 📌 Model Details  

- **Pretrained Model**: `google/pegasus-cnn_dailymail` from Hugging Face  
- **Fine-tuned On**: **Test set** of the SAMSum dataset (due to limited resources)  
- **Training Platform**: Google Colab (Free T4 GPU)  
- **Epochs**: **1 epoch** (limited by Colab’s free tier)  
- **Validation**: Performed on the **validation set**  
- **Evaluation**: Runs on the **test set** and outputs **ROUGE scores**  

This project is primarily focused on building an **end-to-end ML pipeline**, rather than achieving state-of-the-art summarization accuracy.  

## 🛠️ Tech Stack  

- **Framework**: PyTorch  
- **API Deployment**: FastAPI  
- **Package Management**: Conda + `requirements.txt`  

## 🏗️ Installation  

Before running the project, set up a virtual environment and install dependencies:  

```bash
# Create a virtual environment
conda create -p venv python==3.10 -y  

# Activate the environment
conda activate ./venv  

# Install dependencies
pip install -r requirements.txt
```

## 🔥 How to Use

### 1️⃣ Configure Training Parameters
Before training the model, you can modify training settings in ```params.yaml```:
```yaml
TrainingArguments:
    num_train_epochs: 1
    warmup_steps: 10
    per_device_train_batch_size: 1
    weight_decay: 0.01
    logging_steps: 5
    eval_strategy: "steps"
    eval_steps: 50
    save_steps: 1000000
    gradient_accumulation_steps: 2
    fp16: False
    report_to: none
```
Adjust these values based on your compute resources and training requirements.

### 2️⃣ Train and Evaluate the Model
Run the training script:
```bash
python main.py
```
This will:
✅ Fine-tune the model
✅ Evaluate it on the test set
✅ Save **ROUGE score metrics** in a file (```metrics.csv``` in ```artifacts/model_evaluation``` directory)

### 3️⃣ Start the API Server
```bash
python app.py
```
The FastAPI server will start on localhost:8080.

### 4️⃣ Access the API

 - Open your browser and go to: http://localhost:8080/docs
 - You will see the FastAPI interactive Swagger UI.
 - You can now use the following routes:

🔹 **Train the Model**
```http
GET /train
```
 - This triggers ```main.py``` to train and evaluate the model.
 - ROUGE scores will be saved in a **metrics file**.
 - Response: ```"Training Successful!"``` (or error message if something goes wrong)

🔹 **Predict a Summary**
```http
POST /predict
```
 - **Input:** A JSON object with a ```text``` field containing the input conversation.
 - **Output:** The model-generated summary.

Example request using ```curl```:
```bash
curl -X 'POST' \
  'http://localhost:8080/predict' \
  -H 'Content-Type: application/json' \
  -d '{"text": "Hey, how are you? I need help with my project."}'
```

### 🏁 **Example Output**

**Input:**
*"Hey, how are you? I need help with my project."*

**Output:**
*"Person needs help with their project."*

## **Future Improvements**
 - Train on a larger dataset with more compute resources.
 - Implement a better evaluation metric for summarization quality.
 - Enhance the FastAPI interface for improved usability.
 - Support batch predictions for processing multiple conversations at once.
 








# ai_engine.py
import os
import google.generativeai as genai
from gtts import gTTS
import base64
import json
from dotenv import load_dotenv
import re
import streamlit as st

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('models/gemini-3.1-flash-lite-preview')

def clean_json_string(text):
    # Loại bỏ các ký tự Markdown nếu có
    text = re.sub(r'```json', '', text)
    text = re.sub(r'```', '', text)
    # Tìm đoạn JSON đầu tiên bắt đầu bằng { và kết thúc bằng }
    match = re.search(r'(\{.*\})|(\[.*\])', text, re.DOTALL)
    if match:
        return match.group(0)
    return text

# ai_engine.py

def get_grammar_practice(hsk_level, grammar_title):
    prompt = f"""Bạn là giáo viên tiếng Trung. Tạo bài tập 'Sắp xếp câu' cho ngữ pháp '{grammar_title}' trình độ HSK{hsk_level}.
    
    Yêu cầu:
    1. Tạo đúng 3 câu tiếng Trung HSK2.0 chuẩn, đúng thứ tự từ trong ngữ pháp và chuẩn ngữ pháp tiếng Trung 100%.
    2. Cung cấp: cụm từ xáo trộn(đầy đủ 100% từ trong đáp án), câu hoàn chỉnh, phiên âm Pinyin, và nghĩa tiếng Việt.
    3. Đừng dùng từ giống dữ liệu cũ
    4. Tạo câu hỏi làm sao cho phần dịch nghe phải thực tế, đọc không ngượng tiếng Việt
    
    ĐỊNH DẠNG JSON MẪU:
    [
      {{
        "shuffled_words": ["老师", "是", "我", "不"],
        "correct_answer": "我不是老师",
        "pinyin": "Wǒ bù shì lǎo shī",
        "translation": "Tôi không phải là giáo viên"
      }}
    ]
    CHỈ TRẢ VỀ JSON."""
    
    try:
        response = model.generate_content(prompt)
        cleaned_json = clean_json_string(response.text.strip())
        return json.loads(cleaned_json)
    except:
        return []
    
def call_gemini_part(prompt_part):
    try:
        response = model.generate_content(prompt_part)
        cleaned = clean_json_string(response.text.strip())
        data = json.loads(cleaned)
        return data if isinstance(data, list) else [data]
    except Exception as e:
        print(f"Lỗi khi tải một phần đề thi: {e}")
        return []

def generate_full_exam(level, difficulty):
    full_exam = {"listening": [], "reading": [], "writing": []}
    total_batches = 11 
    current_batch = 0
    progress_bar = st.progress(0, text="Bắt đầu khởi tạo AI...")

    def update_progress(task_name):
        nonlocal current_batch
        current_batch += 1
        percent = min(current_batch / total_batches, 1.0)
        progress_bar.progress(percent, text=f"Đang soạn đề: {task_name} (Tiến độ: {current_batch}/{total_batches})")

    # --- PHẦN 1: ĐIỀN TỪ CÂU ĐƠN (5 CÂU) ---
    p_read_1 = f"""Tạo ĐÚNG 5 CÂU Đọc HSK {level}2.0 - Điền từ câu đơn. 
    Yêu cầu JSON: [{{
        "type": "fill_blank",
        "words": ["A","B","C","D","E","F"],
        "question": "Tôi muốn ___ cơm.",
        "answer": "ăn",
        "full_sentence": "Tôi muốn **ăn** cơm.",
        "pinyin": "Wǒ xiǎng chī fàn.",
        "translation": "Tôi muốn ăn cơm.",
        "explanation_vn": "Từ 'ăn' (chī) là động từ phù hợp với ngữ cảnh dùng bữa."
    }}]"""
    full_exam["reading"].extend(call_gemini_part(p_read_1))
    update_progress("Đọc - Điền từ câu đơn")

    # --- PHẦN 2: ĐIỀN TỪ HỘI THOẠI (5 CÂU) ---
    p_read_2 = f"""Tạo ĐÚNG 5 CÂU Đọc HSK {level}2.0 - Điền từ hội thoại A-B. 
    Yêu cầu JSON: [{{
        "type": "fill_blank",
        "words": ["A","B","C","D","E","F"],
        "question": "A: Bạn khỏe không? \\n B: Tôi ___ khỏe.",
        "answer": "rất",
        "full_sentence": "A: Bạn khỏe không? \\n B: Tôi **rất** khỏe.",
        "pinyin": "Wǒ hěn hǎo.",
        "translation": "Tôi rất khỏe.",
        "explanation_vn": "Phó từ 'rất' bổ nghĩa cho tính từ 'khỏe'."
    }}]"""
    full_exam["reading"].extend(call_gemini_part(p_read_2))
    update_progress("Đọc - Điền từ hội thoại")

    # --- PHẦN 3: SẮP XẾP THỨ TỰ A-B-C (10 CÂU) ---
    for i in range(2):
        p_read_3 = f"""Tạo ĐÚNG 5 CÂU sắp xếp A, B, C (HSK {level}2.0). 
        Yêu cầu JSON: [{{
            "type": "order",
            "options": ["A. ...", "B. ...", "C. ..."],
            "answer": "BCA",
            "pinyin": "Phiên âm của cả đoạn sau khi sắp xếp",
            "translation": "Nghĩa của cả đoạn",
            "explanation_vn": "Giải thích logic liên kết giữa các câu."
        }}]"""
        full_exam["reading"].extend(call_gemini_part(p_read_3))
        update_progress(f"Đọc - Sắp xếp đoạn văn {i+1}")

    # --- PHẦN 4: TRẮC NGHIỆM ĐOẠN VĂN (20 CÂU) ---
    for i in range(4):
        p_read_4 = f"""Tạo ĐÚNG 5 CÂU trắc nghiệm trích đoạn HSK {level}2.0. 
        Yêu cầu JSON: [{{
            "type": "choice",
            "passage": "...",
            "question": "★ ...",
            "options": ["A...","B...","C...","D..."],
            "answer": "A",
            "pinyin": "Phiên âm đoạn văn",
            "translation": "Dịch đoạn văn và câu hỏi",
            "explanation_vn": "Tại sao đáp án đó đúng dựa trên văn bản."
        }}]"""
        full_exam["reading"].extend(call_gemini_part(p_read_4))
        update_progress(f"Đọc - Trắc nghiệm {i+1}")

    # --- PHẦN 5: VIẾT - SẮP XẾP TỪ (15 CÂU) ---
    for i in range(3):
        p_write = f"""Tạo ĐÚNG 5 CÂU Viết HSK {level} - Sắp xếp từ2.0. 
        Ví dụ: (有) (了) (800 年的) -> 800 年的有了... 
        Yêu cầu JSON: [{{
            "shuffled_words": ["(词语1)", "(词语2)"],
            "answer": "Câu hoàn chỉnh",
            "pinyin": "Phiên âm",
            "translation": "Dịch nghĩa",
            "explanation_vn": "Giải thích cấu trúc ngữ pháp (Vd: S + V + O)."
        }}]"""
        full_exam["writing"].extend(call_gemini_part(p_write))
        update_progress(f"Viết - Sắp xếp câu {i+1}")

    progress_bar.empty() 
    return full_exam
  
def ai_give_feedback(level, score, max_score, wrong_answers):
    # Nếu làm đúng hết
    if not wrong_answers:
        return "Tuyệt vời! Bạn đã trả lời đúng tất cả các câu hỏi. Kiến thức của bạn rất vững chắc."
        
    wrong_context = "\n".join([
        f"- Phần {w['section']}: Câu hỏi/Nội dung: '{w['question']}' | Lỗi sai: Chọn '{w['user_ans']}' (Đúng phải là '{w['correct_ans']}')" 
        for w in wrong_answers
    ])
    
    prompt = f"""
    Học viên vừa hoàn thành bài thi thử HSK {level} và đạt {score}/{max_score} điểm.
    Dưới đây là danh sách các câu học viên làm sai:
    {wrong_context}
    
    Dựa trên các lỗi sai này, hãy:
    1. Đánh giá ngắn gọn về điểm yếu của học viên (Ngữ pháp, từ vựng, hay kỹ năng nghe/đọc).
    2. Đưa ra 2-3 lời khuyên cụ thể, thực tế để học viên cải thiện.
    Lưu ý: Bạn là một giáo viên nhiệt huyết, hãy dùng giọng điệu khích lệ. Đừng chấm điểm lại vì hệ thống đã chấm rồi.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Hệ thống AI nhận xét đang bận, vui lòng thử lại sau."
    
def text_to_speech(text):
    tts = gTTS(text=text, lang='zh-cn')
    tts.save("temp_audio.mp3")
    with open("temp_audio.mp3", "rb") as f:
        data = f.read()
    os.remove("temp_audio.mp3")
    return base64.b64encode(data).decode()

def ai_evaluate_exam(exam_data, user_answers):
    prompt = f"Dựa trên đề thi {exam_data} và bài làm {user_answers}, hãy phân tích chi tiết lỗi sai ngữ pháp, từ vựng và đưa ra lời khuyên học tập bằng tiếng Việt."
    return model.generate_content(prompt).text
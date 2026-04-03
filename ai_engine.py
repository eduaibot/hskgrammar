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
    
def generate_full_exam(level, difficulty):
    prompt = f"""
    Đóng vai trò là một chuyên gia ra đề thi HSK. Hãy tạo một đề thi thử HSK cấp độ {level}, độ khó {difficulty}.
    Số lượng: 5 câu Nghe, 40 câu Đọc, 15 câu Viết (nhớ phải tạo đủ số câu), thoải mái suy nghĩ k vấn đề thời gian bao giờ đủ số câu như này thì ok
    Đọc Gồm 3 phần nhỏ (Điền từ, Nối câu, Chọn đáp án đúng).
    Viết Gồm 2 phần nhỏ (Sắp xếp câu).

    YÊU CẦU JSON:
    {{
      "level": {level},
      "listening": [
        {{
          "text": "Câu tiếng Trung để phát âm thanh",
          "options": ["A. ...", "B. ...", "C. ..."],
          "answer": "A",
          "explanation_vn": "Giải thích ngắn bằng tiếng Việt tại sao chọn A",
          "points": 2.5
        }}
      ],
      "reading": [
        {{
          "question": "Câu hỏi/Đoạn văn Hán tự",
          "options": ["A. ...", "B. ...", "C. ..."],
          "answer": "B",
          "pinyin": "Phiên âm pinyin cho câu hỏi",
          "translation": "Dịch nghĩa tiếng Việt",
          "points": 2.5
        }}
      ],
      "writing": [
        {{
          "question": "Các từ xáo trộn hoặc câu hỏi viết",
          "answer": "Câu hoàn chỉnh đúng Hán tự",
          "pinyin": "Phiên âm của câu đáp án",
          "translation": "Dịch nghĩa của câu đáp án",
          "points": 100/15
        }}
      ]
    }}
    LƯU Ý: Trả về duy nhất JSON. Không có văn bản thừa.
    """
    try:
        response = model.generate_content(prompt)
        cleaned_json = clean_json_string(response.text.strip())
        data = json.loads(cleaned_json)
        return data
    except Exception as e:
        st.error(f"Lỗi tạo đề: {e}")
        return {"listening": [], "reading": [], "writing": []}
    
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
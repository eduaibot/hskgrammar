# app.py
import streamlit as st
import time
from grammar import HSK_GRAMMAR_DB
from database import (init_db, check_user, register_user, save_history, 
                      save_exam_progress, get_unfinished_exam, clear_unfinished_exam, get_history)
from ai_engine import get_grammar_practice, generate_full_exam, ai_give_feedback, text_to_speech, ai_evaluate_exam
import extra_streamlit_components as stx  # Thêm dòng này
import time
from datetime import datetime, timedelta
from styles import apply_styles

init_db()
apply_styles()

# --- 1. KHỞI TẠO COOKIE MANAGER ---
# Phải đặt key cố định để tránh bị reset khi rerun
cookie_manager = stx.CookieManager(key="hsk_cookie_manager")

# --- 2. CƠ CHẾ KIỂM TRA ĐĂNG NHẬP TỰ ĐỘNG ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Đợi 0.1 giây để Cookie Manager kịp khởi tạo (Fix lỗi async)
time.sleep(0.1) 
saved_user = cookie_manager.get('hsk_user_login')

# Nếu chưa đăng nhập nhưng tìm thấy Cookie -> Tự động login
if not st.session_state.logged_in and saved_user:
    st.session_state.logged_in = True
    st.session_state.user = saved_user
    st.rerun()

# --- 3. GIAO DIỆN ĐĂNG NHẬP ---
if not st.session_state.logged_in:
    st.markdown('<div class="glass-card"><h1>🏮 HSK AI MASTER</h1></div>', unsafe_allow_html=True)
    
    tab_login, tab_reg = st.tabs(["🔑 Đăng nhập", "📝 Đăng ký tài khoản"])
    
    with tab_login:
        with st.form("login_form"):
            u_login = st.text_input("Tên đăng nhập", placeholder="Nhập username...")
            p_login = st.text_input("Mật khẩu", type="password", placeholder="Nhập password...")
            remember_me = st.checkbox("Ghi nhớ đăng nhập trên trình duyệt này (30 ngày)", value=True)
            submit_login = st.form_submit_button("Vào hệ thống", use_container_width=True, type="primary")
            
            if submit_login:
                if not u_login or not p_login:
                    st.warning("Vui lòng nhập tài khoản và mật khẩu!")
                elif check_user(u_login, p_login): # Hàm của bạn trong database.py
                    # A. Cập nhật Session State
                    st.session_state.logged_in = True
                    st.session_state.user = u_login
                    
                    # B. QUAN TRỌNG: Lưu vào Cookie nếu người dùng tích chọn
                    if remember_me:
                        cookie_manager.set(
                            'hsk_user_login', 
                            u_login, 
                            expires_at=datetime.now() + timedelta(days=30),
                            key="set_cookie_login" # Thêm key để tránh xung đột
                        )
                    
                    st.success(f"Chào mừng {u_login}!")
                    time.sleep(0.5) # Đợi một chút để cookie kịp set
                    st.rerun()
                else:
                    st.error("❌ Sai tài khoản hoặc mật khẩu.")

    # ... (Giữ nguyên phần Tab Đăng ký của bạn) ...
    st.stop()
    
# --- KHỞI TẠO TẤT CẢ TRẠNG THÁI (SESSION STATE) ---
if 'exam_running' not in st.session_state:
    st.session_state.exam_running = False
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
# Thêm dòng này để tránh lỗi khi render kết quả
if 'exam_data' not in st.session_state:
    st.session_state.exam_data = {}

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title(f"Xin chào, {st.session_state.user}")
    mode = st.radio("Chế độ học", ["Học Ngữ Pháp", "Thi Thử AI", "Lịch Sử & Tiến Độ"])
    if st.button("Đăng xuất"):
        cookie_manager.delete('hsk_user_login') # Xóa cookie trên trình duyệt
        st.session_state.clear() # Xóa hết session
        st.rerun()

# --- MÀN HÌNH 1: HỌC NGỮ PHÁP ---
if mode == "Học Ngữ Pháp":
    st.header("📚 Thư viện Ngữ pháp HSK 1-6")
    level = st.tabs([f"HSK {i}" for i in range(1, 7)])
    
    for i, tab in enumerate(level):
        with tab:
            for g in HSK_GRAMMAR_DB.get(i+1, []):
                with st.expander(f"🔹 {g['title']}"):
                    st.write(g['desc'])
                    if st.button(f"Luyện tập {g['id']}", key=g['id']):
                        for key in ['user_selections', 'available_words', 'current_quiz']:
                            if key in st.session_state:
                                del st.session_state[key]
                        with st.spinner("AI đang tạo câu hỏi..."):
                            st.session_state.current_quiz = get_grammar_practice(i+1, g['title'])
                            st.session_state.quiz_step = 0

    if 'current_quiz' in st.session_state:
        quiz_data = st.session_state.current_quiz

        # --- BƯỚC 1: KHỞI TẠO DỮ LIỆU (LUÔN CHẠY TRƯỚC) ---
        # Kiểm tra xem đã có dữ liệu trong session_state chưa, nếu chưa hoặc dữ liệu cũ thì nạp mới
        if 'available_words' not in st.session_state or 'user_selections' not in st.session_state:
            st.session_state.user_selections = {i: [] for i in range(len(quiz_data))}
            st.session_state.available_words = {}
            for i, item in enumerate(quiz_data):
                # Lấy list từ xáo trộn từ AI (phòng hờ KeyError)
                raw_words = item.get('shuffled_words', item.get('words', []))
                st.session_state.available_words[i] = list(raw_words)

        # --- BƯỚC 2: GIAO DIỆN (CHỈ CHẠY KHI ĐÃ CÓ DỮ LIỆU) ---
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("✍️ Sắp xếp câu (Bấm vào từ để chọn)")

        for idx, item in enumerate(quiz_data):
            st.write(f"---")
            st.write(f"**Câu {idx+1}:**")

            # 1. NGĂN CHỨA CÂU (Các từ đã chọn)
            st.write("*Câu của bạn:*")
            st.markdown('<div style="background:rgba(255,255,255,0.05); padding:10px; border-radius:5px; min-height:50px; margin-bottom:10px; border: 1px dashed rgba(255,255,255,0.2);">', unsafe_allow_html=True)
            
            selected = st.session_state.user_selections[idx]
            if not selected:
                st.caption("Hãy chọn các từ bên dưới...")
            else:
                # Hiển thị các từ đã chọn thành hàng ngang
                cols_sel = st.columns(len(selected) + 1)
                for i, word in enumerate(selected):
                    # Nút màu xanh (Primary) để phân biệt từ đã chọn
                    if cols_sel[i].button(word, key=f"btn_sel_{idx}_{i}", type="primary"):
                        # Logic: Xóa khỏi ngăn chứa -> Trả về hàng chờ
                        st.session_state.user_selections[idx].pop(i)
                        st.session_state.available_words[idx].append(word)
                        st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

            # 2. HÀNG CHỜ TỪ (Các từ còn lại để chọn)
            st.write("*Từ còn lại (Bấm để chọn):*")
            available = st.session_state.available_words[idx]
            
            if not available:
                st.caption("✅ Đã xếp xong.")
            else:
                # Hiển thị tối đa 4 nút mỗi hàng để tránh bị tràn màn hình mobile
                n_cols = 4
                for i in range(0, len(available), n_cols):
                    row_words = available[i : i + n_cols]
                    cols_avail = st.columns(n_cols)
                    for j, word in enumerate(row_words):
                        if cols_avail[j].button(word, key=f"btn_avail_{idx}_{i+j}"):
                            # Logic: Thêm vào ngăn chứa -> Xóa khỏi hàng chờ
                            st.session_state.user_selections[idx].append(word)
                            st.session_state.available_words[idx].pop(i + j)
                            st.rerun()

        # --- BƯỚC 3: CHẤM ĐIỂM ---
        st.write("---")
        if st.button("🚀 Chấm điểm", use_container_width=True, type="secondary"):
            score = 0
            for idx, item in enumerate(quiz_data):
                # Ghép các từ người dùng đã chọn thành chuỗi để so sánh
                user_sentence = "".join(st.session_state.user_selections[idx])
                
                # Làm sạch chuỗi (xóa khoảng trắng/dấu câu) để so sánh chính xác
                def clean(s): return s.replace(" ", "").replace("。", "").replace("？", "").replace("！", "").strip()
                
                correct_ans = item.get('correct_answer', '')
                
                with st.expander(f"Kết quả Câu {idx+1}", expanded=True):
                    if clean(user_sentence) == clean(correct_ans) and user_sentence != "":
                        st.success("✅ Chính xác!")
                        score += 1
                    else:
                        st.error("❌ Chưa đúng.")
                    
                    st.write(f"**Bạn làm:** {clean(user_sentence)}")
                    st.write(f"**Đáp án:** {correct_ans}")
                    st.write(f"**Pinyin:** :orange[{item.get('pinyin')}]")
                    st.write(f"**Dịch nghĩa:** {item.get('translation')}")

            if score == len(quiz_data):
                st.balloons()

        # Nút làm bài mới (Reset session state)
        if st.button("🔄 Đổi bài tập khác"):
            for key in ['user_selections', 'available_words', 'current_quiz']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
        
# --- MÀN HÌNH 2: THI THỬ AI ---
elif mode == "Thi Thử AI":
    # Khởi tạo session state
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = {}
    if 'exam_running' not in st.session_state:
        st.session_state.exam_running = False

    # 1. MÀN HÌNH CHUẨN BỊ
    if not st.session_state.exam_running and 'last_feedback' not in st.session_state:
        st.header("📝 Hệ thống Thi thử HSK AI (Reading & Writing)")
        
        unfinished = get_unfinished_exam(st.session_state.user)
        if unfinished:
            st.warning("⚠️ Bạn có một bài thi đang làm dở!")
            c_resume, c_new = st.columns(2)
            if c_resume.button("Tiếp tục làm bài", use_container_width=True):
                st.session_state.exam_data = unfinished["exam"]
                st.session_state.user_answers = unfinished["answers"]
                st.session_state.exam_time = unfinished["time_left"]
                st.session_state.start_time = time.time()
                st.session_state.exam_running = True
                st.session_state.submitted = False
                st.rerun()
            if c_new.button("Bỏ qua & Xóa bài cũ", use_container_width=True):
                clear_unfinished_exam(st.session_state.user)
                st.rerun()
            st.stop()

        st.subheader("Thiết lập đề thi")
        c1, c2, c3 = st.columns(3)
        lv = c1.selectbox("Cấp độ HSK", [2, 3, 4, 5, 6], index=1)
        diff = c2.select_slider("Độ khó", ["Dễ", "Vừa", "Khó"], value="Vừa")
        tm = c3.number_input("Thời gian (phút)", 5, 120, 30)
        
        if st.button("🔥 BẮT ĐẦU THI", use_container_width=True, type="primary"):
            with st.spinner("Gemini đang soạn đề (Đọc & Viết)..."):
                st.session_state.exam_data = generate_full_exam(lv, diff)
                st.session_state.exam_time = tm * 60
                st.session_state.start_time = time.time()
                st.session_state.user_answers = {} 
                st.session_state.exam_running = True
                st.session_state.submitted = False
                # Dọn dẹp session cũ
                for k in list(st.session_state.keys()):
                    if any(x in k for x in ["in_R_", "in_W_"]):
                        del st.session_state[k]
                st.rerun()

    # 2. GIAO DIỆN LÀM BÀI
    elif st.session_state.exam_running:
        exam = st.session_state.exam_data
        read_qs = exam.get('reading', [])
        write_qs = exam.get('writing', [])

        elapsed = time.time() - st.session_state.start_time
        remaining = int(st.session_state.exam_time - elapsed)
        
        if remaining <= 0:
            st.session_state.submitted = True
            st.session_state.exam_running = False
            st.rerun()

        c_time, c_save = st.columns([3, 1])
        c_time.subheader(f"⏳ Còn lại: {remaining//60:02d}:{remaining%60:02d}")
        if c_save.button("💾 Lưu & Thoát"):
            save_exam_progress(st.session_state.user, exam, st.session_state.user_answers, remaining)
            st.session_state.exam_running = False
            st.rerun()

        # --- BIẾN ĐIỀU KHIỂN TRẠNG THÁI ---
        if 'submitted' not in st.session_state:
            st.session_state.submitted = False

        # --- HIỂN THỊ TỔNG ĐIỂM (CHỈ HIỆN KHI ĐÃ NỘP BÀI) ---
        if st.session_state.submitted:
            total_q = len(read_qs) + len(write_qs)
            score = st.session_state.user_score
            st.markdown(f"""
                <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #ff4b4b;">
                    <h1 style="margin:0; color: #ff4b4b;">🎯 TỔNG ĐIỂM: {score} / {total_q}</h1>
                    <p style="font-size: 18px;">({round(score/total_q*100, 1)}% hoàn thành)</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("🔄 Làm đề mới"):
                st.session_state.submitted = False
                st.session_state.exam_running = False
                st.rerun()
            st.divider()

        # --- HIỂN THỊ NỘI DUNG ĐỀ / BÀI CHẤM ---
        with st.form("hsk_exam_form"):
            # --- I. PHẦN ĐỌC HIỂU ---
            if read_qs:
                st.write("### I. PHẦN ĐỌC HIỂU")
                for i, q in enumerate(read_qs):
                    st.markdown(f"**Câu {i+1}:**")
                    u_ans = st.session_state.user_answers.get(f"R_{i}", "").strip()
                    correct_ans = str(q.get('answer', '')).strip()
                    
                    # Hiển thị câu hỏi (Trắc nghiệm/Điền từ/Sắp xếp)
                    if q.get('type') == 'fill_blank':
                        st.write(f"Từ gợi ý: {', '.join(q.get('words', []))}")
                        st.write(f"Câu hỏi: {q['question']}")
                    elif q.get('type') == 'order':
                        for opt in q['options']: st.write(opt)
                    elif q.get('type') == 'choice':
                        st.write(q.get('passage', ''))
                        st.write(f"★ {q.get('question', '')}")
                        if not st.session_state.submitted:
                            options = q['options']
                            default_idx = options.index(u_ans) if u_ans in options else None
                            u_ans = st.radio(f"Chọn đáp án câu {i+1}:", options, index=default_idx, key=f"r_radio_{i}")
                    
                    # Nếu chưa nộp: hiện ô nhập liệu
                    if not st.session_state.submitted and q.get('type') != 'choice':
                        u_ans = st.text_input("Đáp án của bạn:", value=u_ans, key=f"r_input_{i}")
                        st.session_state.user_answers[f"R_{i}"] = u_ans

                    # NẾU ĐÃ NỘP BÀI: HIỆN ĐÁP ÁN & GIẢI THÍCH
                    if st.session_state.submitted:
                        is_correct = (u_ans.lower() == correct_ans.lower())
                        color = "#28a745" if is_correct else "#dc3545" # Màu xanh / đỏ
                        
                        # 1. Hiển thị thông báo đúng/sai
                        st.markdown(f"**Kết quả:** <span style='color:{color}; font-weight:bold;'>{'✅ Đúng' if is_correct else '❌ Sai'}</span>", unsafe_allow_html=True)
                        
                        # 2. Nếu là điền từ, hiển thị câu đã điền hoàn chỉnh (đã có dấu ** từ AI)
                        if q.get('type') == 'fill_blank' and q.get('full_sentence'):
                            st.markdown(f"👉 **Câu hoàn chỉnh:** {q['full_sentence']}")
                        else:
                            st.markdown(f"👉 **Đáp án đúng:** `{correct_ans}`")

                        # 3. Hiển thị Pinyin và Nghĩa với style dễ nhìn
                        st.info(f"""
                        📖 **Pinyin:** {q.get('pinyin', '')}
                        🇻🇳 **Dịch nghĩa:** {q.get('translation', '')}
                        💡 **Giải thích:** {q.get('explanation_vn', '')}
                        """)

            # --- II. PHẦN VIẾT ---
            if write_qs:
                st.write("### II. PHẦN VIẾT")
                for i, q in enumerate(write_qs):
                    st.write(f"**Câu {i+1}:** {' '.join(q.get('shuffled_words', []))}")
                    u_ans = st.session_state.user_answers.get(f"W_{i}", "").strip()
                    correct_ans = q.get('answer', '').strip()

                    if not st.session_state.submitted:
                        u_ans = st.text_input("Viết lại câu hoàn chỉnh:", value=u_ans, key=f"w_input_{i}")
                        st.session_state.user_answers[f"W_{i}"] = u_ans

                    if st.session_state.submitted:
                        is_correct = (u_ans.replace(" ","") == correct_ans.replace(" ",""))
                        color = "green" if is_correct else "red"
                        st.markdown(f"**Kết quả:** <span style='color:{color}'>{'✅' if is_correct else '❌'}</span>", unsafe_allow_html=True)
                        st.write(f"**👉 Đáp án đúng:** {correct_ans}")
                        with st.expander("Dịch nghĩa & Pinyin"):
                            st.write(f"📖 **Pinyin:** {q.get('pinyin', '')}")
                            st.write(f"🇻🇳 **Dịch:** {q.get('translation', '')}")
                        st.divider()

            # Nút bấm chính
            if not st.session_state.submitted:
                if st.form_submit_button("NỘP BÀI CHẤM ĐIỂM", type="primary", use_container_width=True):
                    # TÍNH ĐIỂM
                    score = 0
                    # Chấm phần Đọc
                    for i, q in enumerate(read_qs):
                        ans = st.session_state.user_answers.get(f"R_{i}", "").strip().lower()
                        if ans == str(q.get('answer', '')).strip().lower():
                            score += 1
                    # Chấm phần Viết
                    for i, q in enumerate(write_qs):
                        ans = st.session_state.user_answers.get(f"W_{i}", "").strip().replace(" ","")
                        if ans == q.get('answer', '').strip().replace(" ",""):
                            score += 1
                    
                    st.session_state.user_score = score
                    st.session_state.submitted = True
                    # Tự động cuộn lên đầu bằng cách rerun
                    st.rerun()
    # 3. GIAO DIỆN CHẤM ĐIỂM
    if st.session_state.get('submitted'):
        exam = st.session_state.exam_data
        total_score, max_score, wrongs = 0, 0, []

        st.header("🧐 KẾT QUẢ CHI TIẾT")

        # Danh sách các phần thi (Đã bỏ Listening)
        sections = [
            (exam.get('reading', []), "R", "Đọc"),
            (exam.get('writing', []), "W", "Viết")
        ]

        for qs, prefix, name in sections:
            if qs:
                st.subheader(f"Phần {name}")
                for i, q in enumerate(qs):
                    pts = q.get('points', 10)
                    max_score += pts
                    
                    # Lấy đáp án người dùng từ session_state
                    u_ans = str(st.session_state.get(f"in_{prefix}_{i}", "")).strip().upper()
                    c_ans = str(q.get('answer', '')).strip().upper()
                    
                    # 1. Hiện lại câu hỏi của đề
                    st.write(f"**Câu {i+1}:** {q.get('question', '')}")
                    
                    # 2. Chấm điểm
                    if u_ans == c_ans:
                        st.success(f"✅ Đúng (+{pts})")
                        total_score += pts
                    else:
                        st.error(f"❌ Sai")
                        st.write(f"- Bạn chọn: `{u_ans if u_ans else '(Trống)'}`")
                        st.write(f"- Đáp án đúng: `{c_ans}`")
                        wrongs.append({
                            "section": name, 
                            "question": q.get('question', ''), 
                            "user_ans": u_ans, 
                            "correct_ans": c_ans
                        })
                    
                    # 3. Giải thích format: Hán tự | /pinyin/ | Nghĩa
                    hz = q.get('question', '') if prefix == "R" else q.get('answer', '')
                    py = q.get('pinyin', '...')
                    tr = q.get('translation', '...')
                    st.markdown(f"📖 **{hz}** | `/{py}/` | 📝 *Nghĩa:* {tr}")
                    st.write("---")

        # AI Feedback
        if 'last_feedback' not in st.session_state:
            with st.spinner("AI đang phân tích bài làm..."):
                fb = ai_give_feedback(exam.get('level', 'N/A'), total_score, max_score, wrongs)
                st.session_state.last_feedback = f"## Tổng điểm: {total_score}/{max_score}\n\n" + fb
                save_history(st.session_state.user, "Thi HSK", f"{total_score}/{max_score}", "Reading/Writing")
                clear_unfinished_exam(st.session_state.user)
                st.rerun()

    if 'last_feedback' in st.session_state:
        st.markdown(st.session_state.last_feedback)
        if st.button("Làm bài mới"):
            keys_to_del = ['last_feedback', 'exam_data', 'user_answers', 'submitted', 'in_R_', 'in_W_']
            for k in list(st.session_state.keys()):
                if any(x in k for x in keys_to_del):
                    del st.session_state[k]
            st.rerun()
                    
# --- MÀN HÌNH 3: LỊCH SỬ ---
elif mode == "Lịch Sử & Tiến Độ":
    st.header("🕒 Lịch sử học tập của bạn")
    history = get_history(st.session_state.user)
    if history:
        for h in history:
            with st.expander(f"{h[3]} - {h[0]}"):
                st.write(f"Nội dung: {h[1]}")
                st.write(f"Kết quả: {h[2]}")
    else:
        st.write("Bạn chưa có dữ liệu học tập.")
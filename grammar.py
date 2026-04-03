# grammar.py
HSK_GRAMMAR_DB = {
    1: [
    {
        "id": "h1_1",
        "title": "Đại từ nhân xưng",
        "pinyin": "Dàicí (代词)",
        "desc": """**Từ khóa:** 我 Wǒ (Tôi), 你 Nǐ (Bạn), 他 Tā (Anh ấy), 她 Tā (Cô ấy), 们 men (Số nhiều).\n
Dùng để chỉ các đối tượng trong giao tiếp. Thêm 们 (men) vào sau đại từ để tạo số nhiều.\n
**Ví dụ:** 我们 (Wǒmen) - Chúng tôi; 他是我的老师 (Tā shì wǒ de lǎoshī) - Anh ấy là giáo viên của tôi."""
    },
    {
        "id": "h1_2",
        "title": "Đại từ nghi vấn",
        "pinyin": "Yíwèn dàicí (疑问代词)",
        "desc": """**Từ khóa:** 谁 Shéi (Ai), 什么 Shénme (Cái gì), 哪儿 Nǎr (Ở đâu), 怎么 Zěnme (Thế nào).\n
Dùng để đặt câu hỏi. Trong tiếng Trung, đại từ nghi vấn đặt ở vị trí của thành phần cần hỏi.\n
**Ví dụ:** 你是谁？ (Nǐ shì shéi?) - Bạn là ai?; 这是什么？ (Zhè shì shénme?) - Đây là cái gì?"""
    },
    {
        "id": "h1_3",
        "title": "Số từ 1-100",
        "pinyin": "Shùcí (数词)",
        "desc": """**Từ khóa:** 一 Yī (1), 二 Èr (2), 三 Sān (3), 十 Shí (10), 百 Bǎi (100).\n
Quy tắc: Số hàng chục + 十 (Shí) + Số đơn vị. \n
**Ví dụ:** 二十五 (Èrshíwǔ) - 25; 九十九 (Jiǔshíjiǔ) - 99; 我家有三口人 (Wǒ jiā yǒu sān kǒu rén) - Nhà tôi có 3 người."""
    },
    {
        "id": "h1_4",
        "title": "Lượng từ cơ bản",
        "pinyin": "Liàngcí (量词)",
        "desc": """**Từ khóa:** 个 gè (Cái/Con), 本 běn (Quyển/Cuốn), 口 kǒu (Người - gia đình).\n
Dùng giữa số từ và danh từ. Mỗi loại danh từ thường đi kèm với một lượng từ nhất định.\n
**Ví dụ:** 三个苹果 (Sān gè píngguǒ) - 3 quả táo; 五本书 (Wǔ běn shū) - 5 quyển sách."""
    },
    {
        "id": "h1_5",
        "title": "Trợ từ sở hữu '的'",
        "pinyin": "de (的)",
        "desc": """**Từ khóa:** 的 de (Của / dùng để kết nối định ngữ).\n
Diễn tả mối quan hệ sở hữu hoặc tính chất giữa hai danh từ.\n
**Ví dụ:** 我的书 (Wǒ de shū) - Sách của tôi; 漂亮的学生 (Piàoliang de xuésheng) - Học sinh xinh đẹp."""
    },
    {
        "id": "h1_6",
        "title": "Phó từ phủ định '不' và '没'",
        "pinyin": "Bù (不) / Méi (没)",
        "desc": """**Từ khóa:** 不 bù (Không - hiện tại/tương lai), 没 méi (Chưa - quá khứ).\n
**Ví dụ:** 我不喝水 (Wǒ bù hē shuǐ) - Tôi không uống nước; 我没去商店 (Wǒ méi qù shāngdiàn) - Tôi đã không đi cửa hàng."""
    },
    {
        "id": "h1_7",
        "title": "Phó từ mức độ '很' và '太'",
        "pinyin": "Hěn (很) / Tài (太)",
        "desc": """**Từ khóa:** 很 hěn (Rất), 太...了 tài...le (Quá... rồi).\n
Dùng để nhấn mạnh mức độ của tính từ.\n
**Ví dụ:** 很好 (Hěn hǎo) - Rất tốt; 这里的菜太好了 (Zhèlǐ de cài tài hǎo le) - Đồ ăn ở đây tốt quá rồi!"""
    },
    {
        "id": "h1_8",
        "title": "Trợ từ nghi vấn '吗' và '呢'",
        "pinyin": "ma (吗) / ne (呢)",
        "desc": """**Từ khóa:** 吗 ma (Dùng hỏi Có/Không), 呢 ne (Hỏi tỉnh lược: Còn... thì sao?).\n
**Ví dụ:** 你好吗？ (Nǐ hǎo ma?) - Bạn khỏe không?; 我很好，你呢？ (Wǒ hěn hǎo, nǐ ne?) - Tôi khỏe, còn bạn?"""
    },
    {
        "id": "h1_9",
        "title": "Câu chữ '是'",
        "pinyin": "shì (是)",
        "desc": """**Từ khóa:** 是 shì (Là / Khẳng định danh tính).\n
Cấu trúc: A + 是 + B. Dùng để giới thiệu hoặc khẳng định A là B.\n
**Ví dụ:** 我是学生 (Wǒ shì xuésheng) - Tôi là học sinh; 他不是我的朋友 (Tā búshì wǒ de péngyou) - Anh ấy không phải bạn tôi."""
    },
    {
        "id": "h1_10",
        "title": "Giới từ địa điểm '加'",
        "pinyin": "zài (在)",
        "desc": """**Từ khóa:** 在 zài (Ở / Tại).\n
Dùng để chỉ vị trí của người hoặc vật. Cấu trúc: S + 在 + Địa điểm + V.\n
**Ví dụ:** 我在学校 (Wǒ zài xuéxiào) - Tôi ở trường; 他在家里吃饭 (Tā zài jiālǐ chīfàn) - Anh ấy ăn cơm ở nhà."""
    },
    {
        "id": "h1_11",
        "title": "Động từ năng nguyện '会' và '想'",
        "pinyin": "Huì (会) / Xiǎng (想)",
        "desc": """**Từ khóa:** 会 huì (Biết - qua học tập), 想 xiǎng (Muốn / Nghĩ).\n
**Ví dụ:** 我会说汉语 (Wǒ huì shuō Hànyǔ) - Tôi biết nói tiếng Trung; 我想去北京 (Wǒ xiǎng qù Běijīng) - Tôi muốn đi Bắc Kinh."""
    },
    {
        "id": "h1_12",
        "title": "Cách hỏi '几' và '多少'",
        "pinyin": "Jǐ (几) / Duōshǎo (多少)",
        "desc": """**Từ khóa:** 几 jǐ (Mấy - số lượng < 10), 多少 duōshǎo (Bao nhiêu - số lượng > 10).\n
**Ví dụ:** 你几岁了？ (Nǐ jǐ suì le?) - Cháu mấy tuổi rồi?; 这个多少钱？ (Zhè ge duōshǎo qián?) - Cái này bao nhiêu tiền?"""
    },
    {
        "id": "h1_13",
        "title": "Nhấn mạnh '是...的'",
        "pinyin": "shì... de (是... de)",
        "desc": """**Từ khóa:** 是...的 shì...de (Nhấn mạnh thời gian, địa điểm, cách thức).\n
Dùng cho hành động đã xảy ra trong quá khứ.\n
**Ví dụ:** 我是坐飞机来的 (Wǒ shì zuò fēijī lái de) - Tôi đi máy bay đến (nhấn mạnh phương thức)."""
    },
    {
        "id": "h1_14",
        "title": "Trợ từ ngữ khí '了'",
        "pinyin": "le (了)",
        "desc": """**Từ khóa:** 了 le (Đã / Biểu thị sự thay đổi).\n
Đặt sau động từ hoặc cuối câu.\n
**Ví dụ:** 我买了一本书 (Wǒ mǎi le yì běn shū) - Tôi đã mua một quyển sách; 下雨了 (Xià yǔ le) - Mưa rồi (biểu thị sự thay đổi)."""
    }
],
    2: [
    {
        "id": "h2_1",
        "title": "Trợ động từ '要' và '想'",
        "pinyin": "Yào (要) / Xiǎng (想)",
        "desc": """**Từ khóa:** 要 yào (Muốn/Phải - quyết tâm cao), 想 xiǎng (Muốn/Nghĩ - nguyện vọng).\n
**Cấu trúc:** $S + [要/想] + V + O$\n
Dùng để diễn tả ý định hoặc mong muốn thực hiện hành động.\n
**Ví dụ:** 我想去商店 (Wǒ xiǎng qù shāngdiàn) - Tôi muốn đi cửa hàng; 我 muốn mua (我要买) một cái điện thoại mới (一个新手机 - yí gè xīn shǒujī)."""
    },
    {
        "id": "h2_2",
        "title": "Khả năng với '会' và '能'",
        "pinyin": "Huì (会) / Néng (能)",
        "desc": """**Từ khóa:** 会 huì (Biết - qua học tập), 能 néng (Có thể - điều kiện khách quan).\n
**Cấu trúc:** $S + [会/能] + V + O$\n
**Ví dụ:** 我会说汉语 (Wǒ huì shuō Hànyǔ) - Tôi biết nói tiếng Trung; 我 hôm nay (我今天 - wǒ jīntiān) có thể đến (能来 - néng lái)."""
    },
    {
        "id": "h2_3",
        "title": "Câu so sánh với '比'",
        "pinyin": "bǐ (比)",
        "desc": """**Từ khóa:** 比 bǐ (So với/Hơn).\n
**Cấu trúc:** $A + 比 + B + Adj$\n
Dùng để so sánh tính chất giữa hai đối tượng A và B.\n
**Ví dụ:** 哥哥比我高 (Gēge bǐ wǒ gāo) - Anh trai cao hơn tôi; 今天比昨天热 (Jīntiān bǐ zuótiān rè) - Hôm nay nóng hơn hôm qua."""
    },
    {
        "id": "h2_4",
        "title": "Trợ từ động thái '过'",
        "pinyin": "guò (过)",
        "desc": """**Từ khóa:** 过 guò (Đã từng - nhấn mạnh trải nghiệm).\n
**Cấu trúc:** $S + V + 过 + O$\n
Diễn tả một hành động đã từng xảy ra trong quá khứ và nay đã kết thúc.\n
**Ví dụ:** 我看过这个电影 (Wǒ kàn guò zhè ge diànyǐng) - Tôi đã từng xem bộ phim này; 你去过中国吗？ (Nǐ qù guò Zhōngguó ma?) - Bạn đã từng đi Trung Quốc chưa?"""
    },
    {
        "id": "h2_5",
        "title": "Trợ từ trạng thái '着'",
        "pinyin": "zhe (着)",
        "desc": """**Từ khóa:** 着 zhe (Đang/Duy trì trạng thái).\n
**Cấu trúc:** $V + 着$\n
Diễn tả một trạng thái đang được duy trì (ví dụ: cửa đang mở, anh ấy đang mặc).\n
**Ví dụ:** 门开着 (Mén kāi zhe) - Cửa đang mở; 他拿着一本书 (Tā ná zhe yì běn shū) - Anh ấy đang cầm một quyển sách."""
    },
    {
        "id": "h2_6",
        "title": "Câu hỏi lựa chọn '还是'",
        "pinyin": "háishì (还是)",
        "desc": """**Từ khóa:** 还是 háishì (Hay là - dùng trong câu hỏi).\n
**Cấu trúc:** $A + 还是 + B?$\n
Đưa ra hai lựa chọn để người nghe chọn một.\n
**Ví dụ:** 你喝茶还是喝咖啡？ (Nǐ hē chá háishì hē kāfēi?) - Bạn uống trà hay uống cà phê?"""
    },
    {
        "id": "h2_7",
        "title": "Giới từ chỉ khoảng cách '离'",
        "pinyin": "lí (离)",
        "desc": """**Từ khóa:** 离 lí (Cách - khoảng cách không gian/thời gian).\n
**Cấu trúc:** $A + 离 + B + (Mức độ) + Adj$\n
**Ví dụ:** 我家离学校很近 (Wǒ jiā lí xuéxiào hěn jìn) - Nhà tôi cách trường rất gần; Công ty cách đây không xa (公司离这儿不远 - gōngsī lí zhèr bù yuǎn)."""
    },
    {
        "id": "h2_8",
        "title": "Phó từ thời gian '就' và '才'",
        "pinyin": "jiù (就) / cái (才)",
        "desc": """**Từ khóa:** 就 jiù (Thì/Sớm), 才 cái (Mới/Muộn).\n
**Cấu trúc:** $S + Time + [就/才] + V + O$\n
**Ví dụ:** 他八点就来了 (Tā bā diǎn jiù lái le) - Tám giờ anh ấy đã đến rồi (sớm); 他九点才来 (Tā jiǔ diǎn cái lái) - Chín giờ anh ấy mới đến (muộn)."""
    },
    {
        "id": "h2_9",
        "title": "Bổ ngữ kết quả cơ bản",
        "pinyin": "Jiéguǒ bǔyǔ (结果补语)",
        "desc": """**Từ khóa:** 好 hǎo (Xong/Tốt), 完 wán (Hết), 懂 dǒng (Hiểu), 见 jiàn (Thấy).\n
**Cấu trúc:** $V + [Bổ ngữ kết quả] + 了$\n
Diễn tả kết quả đạt được sau khi thực hiện hành động.\n
**Ví dụ:** 我听懂了 (Wǒ tīng dǒng le) - Tôi nghe hiểu rồi; 饭做好了 (Fàn zuò hǎo le) - Cơm làm xong rồi."""
    },
    {
        "id": "h2_10",
        "title": "Liên từ '因为...所以...'",
        "pinyin": "yīnwèi... suǒyǐ... (因为...所以...)",
        "desc": """**Từ khóa:** 因为 yīnwèi (Bởi vì), 所以 suǒyǐ (Cho nên).\n
**Cấu trúc:** $因为 + Nguyên nhân, 所以 + Kết quả$\n
**Ví dụ:** 因为天气不好，所以我不去学校 (Yīnwèi tiānqì bù hǎo, suǒyǐ wǒ bú qù xuéxiào) - Vì thời tiết không tốt nên tôi không đi học."""
    },
    {
        "id": "h2_11",
        "title": "Cấu trúc 'Tuy... nhưng...'",
        "pinyin": "suīrán... dànshì... (虽然...但是...)",
        "desc": """**Từ khóa:** 虽然 suīrán (Tuy rằng), 但是 dànshì (Nhưng mà).\n
**Cấu trúc:** $虽然 + Phân câu 1, 但是 + Phân câu 2$\n
**Ví dụ:** 虽然外面很冷， nhưng trong phòng rất ấm (但是房间里很暖和 - dànshì fángjiān lǐ hěn nuǎnhuó)."""
    },
    {
        "id": "h2_12",
        "title": "Thời điểm hành động 'đang xảy ra'",
        "pinyin": "zhèngzài... ne (正在...呢)",
        "desc": """**Từ khóa:** 正在 zhèngzài (Đang), 呢 ne (Trợ từ cuối câu).\n
**Cấu trúc:** $S + 正在 + V + (O) + 呢$\n
**Ví dụ:** 我正在看电视呢 (Wǒ zhèngzài kàn diànshì ne) - Tôi đang xem TV đây; 他们正在打篮球 (Tāmen zhèngzài dǎ lánqiú) - Họ đang đánh bóng rổ."""
    },
    {
        "id": "h2_13",
        "title": "Câu hành động sắp xảy ra",
        "pinyin": "kuàiyào... le (快要...了)",
        "desc": """**Từ khóa:** 快要 kuàiyào (Sắp), 了 le (Rồi).\n
**Cấu trúc:** $S + 快要 + V + 了$\n
**Ví dụ:** 火车快 muốn chạy rồi (火车快要开了 - huǒchē kuàiyào kāi le); Sắp mưa rồi (快要下雨了 - kuàiyào xià yǔ le)."""
    },
    {
        "id": "h2_14",
        "title": "Giới từ 'đối với'",
        "pinyin": "duì (对)",
        "desc": """**Từ khóa:** 对 duì (Đối với/Hướng về).\n
**Cấu trúc:** $A + 对 + B + Adj/V$\n
Dùng để chỉ đối tượng mà hành động hoặc tính chất hướng tới.\n
**Ví dụ:** 跑步对身体很好 (Pǎobù duì shēntǐ hěn hǎo) - Chạy bộ rất tốt cho sức khỏe; 老师对我也很好 (Lǎoshī duì wǒ yě hěn hǎo) - Thầy giáo đối với tôi cũng rất tốt."""
    }
],
    3: [
    {
        "id": "h3_1",
        "title": "Bổ ngữ xu hướng phức hợp",
        "pinyin": "Fùhé qūxiàng bǔyǔ (复合趋向补语)",
        "desc": """**Từ khóa:** 进来 jìnhlái (Vào đây), 拿出来 ná chūlái (Lấy ra đây), 走 quá khứ (走过去 - zǒu guòqù).\n
**Cấu trúc:** $S + V + [上/下/进/出/回/过/起] + [来/去]$\n
Dùng để chỉ hướng cụ thể của hành động so với người nói.\n
**Ví dụ:** 老师 (Lǎoshī) đi vào lớp học rồi (走进了教室来 - zǒu jìn le jiàoshì lái); 请 (Qǐng) lấy sách ra (把书拿出来 - bǎ shū ná chūlái)."""
    },
    {
        "id": "h3_2",
        "title": "Bổ ngữ khả năng",
        "pinyin": "Kěnéng bǔyǔ (可能补语)",
        "desc": """**Từ khóa:** 得 de (Có thể), 不 bù (Không thể).\n
**Cấu trúc:** $V + 得/不 + [Kết quả/Xu hướng]$\n
Diễn tả một hành động có thể đạt được kết quả nào đó hay không.\n
**Ví dụ:** 我 (Wǒ) nhìn thấy được (看得见 - kàn de jiàn); 老师 (Lǎoshī) nói nhanh quá, tôi nghe không hiểu (我听不懂 - wǒ tīng bù dǒng)."""
    },
    {
        "id": "h3_3",
        "title": "Bổ ngữ trạng thái nâng cao",
        "pinyin": "Zhuàngtài bǔyǔ (状态补语)",
        "desc": """**Từ khóa:** 得 de (Dùng để kết nối động từ và phần miêu tả).\n
**Cấu trúc:** $V + 得 + [Phó từ mức độ] + Adj$\n
Dùng để đánh giá hoặc miêu tả trạng thái/trình độ của hành động.\n
**Ví dụ:** 他 (Tā) chạy rất nhanh (跑得很快 - pǎo de hěn kuài); 她 (Tā) hát rất hay (唱得非常好 - chàng de fēicháng hǎo)."""
    },
    {
        "id": "h3_4",
        "title": "Câu chữ '把'",
        "pinyin": "bǎ zì jù (把字句)",
        "desc": """**Từ khóa:** 把 bǎ (Dùng để đưa tân ngữ lên trước động từ).\n
**Cấu trúc:** $S + 把 + O + V + Thành phần khác (了/Bổ ngữ)$\n
Dùng khi hành động làm thay đổi trạng thái hoặc vị trí của tân ngữ.\n
**Ví dụ:** 我 (Wǒ) đã làm xong bài tập rồi (把作业做完了 - bǎ zuòyè zuò wán le); 请 (Qǐng) dọn dẹp phòng sạch sẽ (把房间打扫干净 - bǎ fángjiān dǎsǎo gānjìng)."""
    },
    {
        "id": "h3_5",
        "title": "Câu bị động với '被'",
        "pinyin": "bèi zì jù (被字句)",
        "desc": """**Từ khóa:** 被 bèi (Bị/Được).\n
**Cấu trúc:** $O (Vật bị tác động) + 被 + S (Người tác động) + V + Thành phần khác$\n
Nhấn mạnh vào đối tượng chịu tác động của hành động.\n
**Ví dụ:** 我的蛋糕 (Wǒ de dàngāo) bị em gái ăn mất rồi (被妹妹吃了 - bèi mèimei chī le); 他的钱 (Tā de qián) bị trộm mất rồi (被偷了 - bèi tōu le)."""
    },
    {
        "id": "h3_6",
        "title": "Cấu trúc 'Càng... Càng...'",
        "pinyin": "yuè... yuè... (越...越...)",
        "desc": """**Từ khóa:** 越 yuè (Càng).\n
**Cấu trúc:** $越 + [V/Adj] + 越 + [V/Adj]$\n
Diễn tả mức độ của một trạng thái biến đổi theo một hành động hoặc trạng thái khác.\n
**Ví dụ:** 雨 (Yǔ) càng lúc càng to (越下越大 - yuè xià yuè dà); 汉语 (Hànyǔ) càng học càng thú vị (越学越有意思 - yuè xué yuè yǒu yìsi)."""
    },
    {
        "id": "h3_7",
        "title": "Cấu trúc 'Chỉ có... mới...'",
        "pinyin": "zhǐyǒu... cái... (只有...才...)",
        "desc": """**Từ khóa:** 只有 zhǐyǒu (Chỉ có), 才 cái (Mới).\n
**Cấu trúc:** $只有 + [Điều kiện duy nhất], 才 + [Kết quả]$\n
**Ví dụ:** 只有 (Zhǐyǒu) nỗ lực học tập (努力学习 - nǔlì xuéxí), mới thi tốt được (才能 trade hǎo - cái néng kǎo hǎo)."""
    },
    {
        "id": "h3_8",
        "title": "Cấu trúc 'Chỉ cần... thì...'",
        "pinyin": "zhǐyào... jiù... (只要...就...)",
        "desc": """**Từ khóa:** 只要 zhǐyào (Chỉ cần), 就 jiù (Thì).\n
**Cấu trúc:** $只要 + [Điều kiện cần], 就 + [Kết quả]$\n
**Ví dụ:** 只要 (Zhǐyào) ngày mai không mưa (明天不下雨 - míngtiān bú xià yǔ), chúng tôi sẽ đi (我们就去 - wǒmen jiù qù)."""
    },
    {
        "id": "h3_9",
        "title": "Cấu trúc 'Càng sớm càng tốt' (Lặp động từ)",
        "pinyin": "V + 了 + 又 + V (V 了又 V)",
        "desc": """**Từ khóa:** 又 yòu (Lại - lặp lại hành động).\n
**Cấu trúc:** $V + 了 + 又 + V$\n
Diễn tả hành động xảy ra lặp đi lặp lại nhiều lần.\n
**Ví dụ:** 他 (Tā) xem đi xem lại (看了又看 - kàn le yòu kàn) bức ảnh này (这张照片 - zhè zhāng zhàopiàn)."""
    },
    {
        "id": "h3_10",
        "title": "Phó từ 'Mới' (Mối quan hệ thời gian)",
        "pinyin": "cái (才)",
        "desc": """**Từ khóa:** 才 cái (Vừa nãy mới / Muộn hơn dự kiến).\n
**Cấu trúc:** $S + Time + 才 + V$\n
**Ví dụ:** 我 (Wǒ) 11 giờ đêm mới ngủ (十一动才睡觉 - shíyī diǎn cái shuìjiào); 他 (Tā) bây giờ mới đến (现在才来 - xiànzài cái lái)."""
    },
    {
        "id": "h3_11",
        "title": "Cấu trúc 'Vừa... vừa...' nâng cao",
        "pinyin": "yòu... yòu... (又...又...)",
        "desc": """**Từ khóa:** 又 yòu (Vừa).\n
**Cấu trúc:** $又 + Adj + 又 + Adj$\n
Dùng để miêu tả hai tính chất cùng tồn tại (thường cùng tốt hoặc cùng xấu).\n
**Ví dụ:** 这个西瓜 (Zhè ge xīguā) vừa ngọt vừa to (又甜又大 - yòu tián yòu dà)."""
    },
    {
        "id": "h3_12",
        "title": "Bổ ngữ thời lượng",
        "pinyin": "Shíjiān bǔyǔ (时间补语)",
        "desc": """**Từ khóa:** 了 le (Diễn tả khoảng thời gian duy trì).\n
**Cấu trúc:** $S + V + 了 + [Khoảng thời gian]$\n
**Ví dụ:** 我 (Wǒ) học tiếng Trung được một năm rồi (学了一年汉语了 - xué le yì nián Hànyǔ le); 他 (Tā) đợi tôi 30 phút rồi (等了我三十分钟了 - děng le wǒ sānshí fēnzhōng le)."""
    },
    {
        "id": "h3_13",
        "title": "Phó từ 'Vừa mới' (Cặp 刚 - 刚才)",
        "pinyin": "gāng (刚) / gāngcái (刚才)",
        "desc": """**Từ khóa:** 刚 gāng (Phó từ - Vừa mới làm), 刚才 gāngcái (Danh từ thời gian - Vừa nãy).\n
**Ví dụ:** 他 (Tā) vừa mới đi (刚走 - gāng zǒu); 刚才 (Gāngcái) ai gọi điện thoại thế? (谁打电话了？ - shéi dǎ diànhuà le?)"""
    },
    {
        "id": "h3_14",
        "title": "Cấu trúc 'Sắp... rồi'",
        "pinyin": "kuài... le (快...了)",
        "desc": """**Từ khóa:** 快 kuài (Sắp), 了 le (Rồi).\n
**Cấu trúc:** $S + 快 + V + 了$\n
**Ví dụ:** 快 (Kuài) vào học rồi (上课了 - shàngkè le); 我 (Wǒ) sắp xong rồi (快好了 - kuài hǎo le)."""
    }
],
    4: [
    {
        "id": "h4_1",
        "title": "Cấu trúc 'Vừa... vừa...' nâng cao",
        "pinyin": "yìbiān... yìbiān... (一边...一边...)",
        "desc": """**Từ khóa:** 一边 yìbiān (Vừa... vừa... - thực hiện hai hành động cùng lúc).\n
**Cấu trúc:** $S + 一边 + V1 + 一边 + V2$\n
Dùng để diễn tả hai hành động song song. Khác với 又...又... dùng cho tính chất.\n
**Ví dụ:** 他 (Tā) vừa ăn cơm vừa xem tivi (一边吃饭一边看电视 - yìbiān chīfàn yìbiān kàn diànshì)."""
    },
    {
        "id": "h4_2",
        "title": "Câu bị động với '让' và '叫'",
        "pinyin": "ràng (让) / jiào (叫)",
        "desc": """**Từ khóa:** 让 ràng / 叫 jiào (Bị/Được - dùng trong khẩu ngữ thay cho 被).\n
**Cấu trúc:** $O + [让/叫] + S + V + Thành phần khác$\n
Lưu ý: Sau 让 và 叫 bắt buộc phải có chủ thể thực hiện hành động (S).\n
**Ví dụ:** 我的手机 (Wǒ de shǒujī) bị anh ấy mượn đi rồi (让他拿走了 - ràng tā ná zǒu le)."""
    },
    {
        "id": "h4_3",
        "title": "Cấu trúc 'Ngay cả... cũng...'",
        "pinyin": "lián... dōu/yě... (连...都/也...)",
        "desc": """**Từ khóa:** 连 lián (Ngay cả/Thậm chí), 都 dōu / 也 yě (Cũng).\n
**Cấu trúc:** $连 + [S/O] + 都/也 + V$\n
Dùng để nhấn mạnh một trường hợp cực đoan để khẳng định sự việc.\n
**Ví dụ:** 他 (Tā) ngay cả tên tôi cũng quên rồi (连我的名字 chōu jiàng le - lián wǒ de míngzi dōu wàng le)."""
    },
    {
        "id": "h4_4",
        "title": "Cấu trúc 'Bất kể... đều...'",
        "pinyin": "wúlùn... dōu... (无论...都...)",
        "desc": """**Từ khóa:** 无论 wúlùn (Bất kể/Dù cho), 都 dōu (Đều).\n
**Cấu trúc:** $无论 + [Lựa chọn/Câu hỏi] + 都 + Kết quả$\n
Diễn tả kết quả không thay đổi trong bất kỳ điều kiện nào.\n
**Ví dụ:** 无论 (Wúlùn) trời mưa hay không (下不下雨 - xià bú xià yǔ), tôi đều đi (我 đều qù - wǒ dōu qù)."""
    },
    {
        "id": "h4_5",
        "title": "Cấu trúc 'Thà rằng... chứ không...'",
        "pinyin": "nìngkě... yě bù... (宁可...也不...)",
        "desc": """**Từ khóa:** 宁可 nìngkě (Thà rằng), 也不 yě bù (Cũng không).\n
**Cấu trúc:** $宁可 + A, 也不 + B$\n
Thể hiện sự lựa chọn kiên quyết, thà chấp nhận A còn hơn làm B.\n
**Ví dụ:** 我 (Wǒ) thà đi bộ (宁可走路 - nìngkě zǒulù), chứ không ngồi xe của anh ấy (也不坐他的车 - yě bú zuò tā de chē)."""
    },
    {
        "id": "h4_6",
        "title": "Cấu trúc 'Chẳng những... ngược lại còn...'",
        "pinyin": "búdàn méiyǒu... fǎn'ér... (不但没有...反而...)",
        "desc": """**Từ khóa:** 不但没有 búdàn méiyǒu (Chẳng những không), 反而 fǎn'ér (Ngược lại còn).\n
**Cấu trúc:** $A + 不但没有 + V1, 反而 + V2$\n
Dùng khi kết quả trái ngược hoàn toàn với mong đợi ban đầu.\n
**Ví dụ:** 雨 (Yǔ) chẳng những không tạnh (不但没有停 - búdàn méiyǒu tíng), ngược lại còn càng mưa càng to (反而越下越大 - fǎn'ér yuè xià yuè dà)."""
    },
    {
        "id": "h4_7",
        "title": "Cấu trúc 'Nếu như... thì...'",
        "pinyin": "jiǎrú... jiù... (假如...就...)",
        "desc": """**Từ khóa:** 假如 jiǎrú (Giả sử/Nếu như), 就 jiù (Thì).\n
**Cấu trúc:** $假如 + [Giả thuyết], 就 + [Kết quả]$\n
Dùng trong văn viết nhiều hơn 如果 (rúguǒ).\n
**Ví dụ:** 假如 (Jiǎrú) có thời gian (有时间 - yǒu shíjiān), tôi sẽ đi du lịch (我就去旅游 - wǒ jiù qù lǚyóu)."""
    },
    {
        "id": "h4_8",
        "title": "Phó từ 'Rốt cuộc' (Cặp 到底 - 究竟)",
        "pinyin": "dàodǐ (到底) / jiūjìng (究竟)",
        "desc": """**Từ khóa:** 到底 dàodǐ / 究竟 jiūjìng (Rốt cuộc/Cuối cùng thì).\n
**Cấu trúc:** $S + 到底/究竟 + V/Adj?$\n
Dùng trong câu hỏi để truy cứu đến cùng sự thật.\n
**Ví dụ:** 你 (Nǐ) rốt cuộc muốn làm gì (到底想做什么 - dàodǐ xiǎng zuò shénme)?"""
    },
    {
        "id": "h4_9",
        "title": "Cấu trúc 'Không những... mà còn...' nâng cao",
        "pinyin": "bùjǐn... érqiě... (不仅...而且...)",
        "desc": """**Từ khóa:** 不仅 bùjǐn (Không chỉ), 而且 érqiě (Mà còn).\n
**Cấu trúc:** $S + 不仅 + A, 而且 + B$\n
**Ví dụ:** 他 (Tā) không chỉ thông minh (不仅聪明 - bùjǐn cōngmíng), mà còn rất nhiệt tình (而且很热情 - érqiě hěn rèqíng)."""
    },
    {
        "id": "h4_10",
        "title": "Cấu trúc 'Ước gì / Phải chi'",
        "pinyin": "yàoshì... jiù hǎo le (要是...就好了)",
        "desc": """**Từ khóa:** 要是 yàoshì (Nếu như), 就好了 jiù hǎo le (Thì tốt rồi).\n
**Cấu trúc:** $要是 + [Ước muốn] + 就好了$\n
**Ví dụ:** 要是 (Yàoshì) bây giờ là mùa hè (现在是夏天 - xiànzài shì xiàtiān) thì tốt rồi (就好了 - jiù hǎo le)."""
    },
    {
        "id": "h4_11",
        "title": "Phó từ chỉ sự 'Vốn dĩ'",
        "pinyin": "běnlái (本来)",
        "desc": """**Từ khóa:** 本来 běnlái (Vốn dĩ/Lẽ ra).\n
**Cấu trúc:** $S + 本来 + V + (O)$\n
Dùng để chỉ tình huống ban đầu hoặc một lẽ đương nhiên.\n
**Ví dụ:** 我 (Wǒ) vốn dĩ định đi (本来打算去 - běnlái dǎsuàn qù), nhưng lại có việc (但是又有事了 - dànshì yòu yǒu shì le)."""
    },
    {
        "id": "h4_12",
        "title": "Cách dùng 'Suýt nữa thì...'",
        "pinyin": "chàdiǎnr (差点儿)",
        "desc": """**Từ khóa:** 差点儿 chàdiǎnr (Suýt nữa).\n
**Cấu trúc:** $S + 差点儿 + [V/Kết quả]$\n
Nếu là việc không mong muốn: Khẳng định hay phủ định đều nghĩa là "suýt bị".\n
**Ví dụ:** 我 (Wǒ) suýt nữa thì quên (差点儿忘了 - chàdiǎnr wàng le) = Suýt nữa thì không quên."""
    },
    {
        "id": "h4_13",
        "title": "Cấu trúc 'Tạm thời / Trước mắt'",
        "pinyin": "zànshí (暂时)",
        "desc": """**Từ khóa:** 暂时 zànshí (Tạm thời).\n
**Cấu trúc:** $S + 暂时 + V + (O)$\n
**Ví dụ:** 这个任务 (Zhè ge rènwu) tạm thời gác lại (暂时放一下 - zànshí fàng yíxià)."""
    },
    {
        "id": "h4_14",
        "title": "Cấu trúc 'Để tránh / Khỏi phải'",
        "pinyin": "yǐmiǎn (以免)",
        "desc": """**Từ khóa:** 以免 yǐmiǎn (Để tránh/Khỏi phải).\n
**Cấu trúc:** $Phân câu A, 以免 + Phân câu B$\n
**Ví dụ:** 请 (Qǐng) mang theo ô (带上雨伞 - dài shàng yǔsǎn), để tránh bị ướt (以免淋湿 - yǐmiǎn línshī)."""
    }
],
    # Bạn có thể thêm tiếp cho đến HSK 6 ở đây...
    6: [
        {"id": "h6_1", "title": "Cấu trúc '与其...不如...'", "desc": "Thay vì... thà rằng..."},
    ]
}
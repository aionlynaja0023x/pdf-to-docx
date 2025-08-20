# PDF to DOCX Converter

โปรแกรมแปลงไฟล์ PDF เป็น DOCX ที่รองรับภาษาไทย พร้อมการปรับแต่งฟอนต์อัตโนมัติ

## คุณสมบัติ

- แปลงไฟล์ PDF เป็น DOCX ได้อย่างแม่นยำ
- รองรับภาษาไทยและตัวอักษรพิเศษ
- ปรับใช้ฟอนต์ TH SarabunPSK อัตโนมัติ
- จัดการข้อผิดพลาดอย่างมีประสิทธิภาพ
- มีการแสดงสถานะการทำงานแบบ Real-time

## การติดตั้ง

1. ติดตั้ง Python 3.7 หรือเวอร์ชันที่ใหม่กว่า
2. ติดตั้ง dependencies:

```bash
pip install -r requirements.txt
```

## การใช้งาน

### ใช้งานผ่าน Command Line

```bash
python pdfdocx.py
```

### ใช้งานในโค้ด

```python
from pdfdocx import convert_pdf_to_docx_final

# แปลงไฟล์ PDF เป็น DOCX
convert_pdf_to_docx_final("input.pdf", "output.docx")
```

## โครงสร้างไฟล์

```
pdftodocx/
├── pdfdocx.py          # ไฟล์หลักของโปรแกรม
├── input.pdf           # ไฟล์ PDF ตัวอย่าง
├── output_final0.docx  # ไฟล์ DOCX ผลลัพธ์
└── README.md           # ไฟล์นี้
```

## Dependencies

- `pdf2docx` - สำหรับแปลง PDF เป็น DOCX
- `python-docx` - สำหรับจัดการไฟล์ DOCX
- `lxml` - สำหรับ XML processing

## ข้อกำหนดระบบ

- Python 3.7+
- ฟอนต์ TH SarabunPSK (สำหรับการแสดงผลภาษาไทย)

## การแก้ไขปัญหา

### ปัญหาฟอนต์ภาษาไทย
หากไม่มีฟอนต์ TH SarabunPSK ในระบบ สามารถเปลี่ยนเป็นฟอนต์อื่นได้โดยแก้ไขในไฟล์ `pdfdocx.py`:

```python
font.name = 'TH SarabunPSK'  # เปลี่ยนเป็นฟอนต์ที่มีในระบบ
```

## License

MIT License - ดูรายละเอียดในไฟล์ LICENSE

## ผู้พัฒนา

พัฒนาโดย [ชื่อของคุณ] - สำหรับการใช้งานส่วนตัวและเชิงพาณิชย์

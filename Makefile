# Makefile สำหรับ PDF to DOCX Converter
# Makefile for PDF to DOCX Converter

.PHONY: help install test clean run example setup

# ตัวแปร
PYTHON = python3
PIP = pip3
PROJECT_NAME = pdf-to-docx
VERSION = 1.0.0

# เป้าหมายเริ่มต้น
help:
	@echo "PDF to DOCX Converter - Makefile"
	@echo "================================"
	@echo ""
	@echo "คำสั่งที่ใช้งานได้:"
	@echo "  install    - ติดตั้ง dependencies"
	@echo "  test       - รันการทดสอบ"
	@echo "  run        - รันโปรแกรมหลัก"
	@echo "  example    - รันตัวอย่างการใช้งาน"
	@echo "  clean      - ลบไฟล์ชั่วคราว"
	@echo "  setup      - ติดตั้งโปรเจค"
	@echo "  help       - แสดงความช่วยเหลือนี้"

# ติดตั้ง dependencies
install:
	@echo "กำลังติดตั้ง dependencies..."
	$(PIP) install -r requirements.txt
	@echo "✅ ติดตั้ง dependencies เสร็จสิ้น"

# รันการทดสอบ
test:
	@echo "กำลังรันการทดสอบ..."
	$(PYTHON) test_pdfdocx.py
	@echo "✅ การทดสอบเสร็จสิ้น"

# รันโปรแกรมหลัก
run:
	@echo "กำลังรันโปรแกรมหลัก..."
	$(PYTHON) pdfdocx.py
	@echo "✅ โปรแกรมทำงานเสร็จสิ้น"

# รันตัวอย่างการใช้งาน
example:
	@echo "กำลังรันตัวอย่างการใช้งาน..."
	$(PYTHON) examples.py
	@echo "✅ ตัวอย่างการใช้งานเสร็จสิ้น"

# ติดตั้งโปรเจค
setup:
	@echo "กำลังติดตั้งโปรเจค..."
	$(PYTHON) setup.py install
	@echo "✅ ติดตั้งโปรเจคเสร็จสิ้น"

# ลบไฟล์ชั่วคราว
clean:
	@echo "กำลังลบไฟล์ชั่วคราว..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -type f -name "*.docx" ! -name "*.docx" -delete
	@find . -type f -name "*.log" -delete
	@echo "✅ ลบไฟล์ชั่วคราวเสร็จสิ้น"

# สร้าง package
package:
	@echo "กำลังสร้าง package..."
	$(PYTHON) setup.py sdist bdist_wheel
	@echo "✅ สร้าง package เสร็จสิ้น"

# อัพโหลดไปยัง PyPI (ต้องมี account)
upload:
	@echo "กำลังอัพโหลดไปยัง PyPI..."
	$(PIP) install twine
	twine upload dist/*
	@echo "✅ อัพโหลดเสร็จสิ้น"

# ตรวจสอบ package
check:
	@echo "กำลังตรวจสอบ package..."
	$(PYTHON) setup.py check
	@echo "✅ ตรวจสอบ package เสร็จสิ้น"

# แสดงข้อมูลโปรเจค
info:
	@echo "ข้อมูลโปรเจค:"
	@echo "  ชื่อ: $(PROJECT_NAME)"
	@echo "  เวอร์ชัน: $(VERSION)"
	@echo "  Python: $(shell $(PYTHON) --version)"
	@echo "  Pip: $(shell $(PIP) --version)"

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ไฟล์ทดสอบสำหรับ PDF to DOCX Converter
Test file for PDF to DOCX Converter
"""

import unittest
import os
import tempfile
import shutil
from pdfdocx import convert_pdf_to_docx_final

class TestPDFToDOCX(unittest.TestCase):
    """คลาสทดสอบสำหรับ PDF to DOCX Converter"""
    
    def setUp(self):
        """ตั้งค่าก่อนการทดสอบแต่ละครั้ง"""
        # สร้างโฟลเดอร์ชั่วคราวสำหรับการทดสอบ
        self.test_dir = tempfile.mkdtemp()
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir)
        
        # สร้างไฟล์ PDF ตัวอย่าง (ไฟล์ว่าง)
        self.test_pdf = "test.pdf"
        with open(self.test_pdf, "wb") as f:
            # เขียนข้อมูล PDF header แบบง่าย
            f.write(b"%PDF-1.4\n1 0 obj\n<<\n/Type /Catalog\n/Pages 2 0 R\n>>\nendobj\n2 0 obj\n<<\n/Type /Pages\n/Kids [3 0 R]\n/Count 1\n>>\nendobj\n3 0 obj\n<<\n/Type /Page\n/Parent 2 0 R\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n>>\nendobj\n4 0 obj\n<<\n/Length 0\n>>\nstream\nendstream\nendobj\nxref\n0 5\n0000000000 65535 f \n0000000009 00000 n \n0000000058 00000 n \n0000000115 00000 n \n0000000204 00000 n \ntrailer\n<<\n/Size 5\n/Root 1 0 R\n>>\nstartxref\n297\n%%EOF")
    
    def tearDown(self):
        """ทำความสะอาดหลังการทดสอบแต่ละครั้ง"""
        # กลับไปยังโฟลเดอร์เดิม
        os.chdir(self.original_dir)
        
        # ลบโฟลเดอร์ชั่วคราว
        shutil.rmtree(self.test_dir)
    
    def test_file_exists_check(self):
        """ทดสอบการตรวจสอบไฟล์ PDF ที่มีอยู่"""
        # ทดสอบกับไฟล์ที่มีอยู่จริง
        result = convert_pdf_to_docx_final(self.test_pdf, "test_output.docx")
        # ควรจะไม่เกิด error จากการไม่พบไฟล์
        self.assertIsInstance(result, bool)
    
    def test_file_not_exists(self):
        """ทดสอบการตรวจสอบไฟล์ PDF ที่ไม่มีอยู่"""
        # ทดสอบกับไฟล์ที่ไม่มีอยู่
        result = convert_pdf_to_docx_final("nonexistent.pdf", "test_output.docx")
        # ควรจะ return False
        self.assertFalse(result)
    
    def test_output_file_creation(self):
        """ทดสอบการสร้างไฟล์ output"""
        output_file = "test_output.docx"
        
        # แปลงไฟล์
        result = convert_pdf_to_docx_final(self.test_pdf, output_file)
        
        # ตรวจสอบว่าไฟล์ output ถูกสร้างขึ้นหรือไม่
        # (แม้ว่าการแปลงอาจจะล้มเหลว แต่ไฟล์อาจถูกสร้างขึ้น)
        if result:
            self.assertTrue(os.path.exists(output_file))
    
    def test_invalid_pdf_handling(self):
        """ทดสอบการจัดการไฟล์ PDF ที่ไม่ถูกต้อง"""
        # สร้างไฟล์ที่ไม่ใช่ PDF
        invalid_pdf = "invalid.txt"
        with open(invalid_pdf, "w") as f:
            f.write("This is not a PDF file")
        
        output_file = "test_output.docx"
        result = convert_pdf_to_docx_final(invalid_pdf, output_file)
        
        # ควรจะจัดการข้อผิดพลาดได้อย่างเหมาะสม
        self.assertIsInstance(result, bool)
    
    def test_output_filename_generation(self):
        """ทดสอบการสร้างชื่อไฟล์ output"""
        # ทดสอบการสร้างชื่อไฟล์ output ที่แตกต่างกัน
        test_cases = [
            ("test.pdf", "output.docx"),
            ("document.pdf", "result.docx"),
            ("file.pdf", "converted.docx")
        ]
        
        for pdf_file, docx_file in test_cases:
            if os.path.exists(pdf_file):
                result = convert_pdf_to_docx_final(pdf_file, docx_file)
                self.assertIsInstance(result, bool)

def run_tests():
    """รันการทดสอบทั้งหมด"""
    print("เริ่มการทดสอบ PDF to DOCX Converter...")
    print("=" * 50)
    
    # สร้าง test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestPDFToDOCX)
    
    # รันการทดสอบ
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("=" * 50)
    if result.wasSuccessful():
        print("✅ การทดสอบทั้งหมดผ่าน!")
        return 0
    else:
        print("❌ การทดสอบบางส่วนล้มเหลว")
        return 1

if __name__ == "__main__":
    exit_code = run_tests()
    exit(exit_code)

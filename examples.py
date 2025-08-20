#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ตัวอย่างการใช้งาน PDF to DOCX Converter
Examples for PDF to DOCX Converter
"""

from pdfdocx import convert_pdf_to_docx_final
import os

def example_basic_usage():
    """ตัวอย่างการใช้งานพื้นฐาน"""
    print("=== ตัวอย่างการใช้งานพื้นฐาน ===")
    
    # ตรวจสอบว่าไฟล์ input.pdf มีอยู่หรือไม่
    if os.path.exists("input.pdf"):
        success = convert_pdf_to_docx_final("input.pdf", "example_output.docx")
        if success:
            print("✅ แปลงไฟล์สำเร็จ!")
        else:
            print("❌ การแปลงไฟล์ล้มเหลว")
    else:
        print("⚠️  ไม่พบไฟล์ input.pdf กรุณาเตรียมไฟล์ PDF ก่อน")

def example_custom_names():
    """ตัวอย่างการใช้งานด้วยชื่อไฟล์ที่กำหนดเอง"""
    print("\n=== ตัวอย่างการใช้งานด้วยชื่อไฟล์ที่กำหนดเอง ===")
    
    # ตัวอย่างการแปลงไฟล์หลายไฟล์
    pdf_files = ["input.pdf"]  # เพิ่มไฟล์ PDF อื่นๆ ที่นี่
    
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            # สร้างชื่อไฟล์ output โดยเปลี่ยนนามสกุล
            base_name = os.path.splitext(pdf_file)[0]
            docx_file = f"{base_name}_converted.docx"
            
            print(f"กำลังแปลง: {pdf_file} -> {docx_file}")
            success = convert_pdf_to_docx_final(pdf_file, docx_file)
            
            if success:
                print(f"✅ แปลง {pdf_file} สำเร็จ!")
            else:
                print(f"❌ การแปลง {pdf_file} ล้มเหลว")
        else:
            print(f"⚠️  ไม่พบไฟล์ {pdf_file}")

def example_batch_processing():
    """ตัวอย่างการประมวลผลแบบ batch"""
    print("\n=== ตัวอย่างการประมวลผลแบบ batch ===")
    
    # ค้นหาไฟล์ PDF ทั้งหมดในโฟลเดอร์ปัจจุบัน
    pdf_files = [f for f in os.listdir(".") if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("⚠️  ไม่พบไฟล์ PDF ในโฟลเดอร์ปัจจุบัน")
        return
    
    print(f"พบไฟล์ PDF {len(pdf_files)} ไฟล์:")
    for pdf_file in pdf_files:
        print(f"  - {pdf_file}")
    
    # สร้างโฟลเดอร์สำหรับเก็บไฟล์ผลลัพธ์
    output_dir = "converted_files"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"สร้างโฟลเดอร์ {output_dir}")
    
    # แปลงไฟล์ทั้งหมด
    success_count = 0
    for pdf_file in pdf_files:
        docx_file = os.path.join(output_dir, f"{os.path.splitext(pdf_file)[0]}.docx")
        
        print(f"\nกำลังแปลง: {pdf_file} -> {docx_file}")
        success = convert_pdf_to_docx_final(pdf_file, docx_file)
        
        if success:
            success_count += 1
            print(f"✅ แปลง {pdf_file} สำเร็จ!")
        else:
            print(f"❌ การแปลง {pdf_file} ล้มเหลว")
    
    print(f"\n=== สรุปผลการแปลง ===")
    print(f"ไฟล์ทั้งหมด: {len(pdf_files)} ไฟล์")
    print(f"แปลงสำเร็จ: {success_count} ไฟล์")
    print(f"แปลงล้มเหลว: {len(pdf_files) - success_count} ไฟล์")

if __name__ == "__main__":
    print("PDF to DOCX Converter - ตัวอย่างการใช้งาน")
    print("=" * 50)
    
    # รันตัวอย่างต่างๆ
    example_basic_usage()
    example_custom_names()
    example_batch_processing()
    
    print("\n" + "=" * 50)
    print("จบการแสดงตัวอย่างการใช้งาน")
    print("\nสำหรับข้อมูลเพิ่มเติม กรุณาอ่าน README.md")

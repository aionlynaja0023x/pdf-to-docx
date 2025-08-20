import os
import sys
import argparse
from pdf2docx import Converter
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn

def convert_pdf_to_docx_final(pdf_path: str, docx_path: str):
    """
    แปลงไฟล์ PDF เป็น DOCX (เวอร์ชันแก้ไขสมบูรณ์)
    - แก้ไขการเรียก close() ซ้ำซ้อน
    - จัดการไฟล์และข้อผิดพลาดด้วย try...finally
    - ปรับฟอนต์ภาษาไทยหลังการแปลง
    """
    if not os.path.exists(pdf_path):
        print(f"!! ข้อผิดพลาด: ไม่พบไฟล์ PDF ที่ '{pdf_path}'")
        return False

    print(f"-> เริ่มต้นกระบวนการแปลงไฟล์: {os.path.basename(pdf_path)}")
    
    cv = None  # กำหนดตัวแปรไว้ก่อน
    try:
        print("   [1/3] กำลังแปลง PDF เป็น DOCX...")
        cv = Converter(pdf_path)
        cv.convert(docx_path, start=0, end=None)
        # --- ลบ cv.close() จากตรงนี้ ---
        
        print(f"   [2/3] แปลงไฟล์เป็น DOCX สำเร็จ: {os.path.basename(docx_path)}")

        print("   [3/3] กำลังปรับใช้ฟอนต์ภาษาไทย (TH SarabunPSK)...")
        doc = Document(docx_path)
        style = doc.styles['Normal']
        font = style.font
        font.name = 'TH SarabunPSK'
        font.size = Pt(14)
        rpr = style.element.rPr
        rpr.rFonts.set(qn('w:eastAsia'), 'TH SarabunPSK')

        for paragraph in doc.paragraphs:
            for run in paragraph.runs:
                run.font.name = 'TH SarabunPSK'
                r = run._element
                r.rPr.rFonts.set(qn('w:eastAsia'), 'TH SarabunPSK')

        doc.save(docx_path)
        print("-> กระบวนการเสร็จสมบูรณ์!")
        return True

    except Exception as e:
        print(f"!! เกิดข้อผิดพลาดร้ายแรงระหว่างการทำงาน: {str(e)}")
        return False
    
    finally:
        # เหลือ cv.close() ไว้ที่นี่ที่เดียวพอ
        # เพื่อรับประกันว่า Converter จะถูกปิดเสมอ และถูกปิดเพียงครั้งเดียว
        if cv:
            cv.close()
            print("   [+] ปิดตัวแปลงไฟล์เรียบร้อย")

def main():
    """ฟังก์ชันหลักสำหรับการใช้งาน command line"""
    parser = argparse.ArgumentParser(
        description="แปลงไฟล์ PDF เป็น DOCX พร้อมรองรับภาษาไทย",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
ตัวอย่างการใช้งาน:
  python pdfdocx.py input.pdf output.docx
  python pdfdocx.py -i input.pdf -o output.docx
  python pdfdocx.py --input input.pdf --output output.docx
        """
    )
    
    parser.add_argument(
        "input", 
        nargs="?", 
        help="ไฟล์ PDF ที่ต้องการแปลง"
    )
    parser.add_argument(
        "output", 
        nargs="?", 
        help="ไฟล์ DOCX ที่จะสร้างขึ้น"
    )
    parser.add_argument(
        "-i", "--input",
        help="ไฟล์ PDF ที่ต้องการแปลง"
    )
    parser.add_argument(
        "-o", "--output",
        help="ไฟล์ DOCX ที่จะสร้างขึ้น"
    )
    
    args = parser.parse_args()
    
    # กำหนดไฟล์ input และ output
    pdf_file = args.input or args.input or args.input
    docx_file = args.output or args.output or args.output
    
    # ถ้าไม่ระบุ argument ให้ใช้ค่าเริ่มต้น
    if not pdf_file:
        pdf_file = "input.pdf"
    if not docx_file:
        docx_file = "output.docx"
    
    # ตรวจสอบว่าไฟล์ input มีอยู่จริงหรือไม่
    if not os.path.exists(pdf_file):
        print(f"!! ข้อผิดพลาด: ไม่พบไฟล์ PDF ที่ '{pdf_file}'")
        print("   กรุณาตรวจสอบชื่อไฟล์และตำแหน่งที่ตั้ง")
        sys.exit(1)
    
    # เริ่มการแปลง
    success = convert_pdf_to_docx_final(pdf_file, docx_file)
    
    if success:
        print(f"\n✅ แปลงไฟล์สำเร็จ!")
        print(f"   ไฟล์ต้นฉบับ: {pdf_file}")
        print(f"   ไฟล์ผลลัพธ์: {docx_file}")
        sys.exit(0)
    else:
        print(f"\n❌ การแปลงไฟล์ล้มเหลว")
        sys.exit(1)

# --- ตัวอย่างการใช้งาน ---
if __name__ == "__main__":
    main()

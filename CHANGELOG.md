# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- เพิ่มการรองรับ command line arguments
- เพิ่มฟังก์ชัน main() สำหรับการใช้งาน command line
- เพิ่มไฟล์ตัวอย่างการใช้งาน (examples.py)
- เพิ่มไฟล์ทดสอบ (test_pdfdocx.py)
- เพิ่ม Makefile สำหรับการจัดการโปรเจค
- เพิ่มไฟล์ setup.py สำหรับการติดตั้ง

### Changed
- ปรับปรุงการจัดการข้อผิดพลาดให้ดีขึ้น
- ปรับปรุงการแสดงผลข้อความให้ชัดเจนขึ้น

## [1.0.0] - 2024-12-19

### Added
- ฟังก์ชันแปลงไฟล์ PDF เป็น DOCX
- การรองรับภาษาไทยและตัวอักษรพิเศษ
- การปรับใช้ฟอนต์ TH SarabunPSK อัตโนมัติ
- การจัดการข้อผิดพลาดอย่างมีประสิทธิภาพ
- การแสดงสถานะการทำงานแบบ Real-time

### Technical Details
- ใช้ library `pdf2docx` สำหรับการแปลง PDF
- ใช้ library `python-docx` สำหรับการจัดการไฟล์ DOCX
- รองรับ Python 3.7+

## [0.1.0] - 2024-12-18

### Added
- โครงสร้างพื้นฐานของโปรเจค
- ฟังก์ชันแปลงไฟล์พื้นฐาน
- การรองรับภาษาไทยเบื้องต้น

---

## การแปลคำ

- **Added** = เพิ่มใหม่
- **Changed** = เปลี่ยนแปลง
- **Deprecated** = ถูกยกเลิก
- **Removed** = ลบออก
- **Fixed** = แก้ไข
- **Security** = ความปลอดภัย

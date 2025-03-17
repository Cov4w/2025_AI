import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout, QListWidget

class AddressBookApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # 주소록 데이터를 저장할 리스트
        self.address_book = []
        
        # UI 설정
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('주소록 프로그램')
        
        # 레이아웃 설정
        layout = QVBoxLayout()
        
        # 이름 입력
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('이름 입력')
        
        # 전화번호 입력
        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText('전화번호 입력')
        
        # 추가 버튼
        self.add_button = QPushButton('추가', self)
        self.add_button.clicked.connect(self.add_contact)
        
        # 검색 입력
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText('검색할 이름 입력')
        
        # 찾기 버튼
        self.search_button = QPushButton('찾기', self)
        self.search_button.clicked.connect(self.search_contact)
        
        # 검색 결과 출력 레이블
        self.search_result = QLabel(self)
        
        # 연락처 목록 표시
        self.contact_list = QListWidget(self)
        
        # 레이아웃에 위젯 추가
        layout.addWidget(self.name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.search_result)
        layout.addWidget(self.contact_list)
        
        self.setLayout(layout)
        
        self.show()
    
    def add_contact(self):
        # 이름과 전화번호를 입력받아 주소록에 추가
        name = self.name_input.text()
        phone = self.phone_input.text()
        
        if name and phone:
            self.address_book.append((name, phone))
            self.update_contact_list()
            self.name_input.clear()
            self.phone_input.clear()
    
    def search_contact(self):
        # 검색된 이름을 찾아서 결과를 표시
        search_name = self.search_input.text().lower()
        found = False
        for name, phone in self.address_book:
            if search_name in name.lower():
                self.search_result.setText(f"찾은 연락처: {name} - {phone}")
                found = True
                break
        
        if not found:
            self.search_result.setText("결과 없음")
    
    def update_contact_list(self):
        # 연락처 목록 갱신
        self.contact_list.clear()
        for name, phone in self.address_book:
            self.contact_list.addItem(f"{name}: {phone}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddressBookApp()
    sys.exit(app.exec_())

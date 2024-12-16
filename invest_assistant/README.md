### 가상환경 생성
python -m venv invest

### 가상환경 활성화
source invest/bin/activate

### alias 설정
alias python=python3
alias pip=pip3

### 가상환경 비활성화
deactivate

### requirements.txt 생성
pip freeze > requirements.txt

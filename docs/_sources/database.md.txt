# 데이터베이스

LAMP에서는 LS-Dyna의 물성 데이터를 저장 및 공유하기 위한 데이터베이스 인터페이스를 제공합니다. 현재 LAMP에서는 MariaDB를 활용하여 개발하고 있기 때문에 데이터베이스 서버에 MariaDB 설치가 필요합니다. 제한된 환경에서 테스트 되고 있기에 다음 환경에서 MariaDB를 활용한 LAMP 사용이 가능합니다. 사용 가능한 환경에 대한 정보는 향후에 테스트 후 추가 될 예정입니다.

* OS : Windows 10 or 11
* MariaDB Version : 10.5.3

## 1. MariaDB 설치 및 현대제철 물성 추가
LAMP에서는 Steel계열의 현대제철 물성 데이터를 제공하고 있습니다. 현대제철 물성을 사용하기 위해서는 LAMP Server, MariaDB를 설치 후 LAMP Server에서 제공되는 현대제철 물성 데이터 (hyundaisteel_db.sql)파일을 로드 하여야 합니다. 자세한 내용은 [LAMP Server 설치](start_lamp.md/#22-lamp-server-설치), [MariaDB 설치](start_lamp.md/#41-mariadb-설치) 그리고 [현대제철 물성 적용](start_lamp.md/#42-현대제철-물성-추가)에서 확인 할 수 있습니다. 
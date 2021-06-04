# StudyRaspberry

## 1. Raspberry Pi 설정

- SDCardFormatter로 SD card 포맷
- Win32Imager로 '라즈베리 이미지 파일' 로드
- wpa_supplicant.conf file 생성

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=KR

network={
	   ssid="iot3"
	   psk="iot123456"
	   key_mgmt=WPA-PSK
}

```
- SSH file 생성

## 2. Port 설정

- Mac address / IP 확인
- 내부 포트 / 외부 포트 설정
- SSH / VNC port 설정
- 고정 ip 설정 (sudo nano /etc/dhcpcd.conf)
```
#interface wlan0
#static ip_address=192.168.0.11
#static routers=192.168.0.1
#static domain_name_servers=168.126.63.1 8.8.8.8

```

## 3. Update 및 버전 변경

- sudo nano /etc/nanorc
- sudo apt-get update or upgrade
- sudo ln -f /user/bin/python3.7 /user/bin/python

## 4. 폰트 사용
- sudo apt-get install fonts-nanum fonts-nanum-extra(폰트 생성)
- sudo apt-get install fonts-unfonts-core(폰트 등록)
- sudo apt-get install fcitx-hangul (fcitx 설치)
- 기본설정 : Fctix /  입력기 설정
- sudo pcmanfm -> default -> im-config -> mode : fctix변경

## 5. 폴더 및 파일 생성
- mkdir (directory name) : 디렉토리 생성
- cd (directory name) : 디렉토리 들어가기
- cd .. : 상워 디렉토리로 이동
- nano (file name) : file 생성 및 들어가기
- gcc (file name) -o (실행 file name) : 실행 파일 생성
 
 # IoT Control - WebPage
 [IoT control ](/IoT%20contloer/README.md) <br>

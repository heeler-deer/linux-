#!/usr/bin/expect -f



spawn sftp sftp@your ftp ip
    expect "password:"
    # 输入密码，并等待FTP提示符的出现
    send "your password\n"
    
    expect "sftp>"
    # 下载所有文件
    send "put your file path\n"
    expect "ftp>"
    # 退出此次ftp会话，并等待服务器的退出提示EOF
    send "bye\r"
    expect eof



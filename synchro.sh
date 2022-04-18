#!/usr/bin/expect -f


                  # 设置超时时间
 
# 向远程服务器请求打开一个FTP会话，并等待服务器询问用户名
spawn sftp sftp@45.32.72.148
    expect "password:"
    # 输入密码，并等待FTP提示符的出现
    send "L3498H1091\n"
    
    expect "sftp>"
    # 下载所有文件
    send "put /home/heeler/Zotero/storage.tar.gz\n"
    expect "ftp>"
    # 退出此次ftp会话，并等待服务器的退出提示EOF
    send "bye\r"
    expect eof



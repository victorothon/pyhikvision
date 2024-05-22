## pyhikvision [Flash and glittering crystal, star a good mood]
![GitHub](https://img.shields.io/github/license/Rennbon/pyhikvision)
![release](https://img.shields.io/github/v/release/Rennbon/pyhikvision)
![python](https://img.shields.io/badge/python-3.10.4-brightgreen)
![platform](https://img.shields.io/badge/platform-Linux64|Linux32|win64|win32-lightgrey)
-In support Linux, Windows under 32 -bit and 64 -bit systems
-Python mapping for the basic types in the official interface document, which can simplify the complexity of the interface entry and exit

Note：The library incorporates the object -oriented concept. Theoretically after understanding this library, the complexity of the later iteration maintenance will be greatly reduced
 
## New change
- Video preview uses TK instead of win32gui to solve the problem of unresponsive and cross -platform problems
- Remove the PC system type configuration
- 32/64 Automatically distinguish the specific variable type
## Branch feature/rennbon With the implementation of RSTP, adding a little step can improve some performance

## Supporting understanding of SDK secondary development principle
- pyhivision uses guidelines https://www.jianshu.com/p/c3c4bf3d1ef8
- Comparison of the official audio and video technical solution of Hikvision https://open.hikvision.com/docs/docId?productId=612781c8ec4acb28e0e1c0c3&version=%2Fff026cfc47a14e79a6c9acf21d9d8769&curNodeId=2e231666a7854dc4a2dc29b9ed06782a
- 官方硬件产品文档 https://open.hikvision.com/docs/docId?productId=5cda567cf47ae80dd41a54b3&version=%2F16e18c75bd644f1dbf9e8301d6fc9b73&tagPath=%E9%80%9A%E7%94%A8%E8%A7%86%E9%A2%91-%E5%AE%9E%E6%97%B6%E9%A2%84%E8%A7%88

### hint
- Some of the SDKs of some devices in Haikang need to be related to Haikang's technology. The version of the official website may not be right. Some developers have encountered this problem. Please pay attention.Know if the SDK corresponds.
- Error code list https://open.hikvision.com/hardware/definitions/NET_DVR_GetLastError.html

### macOS Development recommendation
Virtual tool：https://www.parallels.cn/pd/general/
Can be installed directly Linux and windows，And it can be independent to the application level, which is very suitable for development of Haikangwei. It is better than cloud server or docker

### Hikvision Resources Download
Official resources：https://open.hikvision.com/download/5cda567cf47ae80dd41a54b3?type=10
netdisc：https://pan.baidu.com/s/1xe3wXH7CYIswPgx59y4XWg Extraction code:oqd5

pyhikvision The latest corresponding SDK version is as follows：
- Equipment network SDK V6.1.9.4_build20220412
- Play library SDK V7.3.9.50_build20210106
- Password reset assistant https://www.hikvision.com/cn/password-reset/#download-agreement

## Initialization of the development environment
### 1. venv（recommend，PyCharm Start directly）
### 2. conda environment （Need installation conda，Download, please jump to https://anaconda.org/anaconda/conda）
packages.yml middle prefix for conda env In the directory, the child environment settings need to be modified in conjunction with its own system environment

```
conda env create  -f .\packages.yml
```

## Quick Start
### local_config.ini Configuration（In the main directory config.ini change into local_config.ini To）
Notice windows Directory segmentation
```
[DEFAULT]
SDKPath: .dll or .so The root directory will traverse loading, fill in the roots SDK Directory can
User: To access the user name of the camera, you need to configure it yourself on Hikvision's graphic interface
Password: The camera access the password, you need to configure it yourself on Hikvision's graphic interface
Port: Camera port
IP: Camera IP

```
### Example startup method

```
cd example
python xxx.py
```

## SDK configuration related
### Linux SDK loading 107 problem solution
1. Add SDK dynamic library path to LD_Library_PATH environment variables

```
# Modify the system pre -increasing package to add a line of Export
vim ~/.bashrc
export  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:{The absolute path in Linux corresponding to the official dynamic library Makeall}: {official dynamic library MakeAll/hcnetsdkcom/absolute path in Linux}
source ~/.bashrc

```

2. Add the SDK path under /etc/ld.so/conf

```
# View configuration information
cat /etc/ld.so.conf
# If there is the following include, it is recommended to create new file settings under ld.so.conf.d, so that the isolation is relatively clean
include ld.so.conf.d/*.conf
# Switch to the specified directory
cd /etc/ld.so.conf.d

vim hikvsdk.conf
# Add the following two paths
{The absolute path in Linux corresponding to the official dynamic library Makeall}
{Official dynamic library MakeAll/HCNETSDKCOM/Absolute path in Linux}

# After saving, execute the following command to reload the system.SO configuration
ldconfig

```

### Notice：

{The absolute path in Linux corresponding to the official dynamic library Makeall} {official dynamic library MakeAll/hcnetsdkcom/in the absolute path in Linux} The corresponding system path needs to be added with "/" because the library Python loading logicThere is no stitching "/"
like:

```
/opt/hkws/lib/
/opt/hkws/lib/HCNetSDKCom/
```

## Maintenance and contact：

Join the discussion group, remember to mark "HKSDK", welcome Star support

1. WeChat group (please add WB343688972 friends or scan the code and add friends, follow the guidance group)

   <img src="./doc/wechat.png" width="200px" >
2. QQ group（901635269）

   <img src="./doc/qq-qr.jpg" width="200px" >


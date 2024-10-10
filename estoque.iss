[Setup]
; Basic settings
AppName=Estoque
AppVersion=1.0
DefaultDirName={pf}\Estoque
DefaultGroupName=Estoque
OutputDir=Output
OutputBaseFilename=EstoqueInstalador
Compression=lzma
SolidCompression=yes

; Application files
[Files]
Source: "dist\adega.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: ".\.env"; DestDir: "{app}"; Flags: ignoreversion

; Create shortcuts
[Icons]
Name: "{group}\Estoque"; Filename: "{app}\adega.exe"
Name: "{group}\Desinstalar Estoque"; Filename: "{uninstallexe}"

; Uninstall settings
[UninstallDelete]
Type: filesandordirs; Name: "{app}"

